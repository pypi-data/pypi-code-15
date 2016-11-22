# -*- coding: utf-8 -*-
# This file is part of quark-sphinx-theme.
# Copyright (c) 2016 Felix Krull <f_krull@gmx.de>
# Released under the terms of the BSD license; see LICENSE.

from __future__ import print_function

from contextlib import contextmanager
from io import open
import os
import shutil
import sys
import tempfile

try:
    # Prefer StringIO on Python 2 so it can cope with str.
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import html5lib
import sphinx
try:
    import tinycss
except ImportError:
    tinycss = None


@contextmanager
def attrs(obj, **kwargs):
    oldvals = {}
    try:
        for k, v in kwargs.items():
            oldval = getattr(obj, k)
            setattr(obj, k, v)
            oldvals[k] = oldval
        yield
    finally:
        for k, oldval in oldvals.items():
            setattr(obj, k, oldval)


@contextmanager
def capture_output():
    stdout = StringIO()
    with attrs(sys, stdout=stdout, stderr=stdout):
        yield stdout


def get_css_errors(filename_or_fobj, encoding=None):
    if hasattr(filename_or_fobj, 'read'):
        source = filename_or_fobj.read()
    else:
        with open(filename_or_fobj, 'r', encoding=encoding) as fobj:
            source = fobj.read()
    parser = tinycss.make_parser()
    css = parser.parse_stylesheet(source)
    lines = source.split('\n')
    errors = []
    for err in css.errors:
        try:
            errors.append('  %s [%s]\n' % (err, lines[err.line - 1]))
        except IndexError:
            errors.append('  %s\n' % err)
    return errors


def run_sphinx(source_dir, build_dir, builder='html', extra_config={}, tags=[],
               sphinx_build='sphinx-build'):
    args = ['sphinx_build', '-b', builder, '-N']
    for k, v in extra_config.items():
        args.extend(['-D', '%s=%s' % (k, v)])
    for tag in tags:
        args.extend(['-t', tag])
    args.extend([source_dir, build_dir])
    with capture_output() as stdout:
        try:
            ret = sphinx.main(args)
        except SystemExit as e:
            ret = e.code
        if ret != 0:
            raise Exception('%s returned non-zero exit status %s\n'
                            '--- Output:\n%s----' %
                            (args, ret, stdout.getvalue()))


class SphinxBuildFixture:
    source_dir = None
    builder = 'html'
    config = {}
    tags = []

    build_dir = None

    @classmethod
    def setUpClass(cls):
        if not cls.source_dir:
            raise Exception('source_dir not set')
        cls.build_dir = tempfile.mkdtemp(prefix='tmp-sphinx-build-test-')
        try:
            run_sphinx(cls.source_dir, cls.build_dir, cls.builder, cls.config,
                       cls.tags)
        except Exception:
            cls.tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        if cls.build_dir:
            shutil.rmtree(cls.build_dir, True)
            cls.build_dir = None

    def read_document(self, name):
        path = os.path.join(self.build_dir, *name.split('/')) + '.html'
        with open(path, 'rb') as f:
            return html5lib.parse(f, namespaceHTMLElements=False)

    def assertHasElement(self, doc, path, n=1):
        self.assertEqual(len(list(doc.findall(path))), n)

    def assertNotElement(self, doc, path):
        self.assertHasElement(doc, path, 0)

    def assertCSSValid(self, filename_or_fobj, encoding=None, auto_skip=True):
        if not tinycss and auto_skip:
            self.skipTest('tinycss not available')
        errors = get_css_errors(filename_or_fobj, encoding)
        self.assertEqual(len(errors), 0, 'CSS errors:\n' + ''.join(errors))

    def assertSphinxCSSValid(self, basename, encoding='utf-8', auto_skip=True):
        self.assertCSSValid(os.path.join(self.build_dir, '_static', basename),
                            encoding=encoding,
                            auto_skip=auto_skip)


def with_document(docname):
    def wrap1(func):
        def wrap2(self, *args, **kwargs):
            func(self, self.read_document(docname), *args, **kwargs)
        return wrap2
    return wrap1


def with_elements(docname, xpath_expr, n=None):
    def wrap1(func):
        def wrap2(self, *args, **kwargs):
            elems = list(self.read_document(docname).findall(xpath_expr))
            if n is not None and len(elems) != n:
                raise AssertionError('expected %s element(s), got %s' %
                                     (n, len(elems)))
            elif len(elems) == 0:
                raise AssertionError('no elements')
            func(self, elems, *args, **kwargs)
        return wrap2
    return wrap1
