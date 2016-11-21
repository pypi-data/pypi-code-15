# -*- coding: utf-8 -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2015 Lance Edgar
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
Data Models
"""

from .core import Base, uuid_column, getset_factory, Setting, Change
from .contact import PhoneNumber, EmailAddress

from .people import Person, PersonPhoneNumber, PersonEmailAddress, PersonMailingAddress
from .users import Role, Permission, User, UserRole
from .stores import Store, StorePhoneNumber, StoreEmailAddress
from .customers import (Customer, CustomerPhoneNumber, CustomerEmailAddress,
                        CustomerGroup, CustomerGroupAssignment, CustomerPerson)

from .org import Department, Subdepartment, Category, Family, ReportCode, DepositLink
from .employees import (Employee, EmployeePhoneNumber, EmployeeEmailAddress,
                        EmployeeStore, EmployeeDepartment)
from .shifts import ScheduledShift, WorkedShift

from .vendors import Vendor, VendorPhoneNumber, VendorEmailAddress, VendorContact
from .products import Brand, Tax, Product, ProductCode, ProductCost, ProductPrice
from .purchase import PurchaseBase, PurchaseItemBase, Purchase, PurchaseItem

from .messages import Message, MessageRecipient

from .datasync import DataSyncChange
from .batches import Batch, BatchColumn, BatchRow
from .labels import LabelProfile
from .bouncer import EmailBounce

from .batch import BatchMixin, BaseFileBatchMixin, FileBatchMixin, BatchRowMixin, ProductBatchRowMixin
from .batch.handheld import HandheldBatch, HandheldBatchRow
from .batch.inventory import InventoryBatch, InventoryBatchRow
from .batch.labels import LabelBatch, LabelBatchRow
from .batch.purchase import PurchaseBatch, PurchaseBatchRow
from .batch.vendorcatalog import VendorCatalog, VendorCatalogRow
from .batch.vendorinvoice import VendorInvoice, VendorInvoiceRow
