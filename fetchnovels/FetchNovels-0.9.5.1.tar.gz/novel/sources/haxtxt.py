#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import serial, utils, config

BASE_URL = 'http://www.haxtxt.com/files/article/html/{}/{}/'


class Haxtxt(serial.SerialNovel):

    def __init__(self, tid):
        super().__init__(utils.base_to_url(BASE_URL, tid), '#BookText',
                         None, '.intro',
                         chap_sel='.chapterlist dd',
                         chap_type=serial.ChapterType.last,
                         tid=tid)
        self.encoding = config.GB

    def get_title_and_author(self):
        title = self.doc('.btitle h1').text().strip('《》')
        author = self.doc('.btitle em a').text()
        return title, author
