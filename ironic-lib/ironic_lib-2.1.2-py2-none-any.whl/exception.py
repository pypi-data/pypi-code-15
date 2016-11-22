# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Ironic base exception handling.

Includes decorator for re-raising Ironic-type exceptions.

SHOULD include dedicated exception logging.

"""

import logging
import six

from oslo_config import cfg
from oslo_utils import excutils

from ironic_lib.common.i18n import _
from ironic_lib.common.i18n import _LE


LOG = logging.getLogger(__name__)

exc_log_opts = [
    cfg.BoolOpt('fatal_exception_format_errors',
                default=False,
                help='Make exception message format errors fatal.',
                deprecated_group='DEFAULT'),
]

CONF = cfg.CONF
CONF.register_opts(exc_log_opts, group='ironic_lib')


class IronicException(Exception):
    """Base Ironic Exception

    To correctly use this class, inherit from it and define
    a 'message' property. That message will get printf'd
    with the keyword arguments provided to the constructor.

    """
    message = _("An unknown exception occurred.")
    code = 500
    headers = {}
    safe = False

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass

        if not message:
            try:
                message = self.message % kwargs

            except Exception:
                with excutils.save_and_reraise_exception() as ctxt:
                    # kwargs doesn't match a variable in the message
                    # log the issue and the kwargs
                    prs = ', '.join('%s=%s' % pair for pair in kwargs.items())
                    LOG.exception(_LE('Exception in string format operation '
                                      '(arguments %s)'), prs)
                    if not CONF.ironic_lib.fatal_exception_format_errors:
                        # at least get the core message out if something
                        # happened
                        message = self.message
                        ctxt.reraise = False

        super(IronicException, self).__init__(message)

    def format_message(self):
        if self.__class__.__name__.endswith('_Remote'):
            return self.args[0]
        else:
            return six.text_type(self)


class InstanceDeployFailure(IronicException):
    message = _("Failed to deploy instance: %(reason)s")


class FileSystemNotSupported(IronicException):
    message = _("Failed to create a file system. "
                "File system %(fs)s is not supported.")


class InvalidMetricConfig(IronicException):
    message = _("Invalid value for metrics config option: %(reason)s")
