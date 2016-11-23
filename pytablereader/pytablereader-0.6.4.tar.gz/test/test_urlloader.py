# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
from __future__ import print_function
import os.path

import pytest
import responses

import pytablereader as ptr
from pytablereader.interface import TableLoader


class Test_TableUrlLoader_constructor:

    @responses.activate
    @pytest.mark.parametrize(["value", "format_name", "expected"], [
        [
            "https://raw.githubusercontent.com/valid/test/data/validext.csv",
            None, ptr.CsvTableTextLoader
        ],
        [
            "https://raw.githubusercontent.com/valid/test/data/validext.csv/",
            None, ptr.CsvTableTextLoader
        ],
        [
            "https://raw.githubusercontent.com/valid/test/data/validext.xlsx",
            None, ptr.ExcelTableFileLoader
        ],
        [
            "https://raw.githubusercontent.com/valid/test/data/validext.html",
            None, ptr.HtmlTableTextLoader
        ],
        [
            "https://raw.githubusercontent.com/valid/test/data/validext.htm/",
            None, ptr.HtmlTableTextLoader
        ],
        [
            "https://raw.githubusercontent.com/valid/test/data/validext.asp",
            None, ptr.HtmlTableTextLoader
        ],
        [
            "https://raw.githubusercontent.com/valid/test/data/validext.aspx/",
            None, ptr.HtmlTableTextLoader
        ],
        [
            "https://raw.githubusercontent.com/valid/test/data/validext.json",
            None, ptr.JsonTableTextLoader
        ],
        [
            "https://github.com/validext.md",
            None, ptr.MarkdownTableTextLoader
        ],
        ["https://github.com/validext.txt", "csv", ptr.CsvTableTextLoader],
        ["https://github.com/validext.txt", "html", ptr.HtmlTableTextLoader],
        ["https://github.com/validext.txt", "json", ptr.JsonTableTextLoader],
        [
            "https://github.com/invalidext.txt",
            "markdown", ptr.MarkdownTableTextLoader
        ],
        [
            "https://github.com/invalidext.txt",
            "mediawiki", ptr.MediaWikiTableTextLoader
        ],
    ])
    def test_normal(self, value, format_name, expected):
        responses.add(
            responses.GET,
            value,
            body='''{}''',
            content_type='text/plain; charset=utf-8',
            status=200
        )

        loader = ptr.TableUrlLoader(value, format_name)
        expected_loader = expected("")

        assert loader.source_type == expected_loader.source_type
        assert loader.format_name == expected_loader.format_name

    @responses.activate
    @pytest.mark.parametrize(["value", "format_name", "expected"], [
        [None, None, ptr.InvalidUrlError],
        ["", None, ptr.InvalidUrlError],
        ["https://github.com/", None, ptr.InvalidUrlError],
        ["/tmp/test.txt", None, ptr.InvalidUrlError],
        ["c:\\tmp\test.txt", None, ptr.InvalidUrlError],
        [
            "https://raw.githubusercontent.com/invalid/test/data/invalidext.txt",
            None, ptr.LoaderNotFoundError
        ],
        [
            "https://raw.githubusercontent.com/invalid/test/data/notexist.json",
            None, ptr.HTTPError
        ],
        [
            "https://raw.githubusercontent.com/invalid/test/data/invalidext.txt",
            "invalidformat", ptr.LoaderNotFoundError
        ],
    ])
    def test_exception(self, value, format_name, expected):
        responses.add(
            responses.GET,
            value,
            body='''404: Not Found''',
            status=404,
        )

        with pytest.raises(expected):
            ptr.TableUrlLoader(value, format_name)


class Test_TableUrlLoader_load:

    def setup_method(self, method):
        TableLoader.clear_table_count()

    @responses.activate
    @pytest.mark.parametrize(["url", "format_name"], [
        [
            'https://raw.githubusercontent.com/valid/test/data/validdata.csv',
            None,
        ],
        [
            'https://raw.githubusercontent.com/valid/test/data/validdata.txt',
            "csv",
        ],
    ])
    def test_normal_csv(self, url, format_name):
        responses.add(
            responses.GET,
            url,
            body='''"attr_a","attr_b","attr_c"
    1,4,"a"
    2,2.1,"bb"
    3,120.9,"ccc"''',
            content_type='text/plain; charset=utf-8',
            status=200
        )

        expeced_list = [
            ptr.TableData(
                "csv1",
                ["attr_a", "attr_b", "attr_c"],
                [
                    [1, 4,      "a"],
                    [2, "2.1",    "bb"],
                    [3, "120.9",  "ccc"],
                ])
        ]

        loader = ptr.TableUrlLoader(url, format_name)

        assert loader.format_name == "csv"

        for tabledata, expected in zip(loader.load(), expeced_list):
            print(tabledata.dumps())
            print(expected.dumps())
            assert tabledata == expected

    @responses.activate
    @pytest.mark.parametrize(["url", "format_name"], [
        [
            'https://raw.githubusercontent.com/valid/test/data/validdata.json',
            None,
        ],
        [
            'https://raw.githubusercontent.com/valid/test/data/validdata.txt',
            "json",
        ],
    ])
    def test_normal_json(self, url, format_name):
        responses.add(
            responses.GET,
            url,
            body='''[
        {"attr_a": 1},
        {"attr_b": 2.1, "attr_c": "bb"}
    ]''',
            content_type='text/plain; charset=utf-8',
            status=200
        )

        expeced_list = [
            ptr.TableData(
                "json1",
                ["attr_a", "attr_b", "attr_c"],
                [
                    {u'attr_a': 1},
                    {u'attr_b': 2.1, u'attr_c': u'bb'},
                ]
            )
        ]

        loader = ptr.TableUrlLoader(url, format_name)

        assert loader.format_name == "json"

        for tabledata, expected in zip(loader.load(), expeced_list):
            assert tabledata == expected

    @responses.activate
    def test_normal_excel(self):
        url = 'https://github.com/thombashi/valid/test/data/validdata.xlsx'

        data_path = os.path.join(
            os.path.dirname(__file__), "data/validdata.xlsx")
        print(data_path)
        with open(data_path, "rb") as f:
            responses.add(
                responses.GET,
                url,
                body=f.read(),
                content_type='application/octet-stream',
                status=200
            )

        expeced_list = [
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

        loader = ptr.TableUrlLoader(url)

        assert loader.format_name == "excel"

        for tabledata, expected in zip(loader.load(), expeced_list):
            assert tabledata == expected
