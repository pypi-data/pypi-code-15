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
Batch utilities
"""

from __future__ import unicode_literals, absolute_import

import inspect


def get_batch_models(model):
    """
    Returns a list of batch models available in the given ``model`` module.
    """
    batches = []
    for name in sorted(dir(model)):
        thing = getattr(model, name)
        if inspect.isclass(thing) and issubclass(thing, model.Base) and issubclass(thing, model.BatchMixin):
            batches.append(thing)
    return batches
