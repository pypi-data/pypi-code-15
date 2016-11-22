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
Views for tempmon clients
"""

from __future__ import unicode_literals, absolute_import

import subprocess

from rattail.db import model

import formalchemy as fa
from webhelpers.html import HTML, tags

from tailbone.db import Session
from tailbone.views import MasterView


class ProbesFieldRenderer(fa.FieldRenderer):

    def render_readonly(self, **kwargs):
        probes = self.raw_value
        if not probes:
            return ''
        items = []
        for probe in probes:
            items.append(HTML.tag('li', c=tags.link_to(probe, self.request.route_url('tempmon.probes.view', uuid=probe.uuid))))
        return HTML.tag('ul', c=items)


def unique_config_key(value, field):
    client = field.parent.model
    query = Session.query(model.TempmonClient)\
                   .filter(model.TempmonClient.config_key == value)
    if client.uuid:
        query = query.filter(model.TempmonClient.uuid != client.uuid)
    if query.count():
        raise fa.ValidationError("Config key must be unique")


class TempmonClientView(MasterView):
    """
    Master view for tempmon clients.
    """
    model_class = model.TempmonClient
    route_prefix = 'tempmon.clients'
    url_prefix = '/tempmon/clients'

    def _preconfigure_grid(self, g):
        g.filters['hostname'].default_active = True
        g.filters['hostname'].default_verb = 'contains'
        g.filters['location'].default_active = True
        g.filters['location'].default_verb = 'contains'
        g.default_sortkey = 'config_key'
        g.config_key.set(label="Key")

    def configure_grid(self, g):
        g.configure(
            include=[
                g.config_key,
                g.hostname,
                g.location,
                g.enabled,
                g.online,
            ],
            readonly=True)

    def _preconfigure_fieldset(self, fs):
        fs.config_key.set(validate=unique_config_key)
        fs.probes.set(renderer=ProbesFieldRenderer)

    def configure_fieldset(self, fs):
        fs.configure(
            include=[
                fs.config_key,
                fs.hostname,
                fs.location,
                fs.probes,
                fs.enabled,
                fs.online,
            ])
        if self.creating or self.editing:
            del fs.probes
            del fs.online

    def restart(self):
        client = self.get_instance()
        try:
            subprocess.check_output(['ssh', client.hostname, 'sudo service tempmon restart'],
                                    stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            self.request.session.flash("Failed to restart client: {}".format(error.output), 'error')
        else:
            self.request.session.flash("Client has been restarted: {}".format(
                self.get_instance_title(client)))
        return self.redirect(self.get_action_url('view', client))

    @classmethod
    def defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        url_prefix = cls.get_url_prefix()
        permission_prefix = cls.get_permission_prefix()
        model_key = cls.get_model_key()
        model_title = cls.get_model_title()

        cls._defaults(config)

        # restart tempmon client
        config.add_tailbone_permission(permission_prefix, '{}.restart'.format(permission_prefix),
                                       "Restart a {}".format(model_title))
        config.add_route('{}.restart'.format(route_prefix), '{}/{{{}}}/restart'.format(url_prefix, model_key))
        config.add_view(cls, attr='restart', route_name='{}.restart'.format(route_prefix),
                        permission='{}.restart'.format(permission_prefix))


def includeme(config):
    TempmonClientView.defaults(config)
