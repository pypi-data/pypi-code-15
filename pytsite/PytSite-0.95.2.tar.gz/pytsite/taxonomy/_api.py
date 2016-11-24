"""Taxonomy Functions.
"""
import re
from pytsite import admin as _admin, router as _router, lang as _lang, util as _util, odm as _odm, reg as _reg
from ._model import Term as _Term

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


_models = []
_localization_enabled = _reg.get('taxonomy.localization', True)


def register_model(model: str, cls, menu_title: str, menu_weight: int = 0, menu_icon: str = 'fa fa-tags'):
    """Register taxonomy model.
    :param cls: str|type
    """
    if is_model_registered(model):
        raise RuntimeError("Model '{}' is already registered as taxonomy model.".format(model))

    if isinstance(cls, str):
        cls = _util.get_class(cls)

    if not issubclass(cls, _Term):
        raise TypeError('Subclass of AbstractTerm expected.')

    _odm.register_model(model, cls)
    _models.append(model)

    menu_url = _router.ep_path('pytsite.odm_ui@browse', {'model': model})
    _admin.sidebar.add_menu(
        'taxonomy', model, menu_title, menu_url, menu_icon, weight=menu_weight,
        permissions=(
            'pytsite.odm_perm.create.' + model,
            'pytsite.odm_perm.modify.' + model,
            'pytsite.odm_perm.delete.' + model,
        )
    )


def is_model_registered(model: str) -> bool:
    """Check if the model is registered as taxonomy model.
    """
    return model in _models


def find(model: str, language: str = None):
    """Get finder for the taxonomy model.
    """
    if not is_model_registered(model):
        raise RuntimeError("Model '{}' is not registered as taxonomy model.".format(model))

    f = _odm.find(model).sort([('weight', _odm.I_DESC)])

    if _localization_enabled:
        f.eq('language', language or _lang.get_current())

    return f


def find_by_title(model: str, title: str, language: str = None) -> _Term:
    """Find term by title.
    """
    return find(model, language).where('title', 'regex_i', '^{}$'.format(title)).first()


def find_by_alias(model: str, alias: str, language: str = None) -> _Term:
    """Find term by alias.
    """
    return find(model, language).eq('alias', alias).first()


def dispense(model: str, title: str, alias: str = None, language: str = None) -> _Term:
    """Create new term or dispense existing.
    """
    if not is_model_registered(model):
        raise RuntimeError("Model '{}' is not registered as taxonomy model.".format(model))

    title = title.strip()

    if not alias:
        alias = _util.transform_str_2(title)

    # Trying to find term by title
    term = find(model, language).where('title', 'regex_i', '^' + title + '$').first()

    # If term is not found, trying to find it by alias
    if not term:
        term = find(model, language).eq('alias', alias).first()

    # If term is not found, create it
    if not term:
        term = _odm.dispense(model)
        term.f_set('title', title).f_set('language', language or _lang.get_current())
        if alias:
            term.f_set('alias', alias)

    return term


def build_alias_str(s: str) -> str:
    return _util.transform_str_2(s)


def sanitize_alias_string(model: str, s: str) -> str:
    """Sanitize a path string.
    """
    s = build_alias_str(s)

    itr = 0
    while True:
        if not find(model).eq('alias', s).count():
            return s

        itr += 1
        if itr == 1:
            s += '-1'
        else:
            s = re.sub('-\d+$', '-' + str(itr), s)
