# Copyright (c) 2013-2014 OpenStack Foundation
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

from networking_odl.common import callback
from networking_odl.common import constants as odl_const
from networking_odl.ml2.mech_driver import OpenDaylightDriver
from networking_odl.tests import base

import mock
import testtools

from neutron.callbacks import events
from neutron.callbacks import resources


FAKE_ID = 'fakeid'


class ODLCallbackTestCase(testtools.TestCase):
    def setUp(self):
        self.useFixture(base.OpenDaylightRestClientFixture())
        super(ODLCallbackTestCase, self).setUp()
        self._precommit = mock.Mock()
        self._postcommit = mock.Mock()
        self.sgh = callback.OdlSecurityGroupsHandler(self._precommit,
                                                     self._postcommit)

    def _test_callback_precommit_for_sg(self, event, op, sg, sg_id):
        plugin_context_mock = mock.Mock()
        expected_dict = ({resources.SECURITY_GROUP: sg}
                         if sg is not None else None)
        self.sgh.sg_callback_precommit(resources.SECURITY_GROUP,
                                       event,
                                       None,
                                       context=plugin_context_mock,
                                       security_group=sg,
                                       security_group_id=sg_id)
        self._precommit.assert_called_with(
            plugin_context_mock, op,
            callback._RESOURCE_MAPPING[resources.SECURITY_GROUP], sg_id,
            expected_dict)

    def _test_callback_postcommit_for_sg(self, event, op, sg, sg_id):
        plugin_context_mock = mock.Mock()
        expected_dict = ({resources.SECURITY_GROUP: sg}
                         if sg is not None else None)
        self.sgh.sg_callback_postcommit(resources.SECURITY_GROUP,
                                        event,
                                        None,
                                        context=plugin_context_mock,
                                        security_group=sg,
                                        security_group_id=sg_id)

        self._postcommit.assert_called_with(
            plugin_context_mock, op,
            callback._RESOURCE_MAPPING[resources.SECURITY_GROUP], sg_id,
            expected_dict)

    def test_callback_precommit_sg_create(self):
        sg = mock.Mock()
        sg_id = sg.get('id')
        self._test_callback_precommit_for_sg(
            events.PRECOMMIT_CREATE, odl_const.ODL_CREATE, sg, sg_id)

    def test_callback_postcommit_sg_create(self):
        sg = mock.Mock()
        sg_id = sg.get('id')
        self._test_callback_postcommit_for_sg(
            events.AFTER_CREATE, odl_const.ODL_CREATE, sg, sg_id)

    def test_callback_precommit_sg_update(self):
        self._test_callback_precommit_for_sg(
            events.PRECOMMIT_UPDATE, odl_const.ODL_UPDATE, mock.Mock(),
            FAKE_ID)

    def test_callback_postcommit_sg_update(self):
        self._test_callback_postcommit_for_sg(
            events.AFTER_UPDATE, odl_const.ODL_UPDATE, mock.Mock(), FAKE_ID)

    def test_callback_precommit_sg_delete(self):
        self._test_callback_precommit_for_sg(
            events.PRECOMMIT_DELETE, odl_const.ODL_DELETE, None, FAKE_ID)

    def test_callback_postcommit_sg_delete(self):
        self._test_callback_postcommit_for_sg(
            events.AFTER_DELETE, odl_const.ODL_DELETE, None, FAKE_ID)

    @mock.patch.object(OpenDaylightDriver, 'sync_from_callback')
    def _test_callback_precommit_for_sg_rules(
            self, event, op, sg_rule, sg_rule_id, sfc):
        plugin_context_mock = mock.Mock()
        expected_dict = ({resources.SECURITY_GROUP_RULE: sg_rule}
                         if sg_rule is not None else None)
        self.sgh.sg_callback_precommit(resources.SECURITY_GROUP_RULE,
                                       event,
                                       None,
                                       context=plugin_context_mock,
                                       security_group_rule=sg_rule,
                                       security_group_rule_id=sg_rule_id)
        self._precommit.assert_called_with(
            plugin_context_mock, op,
            callback._RESOURCE_MAPPING[resources.SECURITY_GROUP_RULE],
            sg_rule_id, expected_dict)

    @mock.patch.object(OpenDaylightDriver, 'sync_from_callback')
    def _test_callback_postcommit_for_sg_rules(
            self, event, op, sg_rule, sg_rule_id, sfc):
        plugin_context_mock = mock.Mock()
        expected_dict = ({resources.SECURITY_GROUP_RULE: sg_rule}
                         if sg_rule is not None else None)
        self.sgh.sg_callback_postcommit(resources.SECURITY_GROUP_RULE,
                                        event,
                                        None,
                                        context=plugin_context_mock,
                                        security_group_rule=sg_rule,
                                        security_group_rule_id=sg_rule_id)

        self._postcommit.assert_called_with(
            plugin_context_mock, op,
            callback._RESOURCE_MAPPING[resources.SECURITY_GROUP_RULE],
            sg_rule_id, expected_dict)

    def test_callback_precommit_sg_rules_create(self):
        rule = mock.Mock()
        rule_id = rule.get('id')
        self._test_callback_precommit_for_sg_rules(
            events.PRECOMMIT_CREATE, odl_const.ODL_CREATE, rule, rule_id)

    def test_callback_postcommit_sg_rules_create(self):
        rule = mock.Mock()
        rule_id = rule.get('id')
        self._test_callback_postcommit_for_sg_rules(
            events.AFTER_CREATE, odl_const.ODL_CREATE, rule, rule_id)

    def test_callback_precommit_sg_rules_delete(self):
        self._test_callback_precommit_for_sg_rules(
            events.PRECOMMIT_DELETE, odl_const.ODL_DELETE, None, FAKE_ID)

    def test_callback_postcommit_sg_rules_delete(self):
        self._test_callback_postcommit_for_sg_rules(
            events.AFTER_DELETE, odl_const.ODL_DELETE, None, FAKE_ID)
