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
FormAlchemy Field Renderers
"""

from __future__ import unicode_literals, absolute_import

from .core import CustomFieldRenderer, DateFieldRenderer

from .common import (StrippedTextFieldRenderer, CodeTextAreaFieldRenderer, AutocompleteFieldRenderer,
                     DecimalFieldRenderer, CurrencyFieldRenderer,
                     DateTimeFieldRenderer, DateTimePrettyFieldRenderer, TimeFieldRenderer,
                     EnumFieldRenderer, YesNoFieldRenderer)

from .files import FileFieldRenderer

# TODO: deprecate / remove Link renderers
from .people import (PersonFieldRenderer, PersonFieldLinkRenderer,
                     CustomerFieldRenderer, CustomerFieldLinkRenderer)

from .users import UserFieldRenderer, PermissionsFieldRenderer

from .employees import EmployeeFieldRenderer

from .products import (ProductFieldRenderer, GPCFieldRenderer, BrandFieldRenderer,
                       PriceFieldRenderer, PriceWithExpirationFieldRenderer)

from .stores import StoreFieldRenderer

from .vendors import VendorFieldRenderer, PurchaseFieldRenderer

from .batch import BatchIDFieldRenderer, HandheldBatchFieldRenderer
