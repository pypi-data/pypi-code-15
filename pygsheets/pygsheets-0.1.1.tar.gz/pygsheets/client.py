# -*- coding: utf-8 -*-.

"""
pygsheets.client
~~~~~~~~~~~~~~~~

This module contains Client class responsible for communicating with
Google SpreadSheet API.

"""
import re
import warnings

from .models import Spreadsheet
from .exceptions import (AuthenticationError, SpreadsheetNotFound,
                         NoValidUrlKeyFound,
                         InvalidArgumentValue, InvalidUser)
from custom_types import *

import httplib2
import os
from json import load as jload

from apiclient import discovery
from apiclient import http as ghttp
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client.service_account import ServiceAccountCredentials
try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

_url_key_re_v1 = re.compile(r'key=([^&#]+)')
_url_key_re_v2 = re.compile(r"/spreadsheets/d/([a-zA-Z0-9-_]+)")


class Client(object):

    """An instance of this class communicates with Google API.

    :param auth: An OAuth2 credential object. Credential objects are those created by the
                 oauth2client library. https://github.com/google/oauth2client

    >>> c = pygsheets.Client(auth=OAuthCredentialObject)


    """
    def __init__(self, auth):
        self.auth = auth
        http = auth.authorize(httplib2.Http(cache="/tmp/.pygsheets_cache", timeout=10))
        discoveryurl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        self.service = discovery.build('sheets', 'v4', http=http,
                                       discoveryServiceUrl=discoveryurl)
        self.driveService = discovery.build('drive', 'v3', http=http)
        self._spreadsheeets = []
        self.batch_requests = dict()
        self.retries = 1

        self._fetch_sheets()

    def _fetch_sheets(self):
        """
        fetch all the sheets info from user's gdrive

        :returns: None
        """
        request = self.driveService.files().list(corpus='user', pageSize=500,
                                                 q="mimeType='application/vnd.google-apps.spreadsheet'",
                                                 fields="files(id, name)")
        results = self._execute_request(None, request, False)
        try:
            results = results['files']
        except KeyError:
            results = []
        self._spreadsheeets = results

    def create(self, title):
        """Creates a spreadsheet, returning a :class:`~pygsheets.Spreadsheet` instance.

        :param title: A title of a spreadsheet.
        """
        body = {'properties': {'title': title}}
        request = self.service.spreadsheets().create(body=body)
        result = self._execute_request(None, request, False)
        self._spreadsheeets.append({'name': title, "id": result['spreadsheetId']})
        return Spreadsheet(self, jsonsheet=result)

    def delete(self, title=None, id=None):
        """Deletes, a spreadsheet by title or id.

        :param title: title of a spreadsheet.
        :param id: id of a spreadsheet this takes precedence if both given.

        :raise pygsheets.SpreadsheetNotFound: if no spreadsheet is found.
        """
        if not id and not title:
            raise SpreadsheetNotFound
        if id:
            if len([x for x in self._spreadsheeets if x["id"] == id]) == 0:
                raise SpreadsheetNotFound
        try:
            if title and not id:
                id = [x["id"] for x in self._spreadsheeets if x["name"] == title][0]
        except IndexError:
            raise SpreadsheetNotFound

        self._execute_request(None, self.driveService.files().delete(fileId=id), False)
        self._spreadsheeets.remove([x for x in self._spreadsheeets if x["name"] == title][0])

    def export(self, spreadsheet_id, fformat):
        request = self.driveService.files().export(fileId=spreadsheet_id, mimeType=fformat.value.split(':')[0])
        import io
        fh = io.FileIO(spreadsheet_id+fformat.value.split(':')[1], 'wb')
        downloader = ghttp.MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

    def open(self, title):
        """Opens a spreadsheet, returning a :class:`~pygsheets.Spreadsheet` instance.

        :param title: A title of a spreadsheet.

        If there's more than one spreadsheet with same title the first one
        will be opened.

        :raises pygsheets.SpreadsheetNotFound: if no spreadsheet with
                                             specified `title` is found.

        >>> c = pygsheets.Client(auth=('user@example.com', 'qwertypassword'))
        >>> c.login()
        >>> c.open('My fancy spreadsheet')

        """
        try:
            ssheet_id = [x['id'] for x in self._spreadsheeets if x["name"] == title][0]
            return self.open_by_key(ssheet_id)
        except IndexError:
            self._fetch_sheets()
            try:
                return [Spreadsheet(self, id=x['id']) for x in self._spreadsheeets if x["name"] == title][0]
            except IndexError:
                raise SpreadsheetNotFound(title)

    def open_by_key(self, key, returnas='spreadsheet'):
        """Opens a spreadsheet specified by `key`, returning a :class:`~pygsheets.Spreadsheet` instance.

        :param key: A key of a spreadsheet as it appears in a URL in a browser.
        :param returnas: return as spreadhseet of json object
        :raises pygsheets.SpreadsheetNotFound: if no spreadsheet with
                                             specified `key` is found.

        >>> c = pygsheets.authorize()
        >>> c.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')

        """
        result = ''
        try:
            result = self.service.spreadsheets().get(spreadsheetId=key,
                                                     fields='properties,sheets/properties,spreadsheetId')\
                                                    .execute()
        except Exception as e:
            raise e
        if returnas == 'spreadsheet':
            return Spreadsheet(self, result)
        elif returnas == 'json':
            return result
        else:
            raise InvalidArgumentValue(returnas)

    def open_by_url(self, url):
        """Opens a spreadsheet specified by `url`,

        :param url: URL of a spreadsheet as it appears in a browser.

        :raises pygsheets.SpreadsheetNotFound: if no spreadsheet with
                                             specified `url` is found.
        :returns: a `~pygsheets.Spreadsheet` instance.

        >>> c = pygsheets.authorize()
        >>> c.open_by_url('https://docs.google.com/spreadsheet/ccc?key=0Bm...FE&hl')

        """
        m1 = _url_key_re_v1.search(url)
        if m1:
            return self.open_by_key(m1.group(1))

        else:
            m2 = _url_key_re_v2.search(url)
            if m2:
                return self.open_by_key(m2.group(1))

            else:
                raise NoValidUrlKeyFound

    def open_all(self, title=None):
        """
        Opens all available spreadsheets,

        :param title: (optional) If specified can be used to filter spreadsheets by title.

        :returns: list of a :class:`~pygsheets.Spreadsheet` instances
        """
        return [Spreadsheet(self, id=x['id']) for x in self._spreadsheeets if ((title is None) or (x['name'] == title))]

    def list_ssheets(self):
        return self._spreadsheeets

    def add_permission(self, file_id, addr, role='reader', is_group=False, expirationTime=None):
        """
        create/update permission for user/group/domain

        :param file_id: id of the file whose permissions to manupulate
        :param addr: this is the email for user/group and domain adress for domains
        :param role: permission to be applied
        :param expirationTime: (Not Implimented) time until this permission should last
        :param is_group: boolean , Is this addr a group; used only when email provided

        """
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addr):
            permission = {
                'type': 'user',
                'role': role,
                'emailAddress': addr
            }
            if is_group:
                permission['type'] = 'group'
        elif re.match('[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})*', addr):
            permission = {
                'type': 'domain',
                'role': role,
                'domain': addr
            }
        else:
            print ("invalid adress: %s" % addr)
            return False
        self.driveService.permissions().create(
            fileId=file_id,
            body=permission,
            fields='id',
        ).execute()

    def list_permissions(self, file_id):
        """
        list permissions of a file
        :param file_id: file id
        :returns:
        """
        request = self.driveService.permissions().list(fileId=file_id,
                                                       fields='permissions(domain,emailAddress,expirationTime,id,role,type)'
                                                       )
        return self._execute_request(file_id, request, False)

    def remove_permissions(self, file_id, addr, permisssions_in=None):
        """
        remove a users permission

        :param file_id: id of drive file
        :param addr: user email/domain name
        :param permisssions_in: permissions of the sheet if not provided its fetched

        :returns:
        """
        if not permisssions_in:
            permissions = self.list_permissions(file_id)['permissions']
        else:
            permissions = permisssions_in

        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addr):
            permission_id = [x['id'] for x in permissions if x['emailAddress'] == addr]
        elif re.match('[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})*', addr):
            permission_id = [x['id'] for x in permissions if x['domain'] == addr]
        else:
            raise InvalidArgumentValue
        if len(permission_id) == 0:
            # @TODO maybe raise an userInvalid exception
            raise InvalidUser
        result = self.driveService.permissions().delete(fileId=file_id, permissionId=permission_id[0]).execute()
        return result

    def get_range(self, spreadsheet_id, vrange, majordim='ROWS', value_render=ValueRenderOption.FORMATTED):
        """
         fetches  values from sheet.

        :param spreadsheet_id:  spreadsheet id
        :param vrange: range in A! format
        :param majordim: if the major dimension is rows or cols 'ROWS' or 'COLUMNS'
        :param value_render: format of output values

        :returns: 2d array
        """
        request = self.service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=vrange,
                                                           majorDimension=majordim, valueRenderOption=value_render.value,
                                                           dateTimeRenderOption=None)
        result = self._execute_request(spreadsheet_id, request, False)
        try:
            return result['values']
        except KeyError:
            return [['']]

    def update_sheet_properties(self, spreadsheet_id, propertyObj, fields_to_update=
                                'title,hidden,gridProperties,tabColor,rightToLeft', batch=False):
        """wrapper for updating sheet properties"""
        request = {"updateSheetProperties": {"properties": propertyObj, "fields": fields_to_update}}
        return self.sh_batch_update(spreadsheet_id, request, None, batch)

    def sh_update_range(self, spreadsheet_id, body, batch, parse=True):
        cformat = 'USER_ENTERED' if parse else 'RAW'
        final_request = self.service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=body['range'],
                                                                    valueInputOption=cformat, body=body)
        self._execute_request(spreadsheet_id, final_request, batch)

    def sh_batch_clear(self, spreadsheet_id, body, batch=False):
        """wrapper around batch clear"""
        final_request = self.service.spreadsheets().values().batchClear(spreadsheetId=spreadsheet_id, body=body)
        self._execute_request(spreadsheet_id, final_request, batch)

    def sh_batch_update(self, spreadsheet_id, request, fields=None, batch=False):
        body = {'requests': [request]}
        final_request = self.service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body,
                                                                fields=fields)
        return self._execute_request(spreadsheet_id, final_request, batch)

    def _execute_request(self, spreadsheet_id, request, batch):
        """Execute the request"""
        if batch:
            def callback(request_id, response, exception):
                if exception:
                    print(exception)
                else:
                    print("Batch operation completed")
            try:
                self.batch_requests[spreadsheet_id].add(request)
            except KeyError:
                self.batch_requests[spreadsheet_id] = self.service.new_batch_http_request(callback=callback)
                self.batch_requests[spreadsheet_id].add(request)
        else:
            for i in range(self.retries):
                try:
                    response = request.execute()
                except Exception as e:
                    # print ("Retry no "+str(i))
                    if not str(e).find('timed out') != -1 or i == self.retries-1:
                        raise e
                else:
                    return response

    # @TODO start new batch after 100 requests as per docs
    def send_batch(self, spreadsheet_id):
        """Send all batched requests"""
        self.batch_requests[spreadsheet_id].execute()
        del self.batch_requests[spreadsheet_id]


def get_outh_credentials(client_secret_file, application_name='PyGsheets', credential_dir=None):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    :param client_secret_file: path to outh2 client secret file
    :param application_name: name of application
    :param credential_dir: path to directory where tokens should be stored
                           'global' if you want to store in system-wide location
                           None if you want to store in current script directory
    :return
        Credentials, the obtained credential.
    """
    if credential_dir == 'global':
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
    elif not credential_dir:
        credential_dir = os.getcwd()
    else:
        pass

    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, SCOPES)
        flow.user_agent = application_name
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def authorize(outh_file='client_secret.json', outh_creds_store=None, service_file=None, credentials=None):
    """Login to Google API using OAuth2 credentials.

    This function instantiates :class:`Client` and performs auhtication.

    :param outh_file: path to outh2 credentials file
    :param outh_creds_store: path to directory where tokens should be stored
                           'global' if you want to store in system-wide location
                           None if you want to store in current script directory
    :param service_file: path to service credentials file
    :param credentials: outh2 credentials object

    :returns: :class:`Client` instance.

    """
    # @TODO handle exceptions
    if not credentials:
        if service_file:
            with open(service_file) as data_file:
                data = jload(data_file)
                print('service_email : '+str(data['client_email']))
            credentials = ServiceAccountCredentials.from_json_keyfile_name(service_file, SCOPES)
        elif outh_file:
            credentials = get_outh_credentials(client_secret_file=outh_file, credential_dir=outh_creds_store)
        else:
            raise AuthenticationError
    rclient = Client(auth=credentials)
    return rclient
