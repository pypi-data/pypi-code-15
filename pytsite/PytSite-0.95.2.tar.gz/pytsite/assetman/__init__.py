"""PytSite Asset Manager.
"""
# Public API
from ._api import register_package, add, remove, dump_js, dump_css, url, add_inline, dump_inline, get_urls, \
    get_locations, reset, detect_collection, build

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import console, events, lang, tpl
    from . import _console_command, _api

    # Resources
    lang.register_package(__name__)

    # Console commands
    console.register_command(_console_command.Assetman())

    # Event handlers
    events.listen('pytsite.router.dispatch', reset, priority=-999)
    events.listen('pytsite.update.after', build)

    # Tpl globals
    tpl.register_global('add_asset', add)
    tpl.register_global('asset_url', url)
    tpl.register_global('css_links', dump_css)
    tpl.register_global('js_links', dump_js)
    tpl.register_global('inline_js', dump_inline)

    # We add this here to avoid cyclic dependency
    register_package('pytsite.lang')
    add('pytsite.lang@translations.js', True, weight=-997)


_init()
