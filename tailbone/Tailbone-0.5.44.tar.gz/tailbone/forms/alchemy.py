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
FormAlchemy Forms
"""

from __future__ import unicode_literals, absolute_import

from rattail.core import Object

import formalchemy as fa
from pyramid.renderers import render

from tailbone.db import Session


class TemplateEngine(fa.templates.TemplateEngine):
    """
    Mako template engine for FormAlchemy.
    """

    def render(self, template, prefix='/forms/', suffix='.mako', **kwargs):
        template = ''.join((prefix, template, suffix))
        return render(template, kwargs)


class AlchemyForm(Object):
    """
    Form to contain a :class:`formalchemy.FieldSet` instance.
    """
    id = None
    create_label = "Create"
    update_label = "Save"

    allow_successive_creates = False

    def __init__(self, request, fieldset, **kwargs):
        super(AlchemyForm, self).__init__(**kwargs)
        self.request = request
        self.fieldset = fieldset

    def _get_readonly(self):
        return self.fieldset.readonly
    def _set_readonly(self, val):
        self.fieldset.readonly = val
    readonly = property(_get_readonly, _set_readonly)

    @property
    def successive_create_label(self):
        return "%s and continue" % self.create_label

    def render(self, **kwargs):
        kwargs['form'] = self
        if self.readonly:
            template = '/forms/form_readonly.mako'
        else:
            template = '/forms/form.mako'
        return render(template, kwargs)

    def render_fields(self):
        return self.fieldset.render()

    def save(self):
        self.fieldset.sync()
        Session.flush()

    def validate(self):
        self.fieldset.rebind(data=self.request.params)
        return self.fieldset.validate()
