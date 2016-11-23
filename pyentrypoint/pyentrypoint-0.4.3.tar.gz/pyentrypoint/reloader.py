"""
    Send signal to pid 1 to reload service
"""
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import signal
from multiprocessing import Process

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from .logs import Logs


class Reload(FileSystemEventHandler):

    """Reload object"""

    def __init__(self, sig, files, pid=1):
        self.signal = sig
        self.files = files
        self.pid = pid
        self.log = Logs().log

    def on_any_event(self, event):
        if event.src_path in self.files:
            self.log.info(
                'File {file} has changed, send sig {sig} to pid {pid}'.format(
                    file=event.src_path,
                    sig=self.signal,
                    pid=self.pid,
                )
            )
            os.kill(self.pid, self.signal)


class Reloader(object):

    """Reload service when files change"""

    def __init__(self, sig='SIGHUP', files=[]):
        if not files:
            raise Exception('No file to watch for reload')

        self.proc = None
        self._files = files
        sig_attr = getattr(signal, sig)
        try:
            assert int(sig_attr)
        except:
            raise Exception('Wrong signal provided for reload')
        self.observer = Observer()
        rel = Reload(sig=sig_attr, files=self.files)
        for dir in self.dirs:
            self.observer.schedule(rel, dir, recursive=False)

    def _get_files(self):
        """Return iterator of tuples (path, file)"""
        for f in self._files:
            if os.path.isdir(f):
                yield (f, f)
            yield (os.path.dirname(f), f)

    @property
    def files(self):
        """Return list of watched files"""
        return list(set([files[1] for files in self._get_files()]))

    @property
    def dirs(self):
        """Return list of watched directories"""
        return list(set([files[0] for files in self._get_files()]))

    def run(self, ret=False):
        while True:
            self.observer.start()
            if ret:
                return self.observer
            self.observer.join()

    def run_in_process(self):
        self.proc = Process(target=self.run)
        self.proc.start()

    def stop(self):
        if self.proc:
            self.proc.stop()
        else:
            self.observer.stop()
