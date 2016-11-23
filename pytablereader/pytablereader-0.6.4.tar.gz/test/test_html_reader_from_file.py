# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

import os

import pytest
import pytablereader as ptr


class Test_HtmlTableTextLoader_load:

    @pytest.mark.parametrize(["filename"], [
        ["python - Wiktionary.html"],
    ])
    def test_smoke(self, tmpdir, filename):
        test_data_file_path = os.path.join(
            os.path.dirname(__file__), "data", filename)
        loader = ptr.TableFileLoader(test_data_file_path)

        success_count = 0

        for tabledata in loader.load():
            if tabledata.is_empty():
                continue

            assert len(tabledata.dumps()) > 10

            success_count += 1

        assert success_count > 0
