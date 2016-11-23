from __future__ import absolute_import, unicode_literals

from . import *  # NOQA

DEBUG = False

# Update this accordingly;
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

CELERY_ALWAYS_EAGER = False
