#!/usr/bin/python
# -*- coding: utf-8

from os.path import dirname, basename, isfile
import glob

modules = glob.glob(dirname(__file__) + "/[!__]*.py")

__all__ = [basename(f)[:-3] for f in modules if isfile(f)]

__name__ = "pgw_tools"

__doc__ = """Utils package for pygetwallpapers"""
