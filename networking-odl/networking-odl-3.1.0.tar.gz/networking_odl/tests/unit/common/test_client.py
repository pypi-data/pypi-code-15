# Copyright (c) 2015 Intel Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from networking_odl.common import client

from neutron.tests import base


class ClientTestCase(base.DietTestCase):
    def setUp(self):
        cfg.CONF.set_override('mechanism_drivers',
                              ['logger', 'opendaylight_v2'],
                              'ml2')
        super(ClientTestCase, self).setUp()

    def _set_config(self, url='http://127.0.0.1:9999', username='someuser',
                    password='somepass'):
        cfg.CONF.set_override('url', url, 'ml2_odl')
        cfg.CONF.set_override('username', username, 'ml2_odl')
        cfg.CONF.set_override('password', password, 'ml2_odl')

    def _test_missing_config(self, **kwargs):
        self._set_config(**kwargs)
        self.assertRaisesRegex(cfg.RequiredOptError,
                               'value required for option \w+ in group '
                               '\[ml2_odl\]',
                               client.OpenDaylightRestClient._check_opt,
                               cfg.CONF.ml2_odl.url)

    def test_valid_config(self):
        self._set_config()
        client.OpenDaylightRestClient._check_opt(cfg.CONF.ml2_odl.url)

    def test_missing_url_raises_exception(self):
        self._test_missing_config(url=None)

    def test_missing_username_raises_exception(self):
        self._test_missing_config(username=None)

    def test_missing_password_raises_exception(self):
        self._test_missing_config(password=None)
