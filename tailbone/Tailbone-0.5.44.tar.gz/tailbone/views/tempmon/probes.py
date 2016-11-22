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
Views for tempmon probes
"""

from __future__ import unicode_literals, absolute_import

from rattail.db import model

from formalchemy.fields import SelectFieldRenderer
from webhelpers.html import tags

from tailbone import forms
from tailbone.views import MasterView


class ClientFieldRenderer(SelectFieldRenderer):

    def render_readonly(self, **kwargs):
        client = self.raw_value
        if not client:
            return ''
        return tags.link_to(client, self.request.route_url('tempmon.clients.view', uuid=client.uuid))


class TempmonProbeView(MasterView):
    """
    Master view for tempmon probes.
    """
    model_class = model.TempmonProbe
    route_prefix = 'tempmon.probes'
    url_prefix = '/tempmon/probes'

    def _preconfigure_grid(self, g):
        g.joiners['client'] = lambda q: q.join(model.TempmonClient)
        g.sorters['client'] = g.make_sorter(model.TempmonClient.config_key)
        g.default_sortkey = 'client'
        g.config_key.set(label="Key")
        g.appliance_type.set(renderer=forms.renderers.EnumFieldRenderer(self.enum.TEMPMON_APPLIANCE_TYPE))
        g.status.set(renderer=forms.renderers.EnumFieldRenderer(self.enum.TEMPMON_PROBE_STATUS))

    def configure_grid(self, g):
        g.configure(
            include=[
                g.client,
                g.config_key,
                g.appliance_type,
                g.description,
                g.device_path,
                g.enabled,
                g.status,
            ],
            readonly=True)

    def _preconfigure_fieldset(self, fs):
        fs.client.set(label="TempMon Client", renderer=ClientFieldRenderer)
        fs.appliance_type.set(renderer=forms.renderers.EnumFieldRenderer(self.enum.TEMPMON_APPLIANCE_TYPE))
        fs.status.set(renderer=forms.renderers.EnumFieldRenderer(self.enum.TEMPMON_PROBE_STATUS))

    def configure_fieldset(self, fs):
        fs.configure(
            include=[
                fs.client,
                fs.config_key,
                fs.appliance_type,
                fs.description,
                fs.device_path,
                fs.critical_temp_min,
                fs.good_temp_min,
                fs.good_temp_max,
                fs.critical_temp_max,
                fs.therm_status_timeout,
                fs.status_alert_timeout,
                fs.enabled,
                fs.status,
            ])
        if self.creating or self.editing:
            del fs.status


def includeme(config):
    TempmonProbeView.defaults(config)
