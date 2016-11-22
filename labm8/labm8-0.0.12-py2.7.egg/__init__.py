# Copyright (C) 2015, 2016 Chris Cummins.
#
# This file is part of labm8.
#
# Labm8 is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Labm8 is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with labm8.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Utils for manipulating quantitative experimental data.
"""
import labm8 as lab
import labm8.io

import sys


def exit(status=0):
    """
    Terminate the program with the given status code.
    """
    if status == 0:
        lab.io.printf(lab.io.Colours.GREEN, "Done.")
    else:
        lab.io.printf(lab.io.Colours.RED, "Error {0}".format(status))
    sys.exit(status)


def is_python3():
    """
    Returns whether the Python version is >= 3.0.

    This is for compatability purposes, where you need to implement different
    code for Python 2 and 3.

    Example:
        To import the StringIO class:

          if is_python3():
            from io import StringIO
          else:
            from StringIO import StringIO

    Returns:
        bool: True if Python >= 3, else False.
    """
    return sys.version_info >= (3, 0)


def is_str(obj):
    """
    Check if an object is a string (Python 2 and 3 compatible).
    """
    try:
        return isinstance(obj, basestring)
    except NameError:
        return isinstance(obj, str)


def is_dict(obj):
    """
    Check if an object is a dict.
    """
    return isinstance(obj, dict)


def is_seq(obj):
    """
    Check if an object is a sequence.
    """
    return (not is_str(obj) and not is_dict(obj) and
            (hasattr(obj, "__getitem__") or hasattr(obj, "__iter__")))


def flatten(lists):
    """
    Flatten a list of lists.
    """
    return [item for sublist in lists for item in sublist]
