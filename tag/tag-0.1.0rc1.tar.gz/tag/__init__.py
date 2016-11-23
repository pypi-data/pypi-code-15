#!/usr/bin/env python
#
# ------------------------------------------------------------------------------
# Copyright (C) 2015 Daniel Standage <daniel.standage@gmail.com>
#
# This file is part of tag (http://github.com/standage/tag) and is licensed
# under the BSD 3-clause license: see LICENSE.
# ------------------------------------------------------------------------------
"""Package-wide configuration"""

from . import comment
from . import feature
from . import range
from . import reader

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
