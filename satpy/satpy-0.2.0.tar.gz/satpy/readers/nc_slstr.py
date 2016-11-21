#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Martin Raspaud

# Author(s):

#   Martin Raspaud <martin.raspaud@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Compact viirs format.
"""

import logging
import os
from datetime import datetime

import numpy as np

import h5netcdf
from satpy.projectable import Projectable
from satpy.readers import DatasetID
from satpy.readers.file_handlers import BaseFileHandler

logger = logging.getLogger(__name__)

PLATFORM_NAMES = {'S3A': 'Sentinel-3A',
                  'S3B': 'Sentinel-3B'}


class NCSLSTRGeo(BaseFileHandler):

    def __init__(self, filename, filename_info, filetype_info):
        super(NCSLSTRGeo, self).__init__(filename, filename_info,
                                         filetype_info)
        self.nc = h5netcdf.File(filename, 'r')
        self.cache = {}

    def get_dataset(self, key, info=None):
        """Load a dataset
        """

        if key in self.cache:
            return self.cache[key]

        logger.debug('Reading %s.', key.name)

        variable = self.nc[key.name]

        ds = (np.ma.masked_equal(variable[:],
                                 variable.attrs['_FillValue']) *
              (variable.attrs.get('scale_factor', 1) * 1.0) +
              variable.attrs.get('add_offset', 0))
        ds.mask = np.ma.getmaskarray(ds)
        self.cache[key] = ds
        return ds

    def get_lonlats(self, navid, nav_info, lon_out, lat_out):
        """Load an area."""
        print nav_info, navid

        if navid.resolution == 500:
            suffix = '_an'
        else:
            suffix = '_in'
        lons = self.get_dataset(DatasetID('longitude' + suffix))
        lats = self.get_dataset(DatasetID('latitude' + suffix))
        lon_out[:] = lons
        lat_out[:] = lats
        lon_out.mask = lons.mask
        lat_out.mask = lats.mask

    @property
    def start_time(self):
        return datetime.strptime(self.nc.attrs['start_time'], '%Y-%m-%dT%H:%M:%S.%fZ')

    @property
    def end_time(self):
        return datetime.strptime(self.nc.attrs['stop_time'], '%Y-%m-%dT%H:%M:%S.%fZ')


class NCSLSTR1B(BaseFileHandler):

    def __init__(self, filename, filename_info, filetype_info):
        super(NCSLSTR1B, self).__init__(filename, filename_info,
                                        filetype_info)
        self.nc = h5netcdf.File(filename, 'r')
        self.channel = filename_info['dataset_name']
        cal_file = os.path.join(os.path.dirname(
            filename), 'viscal.nc')
        self.cal = h5netcdf.File(cal_file, 'r')
        # TODO: get metadata from the manifest file (xfdumanifest.xml)
        self.platform_name = PLATFORM_NAMES[filename_info['mission_id']]
        self.sensor = 'slstr'

    def get_dataset(self, key, info):
        """Load a dataset
        """
        if self.channel != key.name:
            return
        logger.debug('Reading %s.', key.name)
        if key.calibration == 'brightness_temperature':
            variable = self.nc[self.channel + '_BT_in']
        else:
            variable = self.nc[self.channel + '_radiance_an']

        radiances = (np.ma.masked_equal(variable[:],
                                        variable.attrs['_FillValue'], copy=False) *
                     variable.attrs.get('scale_factor', 1) +
                     variable.attrs.get('add_offset', 0))
        units = variable.attrs['units']
        if key.calibration == 'reflectance':
            solar_flux = self.cal['solar_flux'][:]
            d_index = np.ma.masked_equal(self.cal['detector_index'][:],
                                         self.cal['detector_index'].attrs[
                                             '_FillValue'],
                                         copy=False)
            idx = int(key.name[2:]) - 1
            radiances /= solar_flux[idx, d_index]
            radiances *= np.pi * 100
            units = '%'

        proj = Projectable(radiances,
                           name=key.name,
                           copy=False,
                           units=units,
                           platform_name=self.platform_name,
                           sensor=self.sensor)
        return proj

    @property
    def start_time(self):
        return datetime.strptime(self.nc.attrs['start_time'], '%Y-%m-%dT%H:%M:%S.%fZ')

    @property
    def end_time(self):
        return datetime.strptime(self.nc.attrs['stop_time'], '%Y-%m-%dT%H:%M:%S.%fZ')


class NCSLSTRAngles(BaseFileHandler):

    datasets = {'satellite_azimuth_angle': 'OAA',
                'satellite_zenith_angle': 'OZA',
                'solar_azimuth_angle': 'SAA',
                'solar_zenith_angle': 'SZA'}

    def __init__(self, filename, filename_info, filetype_info):
        super(NCSLSTRAngles, self).__init__(filename, filename_info,
                                            filetype_info)
        self.nc = None
        # TODO: get metadata from the manifest file (xfdumanifest.xml)
        self.platform_name = PLATFORM_NAMES[filename_info['mission_id']]
        self.sensor = 'slstr'
        self._start_time = filename_info['start_time']
        self._end_time = filename_info['end_time']

    def get_dataset(self, key, info):
        """Load a dataset
        """
        if key.name not in self.datasets:
            return

        if self.nc is None:
            self.nc = h5netcdf.File(self.filename, 'r')

        logger.debug('Reading %s.', key.name)
        variable = self.nc[self.datasets[key.name]]

        values = (np.ma.masked_equal(variable[:],
                                     variable.attrs['_FillValue'], copy=False) *
                  variable.attrs.get('scale_factor', 1) +
                  variable.attrs.get('add_offset', 0))
        units = variable.attrs['units']

        l_step = self.nc.attrs['al_subsampling_factor']
        c_step = self.nc.attrs['ac_subsampling_factor']

        if c_step != 1 or l_step != 1:
            from geotiepoints.interpolator import Interpolator
            tie_lines = np.arange(
                0, (values.shape[0] - 1) * l_step + 1, l_step)
            tie_cols = np.arange(0, (values.shape[1] - 1) * c_step + 1, c_step)
            lines = np.arange((values.shape[0] - 1) * l_step + 1)
            cols = np.arange((values.shape[1] - 1) * c_step + 1)
            along_track_order = 1
            cross_track_order = 3
            satint = Interpolator([values],
                                  (tie_lines, tie_cols),
                                  (lines, cols),
                                  along_track_order,
                                  cross_track_order)
            (values, ) = satint.interpolate()

        proj = Projectable(values,
                           copy=False,
                           units=units,
                           platform_name=self.platform_name,
                           sensor=self.sensor)
        return proj

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time
