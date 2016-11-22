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
Batch Handlers
"""

from __future__ import unicode_literals, absolute_import

import os
import shutil

from sqlalchemy import orm

from rattail.util import progress_loop, load_object


class BatchHandler(object):
    """
    Base class for all batch handlers; subclass and override as necessary.
    """

    def __init__(self, config):
        self.config = config
        self.enum = config.get_enum()

    @property
    def batch_model_class(self):
        """
        Reference to the data model class of the batch type for which this
        handler is responsible.
        """
        raise NotImplementedError("You must set the 'batch_model_class' attribute "
                                  "for class '{}'".format(self.__class__.__name__))

    @property
    def batch_key(self):
        """
        Unique key for the type of batch for this handler.
        """
        return self.batch_model_class.batch_key

    def get_model_title(self):
        return self.batch_model_class.get_model_title()

    def make_batch(self, session, progress=None, **kwargs):
        """
        Make a new batch, with initial rows if applicable.
        """
        batch = self.batch_model_class(**kwargs)
        session.add(batch)
        session.flush()
        return batch

    @property
    def root_datadir(self):
        """
        The absolute path of the root folder in which data for this particular
        type of batch is stored.  The structure of this path is as follows:

        .. code-block:: none

           /{root_batch_data_dir}/{batch_type_key}

        * ``{root_batch_data_dir}`` - Value of the 'batch.files' option in the
          [rattail] section of config file.
        * ``{batch_type_key}`` - Unique key for the type of batch it is.

        .. note::
           While it is likely that the data folder returned by this method
           already exists, this method does not guarantee it.
        """
        return self.config.batch_filedir(self.batch_key)

    def datadir(self, batch):
        """
        Returns the absolute path of the folder in which the batch's source
        data file(s) resides.  Note that the batch must already have been
        persisted to the database.  The structure of the path returned is as
        follows:

        .. code-block:: none

           /{root_datadir}/{uuid[:2]}/{uuid[2:]}

        * ``{root_datadir}`` - Value returned by :meth:`root_datadir()`.
        * ``{uuid[:2]}`` - First two characters of batch UUID.
        * ``{uuid[2:]}`` - All batch UUID characters *after* the first two.

        .. note::
           While it is likely that the data folder returned by this method
           already exists, this method does not guarantee any such thing.  It
           is typically assumed that the path will have been created by a
           previous call to :meth:`make_batch()` however.
        """
        return os.path.join(self.root_datadir, batch.uuid[:2], batch.uuid[2:])

    def make_datadir(self, batch):
        """
        Returns the data folder specific to the given batch, creating if necessary.
        """
        datadir = self.datadir(batch)
        os.makedirs(datadir)
        return datadir

    # TODO: remove default attr?
    def set_input_file(self, batch, path, attr='filename'):
        """
        Assign the data file found at ``path`` to the batch.  This overwrites
        the given attribute (``attr``) of the batch and places a copy of the
        data file in the batch's data folder.
        """
        datadir = self.make_datadir(batch)
        filename = os.path.basename(path)
        shutil.copyfile(path, os.path.join(datadir, filename))
        setattr(batch, attr, filename)

    def requires_prefill(self, batch):
        """
        This method should return a boolean indicating whether or not the given
        batch requires a "pre-fill" - i.e. populating the initial row set from
        a data source.  Note that this is considered to be a dynamic value
        because some batch types may support being created from one or more (or
        none) optional data sources; in such cases the batch itself must be
        inspected to determine the answer here.
        """
        return False

    def setup_populate(self, batch, progress=None):
        """
        Perform any setup (caching etc.) necessary for populating a batch.
        """

    def teardown_populate(self):
        """
        Perform any teardown (cleanup etc.) necessary after populating a batch.
        """

    def make_initial_rows(self, batch, progress=None):
        """
        Populate the batch with initial data rows.  It is assumed that the data
        source to be used will be known by inspecting various properties of the
        batch itself.
        """
        raise NotImplementedError("Batch requires pre-fill but its data source "
                                  "is unknown/unsupported: {}".format(batch))

    def refreshable(self, batch):
        """
        This method should return a boolean indicating whether or not the
        handler supports a "refresh" operation for the batch, given its current
        condition.  The default simply returns ``True`` but you may override as
        needed.

        Note that this (currently) only affects the enabled/disabled state of
        the Refresh button within the Tailbone batch view.
        """
        return not bool(batch.executed)

    def progress_loop(self, *args, **kwargs):
        return progress_loop(*args, **kwargs)

    def setup_refresh(self, batch, progress=None):
        """
        Perform any setup (caching etc.) necessary for refreshing a batch.
        """

    def teardown_refresh(self):
        """
        Perform any teardown (cleanup etc.) necessary after refreshing a batch.
        """

    def refresh(self, batch, progress=None):
        """
        Perform a full data refresh for the batch.  What exactly this means will
        depend on the type of batch, and specific handler logic.

        Generally speaking this refresh is meant to use queries etc. to obtain
        "fresh" data for the batch (header) and all its rows.  In most cases
        certain data is expected to be "core" to the batch and/or rows, and
        such data will be left intact, with all *other* data values being
        re-calculated and/or reset etc.
        """
        self.setup_refresh(batch, progress=progress)

        def refresh(row, i):
            self.refresh_row(row)

        success = progress_loop(refresh, batch.active_rows(), progress,
                                message="Refreshing batch data rows")

        self.teardown_refresh()
        return success

    def refresh_row(self, row):
        """
        This method will be passed a row object which has already been properly
        added to a batch, and which has basic required fields already
        populated.  This method is then responsible for further populating all
        applicable fields for the row, based on current data within the
        relevant system(s).

        Note that in some cases this method may be called multiple times for
        the same row, e.g. once when first creating the batch and then later
        when a user explicitly refreshes the batch.  The method logic must
        account for this possibility.
        """

    def executable(self, batch):
        """
        This method should return a boolean indicating whether or not execution
        should be allowed for the batch, given its current condition.  The
        default simply returns ``True`` but you may override as needed.

        Note that this (currently) only affects the enabled/disabled state of
        the Execute button within the Tailbone batch view.
        """
        return not bool(batch.executed)


def get_batch_handler(config, batch_key, default=None):
    """
    Returns a batch handler object corresponding to the given batch key.
    """
    spec = config.get('rattail.batch', '{}.handler'.format(batch_key), default=default)
    assert spec, "no handler spec could be determined for batch type: {}".format(batch_key)
    handler = load_object(spec)(config)
    return handler
