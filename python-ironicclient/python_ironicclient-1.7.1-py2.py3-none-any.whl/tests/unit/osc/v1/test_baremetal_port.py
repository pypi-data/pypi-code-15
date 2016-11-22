#
#   Copyright 2015 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import copy

import mock
from osc_lib.tests import utils as osctestutils
from osc_lib import utils as oscutils

from ironicclient import exc
from ironicclient.osc.v1 import baremetal_port
from ironicclient.tests.unit.osc.v1 import fakes as baremetal_fakes


class TestBaremetalPort(baremetal_fakes.TestBaremetal):

    def setUp(self):
        super(TestBaremetalPort, self).setUp()

        self.baremetal_mock = self.app.client_manager.baremetal
        self.baremetal_mock.reset_mock()


class TestCreateBaremetalPort(TestBaremetalPort):
    def setUp(self):
        super(TestCreateBaremetalPort, self).setUp()

        self.baremetal_mock.port.create.return_value = (
            baremetal_fakes.FakeBaremetalResource(
                None,
                copy.deepcopy(baremetal_fakes.BAREMETAL_PORT),
                loaded=True,
            ))

        # Get the command object to test
        self.cmd = baremetal_port.CreateBaremetalPort(self.app, None)

    def test_baremetal_port_create(self):
        arglist = [
            baremetal_fakes.baremetal_port_address,
            '--node', baremetal_fakes.baremetal_uuid,
        ]

        verifylist = [
            ('node_uuid', baremetal_fakes.baremetal_uuid),
            ('address', baremetal_fakes.baremetal_port_address),
        ]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        # DisplayCommandBase.take_action() returns two tuples
        self.cmd.take_action(parsed_args)

        # Set expected values
        args = {
            'address': baremetal_fakes.baremetal_port_address,
            'node_uuid': baremetal_fakes.baremetal_uuid,
        }

        self.baremetal_mock.port.create.assert_called_once_with(**args)

    def _test_baremetal_port_create_llc_warning(self, additional_args,
                                                additional_verify_items):
        arglist = [
            baremetal_fakes.baremetal_port_address,
            '--node', baremetal_fakes.baremetal_uuid,
        ]
        arglist.extend(additional_args)

        verifylist = [
            ('node_uuid', baremetal_fakes.baremetal_uuid),
            ('address', baremetal_fakes.baremetal_port_address),
        ]
        verifylist.extend(additional_verify_items)

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        self.cmd.log = mock.Mock()

        # DisplayCommandBase.take_action() returns two tuples
        columns, data = self.cmd.take_action(parsed_args)

        # Set expected values
        args = {
            'address': baremetal_fakes.baremetal_port_address,
            'node_uuid': baremetal_fakes.baremetal_uuid,
            'local_link_connection': {'switch_id': 'aa:bb:cc:dd:ee:ff',
                                      'port_id': 'eth0'}
        }

        self.baremetal_mock.port.create.assert_called_once_with(**args)
        self.cmd.log.warning.assert_called()

    def test_baremetal_port_create_llc_warning_some_deprecated(self):
        self._test_baremetal_port_create_llc_warning(
            additional_args=['-l', 'port_id=eth0', '--local-link-connection',
                             'switch_id=aa:bb:cc:dd:ee:ff'],
            additional_verify_items=[
                ('local_link_connection_deprecated', ['port_id=eth0']),
                ('local_link_connection', ['switch_id=aa:bb:cc:dd:ee:ff'])]
        )

    def test_baremetal_port_create_llc_warning_all_deprecated(self):
        self._test_baremetal_port_create_llc_warning(
            additional_args=['-l', 'port_id=eth0', '-l',
                             'switch_id=aa:bb:cc:dd:ee:ff'],
            additional_verify_items=[('local_link_connection_deprecated',
                                      ['port_id=eth0',
                                       'switch_id=aa:bb:cc:dd:ee:ff'])]
        )


class TestShowBaremetalPort(TestBaremetalPort):
    def setUp(self):
        super(TestShowBaremetalPort, self).setUp()

        self.baremetal_mock.port.get.return_value = (
            baremetal_fakes.FakeBaremetalResource(
                None,
                copy.deepcopy(baremetal_fakes.BAREMETAL_PORT),
                loaded=True))

        self.baremetal_mock.port.get_by_address.return_value = (
            baremetal_fakes.FakeBaremetalResource(
                None,
                copy.deepcopy(baremetal_fakes.BAREMETAL_PORT),
                loaded=True))

        self.cmd = baremetal_port.ShowBaremetalPort(self.app, None)

    def test_baremetal_port_show(self):
        arglist = ['zzz-zzzzzz-zzzz']
        verifylist = [('port', baremetal_fakes.baremetal_port_uuid)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        columns, data = self.cmd.take_action(parsed_args)

        # Set expected values
        args = ['zzz-zzzzzz-zzzz']
        self.baremetal_mock.port.get.assert_called_with(*args, fields=None)

        collist = (
            'address',
            'extra',
            'node_uuid',
            'uuid')
        self.assertEqual(collist, columns)

        datalist = (
            baremetal_fakes.baremetal_port_address,
            baremetal_fakes.baremetal_port_extra,
            baremetal_fakes.baremetal_uuid,
            baremetal_fakes.baremetal_port_uuid)
        self.assertEqual(datalist, tuple(data))

    def test_baremetal_port_show_address(self):

        arglist = ['--address', baremetal_fakes.baremetal_port_address]
        verifylist = [('address', True)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        self.cmd.take_action(parsed_args)

        args = {'AA:BB:CC:DD:EE:FF'}
        self.baremetal_mock.port.get_by_address.assert_called_with(
            *args, fields=None)

    def test_baremetal_port_show_no_port(self):
        arglist = []
        verifylist = []

        self.assertRaises(osctestutils.ParserException,
                          self.check_parser,
                          self.cmd, arglist, verifylist)


class TestBaremetalPortUnset(TestBaremetalPort):
    def setUp(self):
        super(TestBaremetalPortUnset, self).setUp()

        self.baremetal_mock.port.update.return_value = (
            baremetal_fakes.FakeBaremetalResource(
                None,
                copy.deepcopy(baremetal_fakes.BAREMETAL_PORT),
                loaded=True))

        self.cmd = baremetal_port.UnsetBaremetalPort(self.app, None)

    def test_baremetal_port_unset_no_options(self):
        arglist = []
        verifylist = []
        self.assertRaises(osctestutils.ParserException,
                          self.check_parser,
                          self.cmd, arglist, verifylist)

    def test_baremetal_port_unset_extra(self):
        arglist = ['port', '--extra', 'foo']
        verifylist = [('port', 'port'),
                      ('extra', ['foo'])]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        self.cmd.take_action(parsed_args)
        self.baremetal_mock.port.update.assert_called_once_with(
            'port',
            [{'path': '/extra/foo', 'op': 'remove'}])

    def test_baremetal_port_unset_multiple_extras(self):
        arglist = ['port',
                   '--extra', 'foo',
                   '--extra', 'bar']
        verifylist = [('port', 'port'),
                      ('extra', ['foo', 'bar'])]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        self.cmd.take_action(parsed_args)
        self.baremetal_mock.port.update.assert_called_once_with(
            'port',
            [{'path': '/extra/foo', 'op': 'remove'},
             {'path': '/extra/bar', 'op': 'remove'}])


class TestBaremetalPortSet(TestBaremetalPort):
    def setUp(self):
        super(TestBaremetalPortSet, self).setUp()

        self.baremetal_mock.port.update.return_value = (
            baremetal_fakes.FakeBaremetalResource(
                None,
                copy.deepcopy(baremetal_fakes.BAREMETAL_PORT),
                loaded=True))

        self.cmd = baremetal_port.SetBaremetalPort(self.app, None)

    def test_baremetal_port_set_node_uuid(self):
        new_node_uuid = '1111-111111-1111'
        arglist = [
            baremetal_fakes.baremetal_port_uuid,
            '--node', new_node_uuid]
        verifylist = [
            ('port', baremetal_fakes.baremetal_port_uuid),
            ('node_uuid', new_node_uuid)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        self.cmd.take_action(parsed_args)
        self.baremetal_mock.port.update.assert_called_once_with(
            baremetal_fakes.baremetal_port_uuid,
            [{'path': '/node_uuid', 'value': new_node_uuid, 'op': 'add'}])

    def test_baremetal_port_set_address(self):
        arglist = [
            baremetal_fakes.baremetal_port_uuid,
            '--address', baremetal_fakes.baremetal_port_address]
        verifylist = [
            ('port', baremetal_fakes.baremetal_port_uuid),
            ('address', baremetal_fakes.baremetal_port_address)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        self.cmd.take_action(parsed_args)
        self.baremetal_mock.port.update.assert_called_once_with(
            baremetal_fakes.baremetal_port_uuid,
            [{'path': '/address',
              'value': baremetal_fakes.baremetal_port_address,
              'op': 'add'}])

    def test_baremetal_set_extra(self):
        arglist = ['port', '--extra', 'foo=bar']
        verifylist = [('port', 'port'),
                      ('extra', ['foo=bar'])]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        self.cmd.take_action(parsed_args)
        self.baremetal_mock.port.update.assert_called_once_with(
            'port',
            [{'path': '/extra/foo', 'value': 'bar', 'op': 'add'}])

    def test_baremetal_port_set_no_options(self):
        arglist = []
        verifylist = []
        self.assertRaises(osctestutils.ParserException,
                          self.check_parser,
                          self.cmd, arglist, verifylist)


class TestBaremetalPortDelete(TestBaremetalPort):
    def setUp(self):
        super(TestBaremetalPortDelete, self).setUp()

        self.baremetal_mock.port.get.return_value = (
            baremetal_fakes.FakeBaremetalResource(
                None,
                copy.deepcopy(baremetal_fakes.BAREMETAL_PORT),
                loaded=True))

        self.cmd = baremetal_port.DeleteBaremetalPort(self.app, None)

    def test_baremetal_port_delete(self):
        arglist = ['zzz-zzzzzz-zzzz']
        verifylist = []

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        self.cmd.take_action(parsed_args)

        args = 'zzz-zzzzzz-zzzz'
        self.baremetal_mock.port.delete.assert_called_with(args)

    def test_baremetal_port_delete_multiple(self):
        arglist = ['zzz-zzzzzz-zzzz', 'fakename']
        verifylist = []

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        self.cmd.take_action(parsed_args)

        args = ['zzz-zzzzzz-zzzz', 'fakename']
        self.baremetal_mock.port.delete.has_calls(
            [mock.call(x) for x in args])
        self.assertEqual(2, self.baremetal_mock.port.delete.call_count)

    def test_baremetal_port_delete_multiple_with_fail(self):
        arglist = ['zzz-zzzzzz-zzzz', 'badname']
        verifylist = []

        self.baremetal_mock.port.delete.side_effect = ['', exc.ClientException]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        self.assertRaises(exc.ClientException,
                          self.cmd.take_action,
                          parsed_args)

        args = ['zzz-zzzzzz-zzzz', 'badname']
        self.baremetal_mock.port.delete.has_calls(
            [mock.call(x) for x in args])
        self.assertEqual(2, self.baremetal_mock.port.delete.call_count)

    def test_baremetal_port_delete_no_port(self):
        arglist = []
        verifylist = []

        self.assertRaises(osctestutils.ParserException,
                          self.check_parser,
                          self.cmd, arglist, verifylist)


class TestBaremetalPortList(TestBaremetalPort):
    def setUp(self):
        super(TestBaremetalPortList, self).setUp()

        self.baremetal_mock.port.list.return_value = [
            baremetal_fakes.FakeBaremetalResource(
                None,
                copy.deepcopy(baremetal_fakes.BAREMETAL_PORT),
                loaded=True)
        ]

        self.cmd = baremetal_port.ListBaremetalPort(self.app, None)

    def test_baremetal_port_list(self):
        arglist = []
        verifylist = []

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        columns, data = self.cmd.take_action(parsed_args)

        kwargs = {
            'marker': None,
            'limit': None}
        self.baremetal_mock.port.list.assert_called_with(**kwargs)

        collist = (
            "UUID",
            "Address")
        self.assertEqual(collist, columns)

        datalist = ((
            baremetal_fakes.baremetal_port_uuid,
            baremetal_fakes.baremetal_port_address
        ), )
        self.assertEqual(datalist, tuple(data))

    def test_baremetal_port_list_address(self):
        arglist = ['--address', baremetal_fakes.baremetal_port_address]
        verifylist = [('address', baremetal_fakes.baremetal_port_address)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        columns, data = self.cmd.take_action(parsed_args)

        kwargs = {
            'address': baremetal_fakes.baremetal_port_address,
            'marker': None,
            'limit': None,
        }
        self.baremetal_mock.port.list.assert_called_with(**kwargs)

    def test_baremetal_port_list_node(self):
        arglist = ['--node', baremetal_fakes.baremetal_uuid]
        verifylist = [('node', baremetal_fakes.baremetal_uuid)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        columns, data = self.cmd.take_action(parsed_args)

        kwargs = {
            'node': baremetal_fakes.baremetal_uuid,
            'marker': None,
            'limit': None,
        }
        self.baremetal_mock.port.list.assert_called_with(**kwargs)

    def test_baremetal_port_list_long(self):
        arglist = ['--long']
        verifylist = [('detail', True)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        columns, data = self.cmd.take_action(parsed_args)

        kwargs = {
            'detail': True,
            'marker': None,
            'limit': None,
        }
        self.baremetal_mock.port.list.assert_called_with(**kwargs)

        collist = ('UUID', 'Address', 'Created At', 'Extra', 'Node UUID',
                   'Local Link Connection', 'PXE boot enabled', 'Updated At',
                   'Internal Info')
        self.assertEqual(collist, columns)

        datalist = ((
            baremetal_fakes.baremetal_port_uuid,
            baremetal_fakes.baremetal_port_address,
            '',
            oscutils.format_dict(baremetal_fakes.baremetal_port_extra),
            baremetal_fakes.baremetal_uuid,
            '',
            '',
            '',
            ''
        ), )
        self.assertEqual(datalist, tuple(data))

    def test_baremetal_port_list_fields(self):
        arglist = ['--fields', 'uuid', 'address']
        verifylist = [('fields', [['uuid', 'address']])]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        self.cmd.take_action(parsed_args)

        kwargs = {
            'marker': None,
            'limit': None,
            'detail': False,
            'fields': ('uuid', 'address')
        }
        self.baremetal_mock.port.list.assert_called_with(**kwargs)

    def test_baremetal_port_list_fields_multiple(self):
        arglist = ['--fields', 'uuid', 'address', '--fields', 'extra']
        verifylist = [('fields', [['uuid', 'address'], ['extra']])]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        self.cmd.take_action(parsed_args)

        kwargs = {
            'marker': None,
            'limit': None,
            'detail': False,
            'fields': ('uuid', 'address', 'extra')
        }
        self.baremetal_mock.port.list.assert_called_with(**kwargs)

    def test_baremetal_port_list_invalid_fields(self):
        arglist = ['--fields', 'uuid', 'invalid']
        verifylist = [('fields', [['uuid', 'invalid']])]
        self.assertRaises(osctestutils.ParserException,
                          self.check_parser,
                          self.cmd, arglist, verifylist)
