# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import logging

from copy import copy
from eve.utils import config

from superdesk.utc import utcnow
from superdesk.errors import SuperdeskApiError
from superdesk.services import BaseService
from superdesk.publish.formatters.ninjs_formatter import NINJSFormatter


logger = logging.getLogger('superdesk')


class PublishService(BaseService):
    """A service for publishing to the content api.

    Serves mainly as a proxy to the data layer.
    """

    formatter = NINJSFormatter()
    subscriber = {'config': {}}

    def publish(self, item, subscribers=[]):
        """Publish an item to content api.

        This must be enabled via ``PUBLISH_TO_CONTENT_API`` setting.

        :param item: item to publish
        """
        doc = self.formatter._transform_to_ninjs(item, self.subscriber)
        now = utcnow()
        doc.setdefault('firstcreated', now)
        doc.setdefault('versioncreated', now)
        doc['subscribers'] = [str(sub['_id']) for sub in subscribers]
        logger.info('publishing %s to %s' % (doc['guid'], subscribers))
        return self._create_doc(doc)

    def create(self, docs, **kwargs):
        ids = []
        for doc in docs:
            ids.extend(self._create_doc(doc, **kwargs))
        return ids

    def _create_doc(self, doc, **kwargs):
        """Create a new item or update existing."""
        item = copy(doc)
        item.setdefault('_id', item.get('guid'))
        _id = item[config.ID_FIELD] = item.pop('guid')
        original = self.find_one(req=None, _id=_id)
        self._process_associations(item)
        if original:
            self.update(_id, item, original)
            return _id
        else:
            return super().create([item], **kwargs)[0]

    def _process_associations(self, doc):
        if 'associations' in doc:
            for group, assoc in doc['associations'].items():
                if type(assoc) != dict:
                    msg = "Associations group %s has invalid value in list: '%s', should be dictionary" \
                        % (group, assoc)
                    raise SuperdeskApiError.badRequestError(msg)
                # if then association dictionary contains more than 2 items
                # (_id, type) then it's an embedded item
                if len(assoc) > 2:
                    self._create_doc(assoc)
                    for key in list(assoc):
                        if key != config.ID_FIELD and key != 'type':
                            del assoc[key]
