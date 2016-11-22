# -*- coding: utf-8 -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2016 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU Affero General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for
#  more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Utilities
"""

from __future__ import unicode_literals, absolute_import

import sys
import subprocess

from pkg_resources import iter_entry_points

try:
    from collections import OrderedDict
except ImportError: # pragma no cover
    from ordereddict import OrderedDict


def capture_output(command):
    """
    Runs ``command`` and returns any output it produces.
    """
    # We *need* to pipe ``stdout`` because that's how we capture the output of
    # the ``hg`` command.  However, we must pipe *all* handles in order to
    # prevent issues when running as a GUI but *from* the Windows console.  See
    # also: http://bugs.python.org/issue3905
    kwargs = dict(stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = subprocess.Popen(command, **kwargs).communicate()[0]
    return output


def import_module_path(module_path):
    """
    Import an arbitrary Python module.

    :param module_path: String referencing a module by its "dotted path".

    :returns: The referenced module.
    """
    if module_path in sys.modules:
        return sys.modules[module_path]
    module = __import__(module_path)

    def last_module(module, module_path):
        parts = module_path.split('.')
        parts.pop(0)
        child = getattr(module, parts[0])
        if len(parts) == 1:
            return child
        return last_module(child, '.'.join(parts))

    return last_module(module, module_path)


def load_object(specifier):
    """
    Load an arbitrary object from a module, according to a specifier.

    The specifier string should contain a dotted path to an importable module,
    followed by a colon (``':'``), followed by the name of the object to be
    loaded.  For example:

    .. code-block:: none

       rattail.files:overwriting_move

    You'll notice from this example that "object" in this context refers to any
    valid Python object, i.e. not necessarily a class instance.  The name may
    refer to a class, function, variable etc.  Once the module is imported, the
    ``getattr()`` function is used to obtain a reference to the named object;
    therefore anything supported by that method should work.

    :param specifier: Specifier string.

    :returns: The specified object.
    """
    module_path, name = specifier.split(':')
    module = import_module_path(module_path)
    return getattr(module, name)


def load_entry_points(group):
    """
    Load a set of ``setuptools``-style entry points.

    This is a convenience wrapper around ``pkg_resources.iter_entry_points()``.

    :param group: The group of entry points to be loaded.

    :returns: A dictionary whose keys are the entry point names, and values are
       the loaded entry points.
    """
    entry_points = {}
    for entry_point in iter_entry_points(group):
        entry_points[entry_point.name] = entry_point.load()
    return entry_points


def prettify(text):
    """
    Return a "prettified" version of text.
    """
    text = text.replace('_', ' ')
    text = text.replace('-', ' ')
    words = text.split()
    return ' '.join([x.capitalize() for x in words])


def progress_loop(func, items, factory, *args, **kwargs):
    """
    This will iterate over ``items`` and call ``func`` for each.  If a progress
    ``factory`` kwarg is provided, then a progress instance will be created and
    updated along the way.
    """
    message = kwargs.pop('message', None)
    count = kwargs.pop('count', None)
    if count is None:
        count = len(items)
    if not count:
        return True

    prog = None
    if factory:
        prog = factory(message, count)

    canceled = False
    for i, item in enumerate(items, 1):
        func(item, i, *args, **kwargs)
        if prog and not prog.update(i):
            canceled = True
            break
    if prog:
        prog.destroy()
    return not canceled
