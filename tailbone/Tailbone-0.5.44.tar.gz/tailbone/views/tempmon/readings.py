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
Views for tempmon readings
"""

from __future__ import unicode_literals, absolute_import

from rattail.db import model

from formalchemy.fields import SelectFieldRenderer
from webhelpers.html import tags

from tailbone.views import MasterView
from tailbone.views.tempmon.probes import ClientFieldRenderer


class ProbeFieldRenderer(SelectFieldRenderer):

    def render_readonly(self, **kwargs):
        probe = self.raw_value
        if not probe:
            return ''
        return tags.link_to(probe, self.request.route_url('tempmon.probes.view', uuid=probe.uuid))


class TempmonReadingView(MasterView):
    """
    Master view for tempmon readings.
    """
    model_class = model.TempmonReading
    route_prefix = 'tempmon.readings'
    url_prefix = '/tempmon/readings'
    creatable = False
    editable = False

    def configure_grid(self, g):
        g.configure(
            include=[
                g.client,
                g.probe,
                g.taken,
                g.degrees_f,
            ],
            readonly=True)

    def _preconfigure_fieldset(self, fs):
        fs.client.set(label="TempMon Client", renderer=ClientFieldRenderer)
        fs.probe.set(label="TempMon Probe", renderer=ProbeFieldRenderer)

    def configure_fieldset(self, fs):
        fs.configure(
            include=[
                fs.client,
                fs.probe,
                fs.taken,
                fs.degrees_f,
            ])


def includeme(config):
    TempmonReadingView.defaults(config)
