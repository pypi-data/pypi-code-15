#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import single, utils

BASE_URL = 'http://ebook.s-dragon.org/forum/archiver/?tid-{}.html'


class Sdragon(single.SingleNovel):

    def __init__(self, tid):
        super().__init__(utils.base_to_url(BASE_URL, tid),
                         '.archiver_postbody',
                         title_sel='h2',
                         title_type=single.TitleType.selector,
                         tid=tid)
