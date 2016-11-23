from unittest import TestCase, skipIf
from . import *
import gzip
from io import StringIO, BytesIO, TextIOWrapper
from xphyle import *
from xphyle.paths import TempDir, STDIN, STDOUT, STDERR

class XphyleTests(TestCase):
    def setUp(self):
        self.root = TempDir()
        configure(False, False, 1, None)
    
    def tearDown(self):
        self.root.close()
    
    def test_configure(self):
        import xphyle.progress
        import xphyle.formats
        import xphyle.paths
        def wrapper(a,b,c):
            pass
        configure(progress=wrapper, system_progress='foo', threads=2, executable_path=['foo'])
        self.assertEqual(wrapper, xphyle.progress._wrapper)
        self.assertEqual(['foo'], xphyle.progress._system_wrapper)
        self.assertEqual(2, xphyle.formats.get_threads())
        self.assertTrue('foo' in xphyle.paths.executable_paths)
        
        configure(threads=False)
        self.assertEqual(1, xphyle.formats.get_threads())
        
        import multiprocessing
        configure(threads=True)
        self.assertEqual(multiprocessing.cpu_count(), xphyle.formats.get_threads())
    
    def test_guess_format(self):
        with self.assertRaises(ValueError):
            guess_file_format(STDOUT)
        with self.assertRaises(ValueError):
            guess_file_format(STDERR)
        path = self.root.make_file(suffix='.gz')
        with gzip.open(path, 'wt') as o:
            o.write('foo')
        self.assertEqual(guess_file_format(path), 'gzip')
        path = self.root.make_file()
        with gzip.open(path, 'wt') as o:
            o.write('foo')
        self.assertEqual(guess_file_format(path), 'gzip')
        
    def test_open_(self):
        path = self.root.make_file(contents='foo')
        with open_(path, compression=False) as fh:
            self.assertEqual(fh.read(), 'foo')
        with open_(path, compression=False) as fh:
            self.assertEqual(next(fh), 'foo')
        with open(path) as fh:
            with open_(fh, compression=False) as fh2:
                self.assertEqual(fh2.read(), 'foo')
    
    def test_open_safe(self):
        with self.assertRaises(IOError):
            with open_('foobar', mode='r', errors=True) as fh:
                pass
        with self.assertRaises(ValueError):
            with open_(None, mode='r', errors=True) as fh:
                pass
        with open_('foobar', mode='r', errors=False) as fh:
            self.assertIsNone(fh)
        with open_(None, mode='r', errors=False) as fh:
            self.assertIsNone(fh)
    
    def test_xopen_invalid(self):
        # invalid path
        with self.assertRaises(ValueError):
            xopen(1)
        # invalid mode
        with self.assertRaises(ValueError):
            xopen('foo', 'z')
        with self.assertRaises(ValueError):
            xopen('foo', 'rz')
        with self.assertRaises(ValueError):
            xopen('foo', 'rU', newline='\n')
        with self.assertRaises(ValueError):
            xopen(STDOUT, 'w', compression=True)
        with self.assertRaises(ValueError):
            xopen('foo.bar', 'w', compression=True)
    
    def test_xopen_std(self):
        # Try stdin
        with intercept_stdin('foo\n'):
            with xopen(STDIN, 'r', context_wrapper=True, compression=False) as i:
                content = i.read()
                self.assertEqual(content, 'foo\n')
        # Try stdout
        i = StringIO()
        with intercept_stdout(i):
            with xopen(STDOUT, 'w', context_wrapper=True, compression=False) as o:
                o.write('foo')
            self.assertEqual(i.getvalue(), 'foo')
        # Try stderr
        i = StringIO()
        with intercept_stderr(i):
            with xopen(STDERR, 'w', context_wrapper=True, compression=False) as o:
                o.write('foo')
            self.assertEqual(i.getvalue(), 'foo')
        
        # Try binary
        i = BytesIO()
        with intercept_stdout(TextIOWrapper(i)):
            with xopen(STDOUT, 'wb', context_wrapper=True, compression=False) as o:
                o.write(b'foo')
            self.assertEqual(i.getvalue(), b'foo')
        
        # Try compressed
        i = BytesIO()
        with intercept_stdout(TextIOWrapper(i)):
            with xopen(STDOUT, 'wt', compression='gz') as o:
                self.assertEqual(o.compression, 'gzip')
                o.write('foo')
            self.assertEqual(gzip.decompress(i.getvalue()), b'foo')
    
    def test_xopen_compressed_stream(self):
        # Try autodetect compressed
        with intercept_stdin(gzip.compress(b'foo\n'), is_bytes=True):
            with xopen(STDIN, 'rt', compression=True) as i:
                self.assertEqual(i.compression, 'gzip')
                self.assertEqual(i.read(), 'foo\n')
    
    def test_xopen_file(self):
        with self.assertRaises(IOError):
            xopen('foobar', 'r')
        path = self.root.make_file(suffix='.gz')
        with xopen(path, 'w', compression=True) as o:
            self.assertEqual(o.compression, 'gzip')
            o.write('foo')
        with gzip.open(path, 'rt') as i:
            self.assertEqual(i.read(), 'foo')
        with self.assertRaises(ValueError):
            with xopen(path, 'rt', compression='bz2', validate=True):
                pass
    
    @skipIf(no_internet(), "No internet connection")
    def test_xopen_url(self):
        badurl = 'http://google.com/__badurl__'
        with self.assertRaises(ValueError):
            xopen(badurl)
        url = 'https://github.com/jdidion/xphyle/blob/master/tests/foo.gz?raw=True'
        with self.assertRaises(ValueError):
            xopen(url, 'w')
        with open_(url, 'rt') as i:
            self.assertEqual('gzip', i.compression)
            self.assertEqual('foo\n', i.read())
