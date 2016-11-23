import re

import cfscrape

from lxml import etree

from golgi import configurable

from amino import List, __, _, F, Maybe
from amino.util.numeric import try_convert_int


@configurable(piratebay=['host'])
class Search(object):
    _size_re = re.compile('Size ([\d.]+\s[KMGT]iB)')

    def __init__(self, query: str) -> None:
        self.query = query

    @property
    def _fetch(self):
        scraper = cfscrape.create_scraper()
        url = 'https://{}/search/{}/0/99/0'.format(self._host, self.query)
        return scraper.get(url).content

    @property
    def run(self):
        return self._parse(self._fetch)

    def _parse(self, html):
        tree = etree.fromstring(html, etree.HTMLParser())
        table = List.wrap(tree.xpath('//table[@id="searchResult"]')).head
        return table / self._parse_table | List()

    def _parse_table(self, table):
        rows = table.xpath('tr')
        return List.wrap(rows) // self._parse_row

    def _parse_row(self, el):
        sub = F(el.xpath) >> List.wrap
        name = sub('descendant::a[@class="detLink"]').head / _.text
        anchors = sub('descendant::a[@href]')
        magnet = (anchors / __.get('href')).find(__.startswith('magnet:'))
        seeders = sub('td').lift(2) / _.text // try_convert_int
        desc = sub('descendant::font[@class="detDesc"]').head / _.text
        return name.product3(magnet, seeders, desc).map4(self._extract_info)

    def _extract_info(self, name, magnet, seeders, desc):
        size = Maybe(self._size_re.search(desc)) / __.group(1) | '0 B'
        return dict(title=name, magnet_link=magnet, seeders=seeders, size=size)

__all__ = ('Search',)
