from __future__ import absolute_import

# Try to use the stdlib if available, use backport if not.
try:
    # `OrderedDict` is only present in python 2.7 and later. Use this
    # to detect python 2.6 and use the backported module below.
    from collections import OrderedDict
    import collections
except ImportError:
    from . import backport_collections as collections

from .cache import Cache


class LRUCache(Cache):
    """Least Recently Used (LRU) cache implementation."""

    def __init__(self, maxsize, missing=None, getsizeof=None):
        Cache.__init__(self, maxsize, missing, getsizeof)
        self.__order = collections.OrderedDict()

    def __getitem__(self, key, cache_getitem=Cache.__getitem__):
        value = cache_getitem(self, key)
        self.__update(key)
        return value

    def __setitem__(self, key, value, cache_setitem=Cache.__setitem__):
        cache_setitem(self, key, value)
        self.__update(key)

    def __delitem__(self, key, cache_delitem=Cache.__delitem__):
        cache_delitem(self, key)
        del self.__order[key]

    def popitem(self):
        """Remove and return the `(key, value)` pair least recently used."""
        try:
            key = next(iter(self.__order))
        except StopIteration:
            raise KeyError('%s is empty' % self.__class__.__name__)
        else:
            return (key, self.pop(key))

    if hasattr(collections.OrderedDict, 'move_to_end'):
        def __update(self, key):
            try:
                self.__order.move_to_end(key)
            except KeyError:
                self.__order[key] = None
    else:
        def __update(self, key):
            try:
                self.__order[key] = self.__order.pop(key)
            except KeyError:
                self.__order[key] = None
