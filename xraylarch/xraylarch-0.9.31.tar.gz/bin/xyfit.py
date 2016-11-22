#!/usr/bin/env python
"""
XY Viewer and Fit App
"""
import os
import larch
from larch_plugins.wx import XYFitViewer

os.chdir(larch.site_config.home_dir)
XYFitViewer().run()
