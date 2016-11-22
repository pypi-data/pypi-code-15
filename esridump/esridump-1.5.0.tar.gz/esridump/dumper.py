import logging
import requests
import simplejson as json
import socket

from esridump import esri2geojson
from esridump.errors import EsriDownloadError

class EsriDumper(object):
    def __init__(self, url, parent_logger=None,
        extra_query_args=None, extra_headers=None,
        timeout=None, fields=None, request_geometry=True,
        outSR=None):
        self._layer_url = url
        self._query_params = extra_query_args or {}
        self._headers = extra_headers or {}
        self._http_timeout = timeout or 30
        self._fields = fields or None
        self._outSR = outSR or '4326'
        self._request_geometry = request_geometry

        if parent_logger:
            self._logger = parent_logger.getChild('esridump')
        else:
            self._logger = logging.getLogger('esridump')

    def _request(self, method, url, **kwargs):
        try:
            self._logger.debug("Requesting %s with args %s", url, kwargs.get('params') or kwargs.get('data'))
            return requests.request(method, url, timeout=self._http_timeout, **kwargs)
        except requests.exceptions.SSLError:
            self._logger.warning("Retrying %s without SSL verification", url)
            return requests.request(method, url, timeout=self._http_timeout, verify=False, **kwargs)

    def _build_url(self, url=None):
        return self._layer_url + url if url else self._layer_url

    def _build_query_args(self, query_args=None):
        if query_args:
            complete_args = query_args
        else:
            complete_args = {}

        complete_args.update(dict(**self._query_params))

        return complete_args

    def _build_headers(self, headers=None):
        complete_headers = dict(**self._headers)
        if headers:
            complete_headers.update(headers)
        return complete_headers

    def _handle_esri_errors(self, response, error_message):
        if response.status_code != 200:
            raise EsriDownloadError('{}: HTTP {} {}'.format(
                error_message,
                response.status_code,
                response.text,
            ))

        try:
            data = response.json()
        except:
            self._logger.error("Could not parse response from {} as JSON:\n\n{}".format(
                response.request.url,
                response.text,
            ))
            raise

        error = data.get('error')
        if error:
            raise EsriDownloadError("{}: {} {}" .format(
                error_message,
                error['message'],
                ', '.join(error['details']),
            ))

        return data

    def can_handle_pagination(self, query_fields):
        check_args = self._build_query_args({
            'resultOffset': 0,
            'resultRecordCount': 1,
            'where': '1=1',
            'returnGeometry': 'false',
            'outFields': ','.join(query_fields),
            'f': 'json',
        })
        headers = self._build_headers()
        query_url = self._build_url('/query')
        response = self._request('POST', query_url, headers=headers, data=check_args)

        try:
            data = response.json()
        except:
            self._logger.error("Could not parse response from pagination check %s as JSON:\n\n%s",
                response.request.url,
                response.text,
            )
            return False

        return data.get('error') and data['error']['message'] != "Failed to execute query."

    def get_metadata(self):
        query_args = self._build_query_args({
            'f': 'json',
        })
        headers = self._build_headers()
        url = self._build_url()
        response = self._request('GET', url, params=query_args, headers=headers)
        metadata_json = self._handle_esri_errors(response, "Could not retrieve layer metadata")
        return metadata_json

    def get_feature_count(self):
        query_args = self._build_query_args({
            'where': '1=1',
            'returnCountOnly': 'true',
            'f': 'json',
        })
        headers = self._build_headers()
        url = self._build_url('/query')
        response = self._request('GET', url, params=query_args, headers=headers)
        count_json = self._handle_esri_errors(response, "Could not retrieve row count")
        count = count_json.get('count')
        if not count:
            raise EsriDownloadError("Server doesn't support returnCountOnly")
        return count_json['count']

    def _find_oid_field_name(self, metadata):
        oid_field_name = metadata.get('objectIdField')
        if not oid_field_name:
            for f in metadata['fields']:
                if f['type'] == 'esriFieldTypeOID':
                    oid_field_name = f['name']
                    break

        return oid_field_name

    def _get_layer_min_max(self, oid_field_name):
        """ Find the min and max values for the OID field. """
        query_args = self._build_query_args({
            'f': 'json',
            'outFields': '',
            'outStatistics': json.dumps([
                dict(statisticType='min', onStatisticField=oid_field_name, outStatisticFieldName='THE_MIN'),
                dict(statisticType='max', onStatisticField=oid_field_name, outStatisticFieldName='THE_MAX'),
            ], separators=(',', ':'))
        })
        headers = self._build_headers()
        url = self._build_url('/query')
        response = self._request('GET', url, params=query_args, headers=headers)
        metadata = self._handle_esri_errors(response, "Could not retrieve min/max oid values")

        # Some servers (specifically version 10.11, it seems) will respond with SQL statements
        # for the attribute names rather than the requested field names, so pick the min and max
        # deliberately rather than relying on the names.
        min_max_values = metadata['features'][0]['attributes'].values()
        return (min(min_max_values), max(min_max_values))

    def _get_layer_oids(self):
        query_args = self._build_query_args({
            'where': '1=1',  # So we get everything
            'returnIdsOnly': 'true',
            'f': 'json',
        })
        url = self._build_url('/query')
        headers = self._build_headers()
        response = self._request('GET', url, params=query_args, headers=headers)
        oid_data = self._handle_esri_errors(response, "Could not retrieve object IDs")
        return oid_data['objectIds']

    def _fetch_bounded_features(self, envelope, outSR):
        query_args = self._build_query_args({
            'geometry': json.dumps(envelope),
            'geometryType': 'esriGeometryEnvelope',
            'spatialRel': 'esriSpatialRelIntersects',
            'returnCountOnly': 'false',
            'returnIdsOnly': 'false',
            'returnGeometry': self._request_geometry,
            'outSR': outSR,
            'outFields': '*',
            'f': 'json'
        })
        headers = self._build_headers()
        url = self._build_url('/query')
        response = self._request('GET', url, params=query_args, headers=headers)
        features = self._handle_esri_errors(response, "Could not retrieve a section of features")
        return features['features']

    def _split_envelope(self, envelope):
        half_width = (envelope['xmax'] - envelope['xmin']) / 2.0
        half_height = (envelope['ymax'] - envelope['ymin']) / 2.0
        return [
            dict(
                xmin=envelope['xmin'],
                ymin=envelope['ymin'],
                xmax=envelope['xmin'] + half_width,
                ymax=envelope['ymin'] + half_height,
            ),
            dict(
                xmax=envelope['xmin'] + half_width,
                ymin=envelope['ymin'],
                xmin=envelope['xmax'],
                ymax=envelope['ymin'] + half_height,
            ),
            dict(
                xmin=envelope['xmin'],
                ymax=envelope['ymin'] + half_height,
                xmax=envelope['xmin'] + half_width,
                ymin=envelope['ymax'],
            ),
            dict(
                xmax=envelope['xmin'] + half_width,
                ymax=envelope['ymin'] + half_height,
                xmin=envelope['xmax'],
                ymin=envelope['ymax'],
            ),
        ]

    def _scrape_an_envelope(self, envelope, outSR, max_records):
        features = self._fetch_bounded_features(envelope, outSR)

        if len(features) == max_records:
            self._logger.info("Retrieved exactly the maximum record count. Splitting this box and retrieving the children.")

            envelopes = self._split_envelope(envelope)

            for child_envelope in envelopes:
                for feature in self._scrape_an_envelope(child_envelope, outSR, max_records):
                    yield feature
        else:
            for feature in features:
                yield feature

    def __iter__(self):
        query_fields = self._fields
        metadata = self.get_metadata()
        page_size = min(1000, metadata.get('maxRecordCount', 500))
        geometry_type = metadata.get('geometryType')

        try:
            row_count = self.get_feature_count()
        except EsriDownloadError:
            self._logger.info("Source does not support feature count")

            # Use geospatial queries when none of the ID-based methods will work
            oid_field_name = self._find_oid_field_name(metadata)

            if not oid_field_name:
                raise EsriDownloadError("Could not find object ID field name for deduplication")

            bounds = metadata['extent']
            saved = set()

            for feature in self._scrape_an_envelope(bounds, self._outSR, page_size):
                attrs = feature['attributes']
                oid = attrs.get(oid_field_name)
                if oid in saved:
                    continue

                yield esri2geojson(feature)

                saved.add(oid)

            return

        page_args = []

        if metadata.get('supportsPagination') or \
           (metadata.get('advancedQueryCapabilities') and metadata['advancedQueryCapabilities']['supportsPagination']):
            # If the layer supports pagination, we can use resultOffset/resultRecordCount to paginate

            # There's a bug where some servers won't handle these queries in combination with a list of
            # fields specified. We'll make a single, 1 row query here to check if the server supports this
            # and switch to querying for all fields if specifying the fields fails.
            if query_fields and not self.can_handle_pagination(query_fields):
                self._logger.info("Source does not support pagination with fields specified, so querying for all fields.")
                query_fields = None

            for offset in range(0, row_count, page_size):
                query_args = self._build_query_args({
                    'resultOffset': offset,
                    'resultRecordCount': page_size,
                    'where': '1=1',
                    'geometryPrecision': 7,
                    'returnGeometry': self._request_geometry,
                    'outSR': self._outSR,
                    'outFields': ','.join(query_fields or ['*']),
                    'f': 'json',
                })
                page_args.append(query_args)
            self._logger.info("Built %s requests using resultOffset method", len(page_args))
        else:
            # If not, we can still use the `where` argument to paginate

            use_oids = True
            if metadata.get('supportsStatistics'):
                # If the layer supports statistics, we can request maximum and minimum object ID
                # to help build the pages

                oid_field_name = self._find_oid_field_name(metadata)

                if not oid_field_name:
                    raise EsriDownloadError("Could not find object ID field name")

                try:
                    (oid_min, oid_max) = self._get_layer_min_max(oid_field_name)

                    for page_min in range(oid_min - 1, oid_max, page_size):
                        page_max = min(page_min + page_size, oid_max)
                        query_args = self._build_query_args({
                            'where': '{} > {} AND {} <= {}'.format(
                                oid_field_name,
                                page_min,
                                oid_field_name,
                                page_max,
                            ),
                            'geometryPrecision': 7,
                            'returnGeometry': self._request_geometry,
                            'outSR': self._outSR,
                            'outFields': ','.join(query_fields or ['*']),
                            'f': 'json',
                        })
                        page_args.append(query_args)
                    self._logger.info("Built {} requests using OID where clause method".format(len(page_args)))

                    # If we reach this point we don't need to fall through to enumerating all object IDs
                    # because the statistics method worked
                    use_oids = False
                except EsriDownloadError:
                    self._logger.exception("Finding max/min from statistics failed. Trying OID enumeration.")

            if use_oids:
                # If the layer does not support statistics, we can request
                # all the individual IDs and page through them one chunk at
                # a time.

                oids = self._get_layer_oids()

                for i in range(0, len(oids), 100):
                    oid_chunk = map(int, oids[i:i+100])
                    query_args = self._build_query_args({
                        'objectIds': ','.join(map(str, oid_chunk)),
                        'geometryPrecision': 7,
                        'returnGeometry': self._request_geometry,
                        'outSR': self._outSR,
                        'outFields': ','.join(query_fields or ['*']),
                        'f': 'json',
                    })
                    page_args.append(query_args)
                self._logger.info("Built %s requests using OID enumeration method", len(page_args))

        query_url = self._build_url('/query')
        headers = self._build_headers()
        for query_args in page_args:
            try:
                response = self._request('POST', query_url, headers=headers, data=query_args)
                data = self._handle_esri_errors(response, "Could not retrieve this chunk of objects")
            except socket.timeout as e:
                raise EsriDownloadError("Timeout when connecting to URL", e)
            except ValueError as e:
                raise EsriDownloadError("Could not parse JSON", e)
            except Exception as e:
                raise EsriDownloadError("Could not connect to URL", e)

            error = data.get('error')
            if error:
                raise EsriDownloadError("Problem querying ESRI dataset with args {}. Server said: {}".format(query_args, error['message']))

            features = data.get('features')

            for feature in features:
                yield esri2geojson(feature)
