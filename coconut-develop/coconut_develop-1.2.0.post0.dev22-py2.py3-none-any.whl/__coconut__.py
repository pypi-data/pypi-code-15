#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
License: Apache 2.0
Description: Mimics what a compiled __coconut__.py would do.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

from coconut.compiler import Compiler as __coconut_compiler__

#-----------------------------------------------------------------------------------------------------------------------
# HEADER:
#-----------------------------------------------------------------------------------------------------------------------

# executes the __coconut__.py header for the current Python version
exec(__coconut_compiler__(target="sys").getheader("code"))
