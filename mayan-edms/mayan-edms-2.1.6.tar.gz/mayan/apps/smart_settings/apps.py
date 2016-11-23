from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from common import MayanAppConfig, menu_setup, menu_object
from common.widgets import exists_widget
from navigation import SourceColumn

from .classes import Namespace, Setting
from .links import link_namespace_detail, link_namespace_list
from .widgets import setting_widget


class SmartSettingsApp(MayanAppConfig):
    app_namespace = 'settings'
    app_url = 'settings'
    name = 'smart_settings'
    verbose_name = _('Smart settings')

    def ready(self):
        super(SmartSettingsApp, self).ready()

        Namespace.initialize()

        SourceColumn(
            source=Namespace, label=_('Setting count'),
            func=lambda context: len(context['object'].settings)
        )
        SourceColumn(
            source=Setting, label=_('Name'),
            func=lambda context: setting_widget(context['object'])
        )
        SourceColumn(
            source=Setting, label=_('Value'), attribute='serialized_value'
        )
        SourceColumn(
            source=Setting, label=_('Found in path'),
            func=lambda context: exists_widget(
                context['object'].value
            ) if context['object'].is_path else _('n/a')
        )

        menu_object.bind_links(
            links=(link_namespace_detail,), sources=(Namespace,)
        )
        menu_setup.bind_links(links=(link_namespace_list,))
