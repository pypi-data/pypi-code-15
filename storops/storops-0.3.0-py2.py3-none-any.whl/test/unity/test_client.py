# coding=utf-8
# Copyright (c) 2015 EMC Corporation.
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

from __future__ import unicode_literals

import unittest
from time import sleep

from hamcrest import assert_that, equal_to, only_contains, none, any_of, \
    contains_string, raises, has_items, greater_than, less_than

from storops.unity.client import UnityClient, UnityDoc, MetricCounterRecords, \
    UnityPerfManager
from storops.unity.enums import RaidTypeEnum, HealthEnum, RaidTypeEnumList, \
    ServiceLevelEnum, ServiceLevelEnumList
from storops.unity.resource.disk import UnityDisk, UnityDiskList
from storops.unity.resource.lun import UnityLun, UnityLunList
from test.unity.rest_mock import patch_rest, t_rest

__author__ = 'Cedric Zhuang'


class UnityClientTest(unittest.TestCase):
    def test_assemble_url_no_compact(self):
        url = UnityClient.assemble_url('api/types', filter='a eq 100')
        assert_that(url, equal_to('/api/types?compact=True&filter=a eq 100'))

    def test_assemble_url_none_filter(self):
        url = UnityClient.assemble_url('api/types', filter=None)
        assert_that(url, equal_to('/api/types?compact=True'))

    @patch_rest
    def test_get_fields(self):
        fields = t_rest().get_fields('metric')
        assert_that(fields, only_contains(
            'id', 'name', 'path', 'product', 'type', 'objectType',
            'description', 'isHistoricalAvailable', 'isRealtimeAvailable',
            'unitDisplayString', 'unit', 'metricGroupName', 'visibility'))

    @patch_rest(output='abc.json')
    def test_mock_file_not_found(self):
        def f():
            t_rest().get_fields('abc')

        assert_that(f, raises(IOError))

    @patch_rest
    def test_make_body_complex(self):
        service_levels = [ServiceLevelEnum.BASIC, ServiceLevelEnum.BRONZE]
        param = {
            'a': 1,
            'b': UnityLun(_id='lun1'),
            'c': UnityLunList(cli=t_rest()),
            'd': [UnityLun(_id='lun10'), UnityLun(_id='lun11'), 0.1],
            'e': {'f': UnityLun(_id='lun12')},
            'g': 'string',
            'h': 0.2,
            'i': service_levels,
            'j': ServiceLevelEnumList.parse(service_levels)
        }
        ret = UnityClient.make_body(param)
        expected = {'a': 1,
                    'b': {'id': 'lun1'},
                    'c': [{'id': 'sv_2'}, {'id': 'sv_3'},
                          {'id': 'sv_5'}, {'id': 'sv_6'},
                          {'id': 'sv_7'}],
                    'd': [{'id': 'lun10'}, {'id': 'lun11'}, 0.1],
                    'e': {'f': {'id': 'lun12'}},
                    'g': 'string', 'h': 0.2, 'i': [0, 1], 'j': [0, 1]}
        assert_that(ret, equal_to(expected))

    @patch_rest
    def test_make_body_blank(self):
        param = {'fastVPParameters': {
            'tieringPolicy': None
        }}
        ret = UnityClient.make_body(param)
        expected = {}
        assert_that(ret, equal_to(expected))

    def test_make_body_nested_empty_dict(self):
        param = {
            'name': 'abc',
            'replicationParameters': {
                'isReplicationDestination': None,
            }
        }
        ret = UnityClient.make_body(param)
        assert_that(ret, equal_to({'name': 'abc'}))

    def test_make_body_no_change(self):
        ret = UnityClient.make_body(True)
        assert_that(ret, equal_to(True))

        ret = UnityClient.make_body('string')
        assert_that(ret, equal_to('string'))

    def test_make_body_resource(self):
        ret = UnityClient.make_body(UnityLun(_id='abc'))
        assert_that(ret, equal_to({'id': 'abc'}))

    def test_make_body_None(self):
        ret = UnityClient.make_body({'a': None})
        assert_that(ret, equal_to({}))

    def test_make_body_enum(self):
        ret = UnityClient.make_body({'a': RaidTypeEnum.RAID5})
        assert_that(ret, equal_to({'a': 1}))

    def test_make_body_kwargs(self):
        ret = UnityClient.make_body(a=1, b='c')
        assert_that(ret, equal_to({'a': 1, 'b': 'c'}))

    def test_make_body_zero(self):
        ret = UnityClient.make_body(a=0, b='')
        assert_that(ret, equal_to({'a': 0, 'b': ''}))

    def test_make_body_empty_collection(self):
        ret = UnityClient.make_body(allow_empty=True, b=(), c=[])
        assert_that(ret, equal_to({'b': [], 'c': []}))

    def test_make_body_nested_empty_collection(self):
        ret = UnityClient.make_body(allow_empty=True, b=(), c={'d': []})
        assert_that(ret, equal_to({'b': [], 'c': {'d': []}}))

    def test_make_body_empty_dict(self):
        inner = UnityClient.make_body(a=None)
        outer = UnityClient.make_body(b=inner, c=3)
        assert_that(outer, equal_to({'c': 3}))

    def test_dict_to_filter_string_normal(self):
        ret = UnityClient.dict_to_filter_string({'a': 1, 'b': 'c'})
        assert_that(ret, equal_to('a eq 1 and b eq "c"'))

    def test_dict_to_filter_unity_resource(self):
        ret = UnityClient.dict_to_filter_string(
            {'c': 1, 'b': UnityLun(_id='lun_1')})
        assert_that(ret, equal_to('b eq "lun_1" and c eq 1'))

    def test_dict_to_filter_list(self):
        ret = UnityClient.dict_to_filter_string({'a': [2, 4]})
        assert_that(ret, any_of('a eq 2 or a eq 4', 'a eq 4 or a eq 2'))
        ret = UnityClient.dict_to_filter_string({'a': ["m", "n"]})
        assert_that(ret, any_of('a eq "m" or a eq "n"',
                                'a eq "n" or a eq "m"'))

    def test_dict_to_filter_string_enum_list(self):
        levels = [ServiceLevelEnum.SILVER, ServiceLevelEnum.PLATINUM]
        ret = UnityClient.dict_to_filter_string({'a': levels})
        assert_that(ret, any_of('a eq 2 or a eq 4', 'a eq 4 or a eq 2'))

    def test_dict_to_filter_string_value_none(self):
        ret = UnityClient.dict_to_filter_string({'a': None, 'b': 'c'})
        assert_that(ret, equal_to('b eq "c"'))

    def test_dict_to_filter_string_value_all_none(self):
        ret = UnityClient.dict_to_filter_string({'a': None, 'b': None})
        assert_that(ret, none())

    def test_dict_to_filter_string_empty(self):
        ret = UnityClient.dict_to_filter_string({})
        assert_that(ret, none())
        ret = UnityClient.dict_to_filter_string(None)
        assert_that(ret, none())


class UnityPerfManagerTest(unittest.TestCase):
    def perf_mon(self):
        return UnityPerfManager()

    def test_enable_perf_metric(self):
        cli = self.perf_mon()
        assert_that(cli.is_perf_metric_enabled(), equal_to(False))
        cli.enable_perf_metric(0, lambda: 1)
        assert_that(cli.is_perf_metric_enabled(), equal_to(True))
        cli.disable_perf_metric()
        assert_that(cli.is_perf_metric_enabled(), equal_to(False))

    def test_double_enable(self):
        cli = self.perf_mon()
        c = []
        cli.enable_perf_metric(0.1, lambda: c.append(1))
        sleep(0.5)
        assert_that(len(c), greater_than(1))
        assert_that(len(c), less_than(8))
        cli.enable_perf_metric(10, lambda: c.append(1))
        sleep(0.5)
        assert_that(len(c), less_than(10))
        cli.disable_perf_metric()
        assert_that(cli.prev_counter, none())
        assert_that(cli.curr_counter, none())
        assert_that(cli.is_perf_metric_enabled(), equal_to(False))

    def test_is_perf_metric_enabled_rsc_default(self):
        cli = self.perf_mon()
        cli.enable_perf_metric(0, lambda: 1)
        enabled = cli.is_perf_metric_enabled(UnityDiskList(cli=cli))
        assert_that(enabled, equal_to(True))
        enabled = cli.is_perf_metric_enabled(UnityDisk(_id='', cli=cli))
        assert_that(enabled, equal_to(True))

    def test_is_perf_metric_enabled_rsc_specific(self):
        cli = self.perf_mon()
        cli.enable_perf_metric(0, lambda: 1, [UnityDisk])
        enabled = cli.is_perf_metric_enabled(UnityDiskList(cli=cli))
        assert_that(enabled, equal_to(True))

        enabled = cli.is_perf_metric_enabled(UnityLunList(cli=cli))
        assert_that(enabled, equal_to(False))

        enabled = cli.is_perf_metric_enabled(UnityDisk(_id='', cli=cli))
        assert_that(enabled, equal_to(True))

        enabled = cli.is_perf_metric_enabled(UnityLun(_id='', cli=cli))
        assert_that(enabled, equal_to(False))

    def test_is_perf_monitored_default(self):
        assert_that(self.perf_mon()._is_perf_monitored('abc'), equal_to(True))

    def test_is_perf_monitored_resource(self):
        cli = self.perf_mon()
        cli._perf_rsc_clz_list = [UnityDisk]
        assert_that(cli._is_perf_monitored(UnityDisk('', cli=cli)),
                    equal_to(True))
        assert_that(cli._is_perf_monitored(UnityLun('', cli=cli)),
                    equal_to(False))

    def test_is_perf_monitored_resource_list(self):
        cli = self.perf_mon()
        cli._perf_rsc_clz_list = [UnityDisk]
        assert_that(cli._is_perf_monitored(UnityDiskList(cli=cli)),
                    equal_to(True))
        assert_that(cli._is_perf_monitored(UnityLunList(cli=cli)),
                    equal_to(False))


class UnityDocTest(unittest.TestCase):
    @patch_rest
    def test_get_doc_of_field(self):
        unity_doc = UnityDoc(t_rest(), UnityLun)
        doc = unity_doc._get_doc(field='name')
        assert_that(doc, equal_to('Readable name'))

    @patch_rest
    def test_get_doc_of_resource(self):
        unity_doc = UnityDoc(t_rest(), UnityLun)
        doc = unity_doc._get_doc()
        assert_that(doc, contains_string('Represents Volume'))

    @patch_rest
    def test_get_doc_of_index(self):
        unity_doc = UnityDoc(t_rest(), HealthEnum)
        doc = unity_doc._get_doc(value=5)
        assert_that(doc, equal_to('OK'))

    @patch_rest
    def test_get_doc_enum_list(self):
        unity_doc = UnityDoc(t_rest(), RaidTypeEnumList)
        doc = unity_doc.doc
        assert_that(doc, contains_string('RAID5 has the only'))

    @patch_rest
    def test_get_doc_unity_resource_list(self):
        unity_doc = UnityDoc(t_rest(), UnityLunList)
        doc = unity_doc.doc
        assert_that(doc, contains_string('Represents Volume'))
        assert_that(doc, contains_string('current_node'))
        assert_that(doc, contains_string('Current SP'))

    def test_get_fmt_str(self):
        assert_that(UnityDoc.get_fmt_str((3, 5, 2)), equal_to('{:5}{:7}{:4}'))

    def test_get_column_max_len_str(self):
        data = [('but', '', 'd'), ('of', 'hand', 'i')]
        assert_that(UnityDoc.get_column_max_len(data), equal_to([3, 4, 1]))

    def test_get_column_max_len_int(self):
        data = [(1, 'd'), (11, 'd')]
        assert_that(UnityDoc.get_column_max_len(data), equal_to([2, 1]))

    def test_format_prop_no_header(self):
        props = [('a', 'b'), ('cc', 'dd')]
        assert_that(UnityDoc.format_prop(props), equal_to(['a   b', 'cc  dd']))

    def test_format_prop_with_header(self):
        props = [('a', 'b')]
        assert_that(UnityDoc.format_prop(props, header=('name', 'value')),
                    equal_to(['name  value', 'a     b']))


class UnityMetricCounterRecordsTest(unittest.TestCase):
    def test_max_count(self):
        records = MetricCounterRecords()
        records.add_results(1)
        records.add_results(2)
        records.add_results(3)
        assert_that(len(records), equal_to(2))
        assert_that(records._records, has_items(2, 3))
        assert_that(records.enabled, equal_to(True))

    def test_default_enabled(self):
        records = MetricCounterRecords()
        assert_that(records.enabled, equal_to(False))

    def test_reset(self):
        records = MetricCounterRecords()
        records.add_results(1)
        records.reset()
        assert_that(len(records), equal_to(0))
        assert_that(records.enabled, equal_to(False))

    def test_add_none_result(self):
        records = MetricCounterRecords()
        records.add_results(None)
        assert_that(len(records), equal_to(0))

    def test_curr_prev_value(self):
        records = MetricCounterRecords()
        assert_that(records.curr, none())
        assert_that(records.prev, none())

        records.add_results(1)
        assert_that(records.curr, equal_to(1))
        assert_that(records.prev, none())

        records.add_results(2)
        assert_that(records.curr, equal_to(2))
        assert_that(records.prev, equal_to(1))

        records.add_results(3)
        assert_that(records.curr, equal_to(3))
        assert_that(records.prev, equal_to(2))

        records.enabled = False
        assert_that(records.curr, none())
        assert_that(records.prev, none())
