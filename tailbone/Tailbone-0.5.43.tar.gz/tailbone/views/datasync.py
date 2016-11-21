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
DataSync Views
"""

from __future__ import unicode_literals, absolute_import

import subprocess
import logging

from rattail.db import model
from rattail.config import parse_list

from tailbone.views import MasterView


log = logging.getLogger(__name__)


class DataSyncChangesView(MasterView):
    """
    Master view for the DataSyncChange model.
    """
    model_class = model.DataSyncChange
    model_title = "DataSync Change"
    url_prefix = '/datasync/changes'
    permission_prefix = 'datasync'

    creatable = False
    viewable = False
    editable = False
    deletable = False

    def configure_grid(self, g):
        g.default_sortkey = 'obtained'
        g.configure(
            include=[
                g.source,
                g.payload_type,
                g.payload_key,
                g.deletion,
                g.obtained,
                g.consumer,
            ],
            readonly=True)

    def restart(self):
        # TODO: Add better validation (e.g. CSRF) here?
        if self.request.method == 'POST':
            cmd = parse_list(self.rattail_config.require('tailbone', 'datasync.restart'))
            log.debug("attempting datasync restart with command: {}".format(cmd))
            result = subprocess.call(cmd)
            if result == 0:
                self.request.session.flash("DataSync daemon has been restarted.")
            else:
                self.request.session.flash("DataSync daemon could not be restarted; result was: {}".format(result), 'error')
        return self.redirect(self.request.route_url('datasyncchanges'))

    @classmethod
    def defaults(cls, config):

        # fix permission group title
        config.add_tailbone_permission_group('datasync', label="DataSync")

        # restart daemon
        config.add_route('datasync.restart', '/datasync/restart')
        config.add_view(cls, attr='restart', route_name='datasync.restart',
                        permission='datasync.restart')
        config.add_tailbone_permission('datasync', 'datasync.restart', label="Restart DataSync Daemon")

        cls._defaults(config)


def includeme(config):
    DataSyncChangesView.defaults(config)
