"""For internal use only. It provides a slice-like file reader."""

import os

try:
    # pylint: disable=no-name-in-module
    from multiprocessing import Lock
except ImportError:
    from threading import Lock


class FileBuffer(object):

    """A slice-able file reader"""

    def __init__(self, database):
        self._handle = open(database, 'rb')
        self._size = os.fstat(self._handle.fileno()).st_size
        if not hasattr(os, 'pread'):
            self._lock = Lock()

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self._read(key.stop - key.start, key.start)
        elif isinstance(key, int):
            return self._read(1, key)
        else:
            raise TypeError("Invalid argument type.")

    def rfind(self, needle, start):
        """Reverse find needle from start"""
        pos = self._read(self._size - start - 1, start).rfind(needle)
        if pos == -1:
            return pos
        return start + pos

    def size(self):
        """Size of file"""
        return self._size

    def close(self):
        """Close file"""
        self._handle.close()

    if hasattr(os, 'pread'):

        def _read(self, buffersize, offset):
            """read that uses pread"""
            # pylint: disable=no-member
            return os.pread(self._handle.fileno(), buffersize, offset)

    else:

        def _read(self, buffersize, offset):
            """read with a lock

            This lock is necessary as after a fork, the different processes
            will share the same file table entry, even if we dup the fd, and
            as such the same offsets. There does not appear to be a way to
            duplicate the file table entry and we cannot re-open based on the
            original path as that file may have replaced with another or
            unlinked.
            """
            with self._lock:
                self._handle.seek(offset)
                return self._handle.read(buffersize)
