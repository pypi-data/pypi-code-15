# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

import pytest
import xlsxwriter

import pytablereader as ptr
from pytablereader.interface import TableLoader


@pytest.fixture
def valid_excel_file_path(tmpdir):
    test_file_path = tmpdir.join("tmp.xlsx")
    workbook = xlsxwriter.Workbook(str(test_file_path))

    worksheet = workbook.add_worksheet("testsheet1")
    table = [
        ["", "", "", ""],
        ["", "a1", "b1", "c1"],
        ["", "aa1", "ab1", "ac1"],
        ["", 1, 1.1, "a"],
        ["", 2, 2.2, "bb"],
        ["", 3, 3.3, "cc"],
    ]
    for row_idx, row in enumerate(table):
        for col_idx, item in enumerate(row):
            worksheet.write(row_idx, col_idx, item)

    worksheet = workbook.add_worksheet("testsheet2")

    worksheet = workbook.add_worksheet("testsheet3")
    table = [
        ["", "", ""],
        ["", "", ""],
        ["a3", "b3", "c3"],
        ["aa3", "ab3", "ac3"],
        [4, 1.1, "a"],
        [5, "", "bb"],
        [6, 3.3, ""],
    ]
    for row_idx, row in enumerate(table):
        for col_idx, item in enumerate(row):
            worksheet.write(row_idx, col_idx, item)

    worksheet = workbook.add_worksheet("invalid_sheet")
    table = [
        ["", "", "", ""],
        ["", "a", "", "c"],
        ["", "aa", "ab", ""],
        ["", "", 1.1, "a"],
    ]
    for row_idx, row in enumerate(table):
        for col_idx, item in enumerate(row):
            worksheet.write(row_idx, col_idx, item)

    workbook.close()

    return str(test_file_path)


@pytest.fixture
def invalid_excel_file_path(tmpdir):
    test_file_path = tmpdir.join("invalid.xlsx")
    workbook = xlsxwriter.Workbook(str(test_file_path))

    worksheet = workbook.add_worksheet("testsheet1")
    table = [
        ["", "", "", ""],
        ["", "a", "", "c"],
        ["", "aa", "ab", ""],
        ["", "", 1.1, "a"],
    ]
    for row_idx, row in enumerate(table):
        for col_idx, item in enumerate(row):
            worksheet.write(row_idx, col_idx, item)

    worksheet = workbook.add_worksheet("testsheet2")

    workbook.close()

    return str(test_file_path)


class Test_ExcelTableFileLoader_make_table_name:

    def setup_method(self, method):
        TableLoader.clear_table_count()

    @property
    def monkey_property(self):
        return "testsheet"

    @pytest.mark.parametrize(["value", "source", "expected"], [
        ["%(sheet)s", "/path/to/data.xlsx", "testsheet"],
        ["%(filename)s", "/path/to/data.xlsx", "data"],
        [
            "prefix_%(filename)s_%(sheet)s",
            "/path/to/data.xlsx",
            "prefix_data_testsheet"
        ],
        [
            "%(format_name)s%(format_id)s_%(filename)s",
            "/path/to/data.xlsx",
            "excel0_data"
        ],
    ])
    def test_normal(self, monkeypatch, value, source, expected):
        loader = ptr.ExcelTableFileLoader(source)
        loader.table_name = value

        monkeypatch.setattr(
            ptr.ExcelTableFileLoader, "_sheet_name", self.monkey_property)

        assert loader.make_table_name() == expected

    @pytest.mark.parametrize(["value", "source", "expected"], [
        [None, "/path/to/data.xlsx", ValueError],
        ["", "/path/to/data.xlsx", ValueError],
        ["%(sheet)s", None, ptr.InvalidTableNameError],
        ["%(sheet)s", "", ptr.InvalidTableNameError],
    ])
    def test_exception(self, value, source, expected):
        loader = ptr.ExcelTableFileLoader(source)
        loader.table_name = value

        with pytest.raises(expected):
            loader.make_table_name()


class Test_ExcelTableFileLoader_load:

    def setup_method(self, method):
        TableLoader.clear_table_count()

    @pytest.mark.parametrize(
        [
            "table_name",
            "start_row",
            "expected_tabledata",
        ],
        [
            [
                "%(sheet)s",
                0,
                [
                    ptr.data.TableData(
                        table_name=u'testsheet1',
                        header_list=[u'a1', u'b1', u'c1'],
                        record_list=[
                            [u'aa1', u'ab1', u'ac1'],
                            [1.0, 1.1, u'a'],
                            [2.0, 2.2, u'bb'],
                            [3.0, 3.3, u'cc'],
                        ]),
                    ptr.data.TableData(
                        table_name=u'testsheet3',
                        header_list=[u'a3', u'b3', u'c3'],
                        record_list=[
                            [u'aa3', u'ab3', u'ac3'],
                            [4.0, 1.1, u'a'],
                            [5.0, u'', u'bb'],
                            [6.0, 3.3, u''],
                        ]),
                ]
            ],
            [
                "%(filename)s_%(sheet)s",
                2,
                [
                    ptr.data.TableData(
                        table_name=u'tmp_testsheet1',
                        header_list=[u'aa1', u'ab1', u'ac1'],
                        record_list=[
                            [1.0, 1.1, u'a'],
                            [2.0, 2.2, u'bb'],
                            [3.0, 3.3, u'cc'],
                        ]),
                    ptr.data.TableData(
                        table_name=u'tmp_testsheet3',
                        header_list=[u'a3', u'b3', u'c3'],
                        record_list=[
                            [u'aa3', u'ab3', u'ac3'],
                            [4.0, 1.1, u'a'],
                            [5.0, u'', u'bb'],
                            [6.0, 3.3, u''],
                        ]),
                ]
            ],
        ])
    def test_normal(
            self, valid_excel_file_path,
            table_name, start_row, expected_tabledata):
        loader = ptr.ExcelTableFileLoader(valid_excel_file_path)
        loader.table_name = table_name
        loader.start_row = start_row

        for tabledata, expected in zip(loader.load(), expected_tabledata):
            assert tabledata == expected

    @pytest.mark.parametrize(
        [
            "table_name",
            "start_row",
            "expected",
        ],
        [
            [
                "%(sheet)s",
                0,
                ptr.InvalidDataError,
            ],
        ])
    def test_abnormal(
            self, invalid_excel_file_path, table_name, start_row, expected):
        loader = ptr.ExcelTableFileLoader(invalid_excel_file_path)
        loader.table_name = table_name
        loader.start_row = start_row

        for tabletuple in loader.load():
            assert tabletuple == []

    @pytest.mark.parametrize(
        [
            "source",
            "expected",
        ],
        [
            ["", IOError],
            [None, IOError],
        ])
    def test_null_file_path(self, source, expected):
        loader = ptr.ExcelTableFileLoader(source)

        with pytest.raises(expected):
            for _tabletuple in loader.load():
                pass

    @pytest.mark.parametrize(
        [
            "table_name",
            "expected",
        ],
        [
            ["", ValueError],
            [None, ValueError],
        ])
    def test_null_table_name(
            self, valid_excel_file_path, table_name, expected):
        loader = ptr.ExcelTableFileLoader(valid_excel_file_path)
        loader.table_name = table_name

        with pytest.raises(expected):
            for _tabletuple in loader.load():
                pass
