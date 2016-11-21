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
Fabric library for the APT package system
"""

from __future__ import unicode_literals, absolute_import

from fabric.api import sudo
from fabric.contrib.files import append

from rattail.fablib import make_deploy, get_debian_version, get_ubuntu_version


deploy = make_deploy(__file__)


def install(*packages, **kwargs):
    """
    Install one or more packages via ``apt-get install``.
    """
    target = kwargs.get('target_release')
    target = '--target-release={}'.format(target) if target else ''
    sudo('DEBIAN_FRONTEND=noninteractive apt-get --assume-yes {} install {}'.format(
            target, ' '.join(packages)))


def update():
    """
    Perform an ``apt-get update`` operation.
    """
    sudo('apt-get update')


def add_source(entry):
    """
    Add a new entry to the apt/sources.list file
    """
    append('/etc/apt/sources.list', entry, use_sudo=True)
    update()


def dist_upgrade():
    """
    Perform a full ``apt-get dist-upgrade`` operation.
    """
    update()
    sudo('apt-get --assume-yes dist-upgrade')


def configure_listchanges():
    """
    Configure apt listchanges to never use a frontend.
    """
    deploy('apt/listchanges.conf', '/etc/apt/listchanges.conf')


def install_emacs():
    """
    Install the Emacs editor
    """
    emacs = 'emacs-nox'
    debian_version = get_debian_version()
    if debian_version:
        if debian_version < 8:
            emacs = 'emacs23-nox'
    else:
        ubuntu_version = get_ubuntu_version()
        if ubuntu_version and ubuntu_version < 16:
            emacs = 'emacs23-nox'

    install(emacs, 'emacs-goodies-el')
