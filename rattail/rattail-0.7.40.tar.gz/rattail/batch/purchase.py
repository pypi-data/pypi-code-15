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
Handler for purchase order batches
"""

from __future__ import unicode_literals, absolute_import

from sqlalchemy import orm

from rattail.db import model
from rattail.batch import BatchHandler
from rattail.time import make_utc


class PurchaseBatchHandler(BatchHandler):
    """
    Handler for purchase order batches.
    """
    batch_model_class = model.PurchaseBatch

    def requires_prefill(self, batch):
        # TODO: this probably should change soon, for now this works..
        return batch.purchase and batch.mode in (self.enum.PURCHASE_BATCH_MODE_RECEIVING,
                                                 self.enum.PURCHASE_BATCH_MODE_COSTING)

    def make_initial_rows(self, batch, progress=None):
        assert batch.purchase and batch.mode in (self.enum.PURCHASE_BATCH_MODE_RECEIVING,
                                                 self.enum.PURCHASE_BATCH_MODE_COSTING)

        def append(item, i):
            row = model.PurchaseBatchRow()
            row.item = item
            row.product = item.product
            row.cases_ordered = item.cases_ordered or None
            row.units_ordered = item.units_ordered or None
            row.cases_received = item.cases_received or None
            row.units_received = item.units_received or None
            row.po_unit_cost = item.po_unit_cost
            row.po_total = item.po_total
            if batch.mode == self.enum.PURCHASE_BATCH_MODE_COSTING:
                row.invoice_unit_cost = item.invoice_unit_cost
                row.invoice_total = item.invoice_total
            batch.add_row(row)
            self.refresh_row(row)

        assert self.progress_loop(append, batch.purchase.items, progress,
                                  message="Adding initial rows to batch")

    def refresh(self, batch, progress=None):
        if batch.mode == self.enum.PURCHASE_BATCH_MODE_NEW:
            batch.po_total = 0
        elif batch.mode in (self.enum.PURCHASE_BATCH_MODE_RECEIVING,
                            self.enum.PURCHASE_BATCH_MODE_COSTING):
            batch.invoice_total = 0
        return super(PurchaseBatchHandler, self).refresh(batch, progress=progress)

    def refresh_row(self, row):
        """
        Refreshing a row will A) assume that ``row.product`` is already set to
        a valid product, and B) update various other fields on the row
        (description, size, etc.)  to reflect the current product data.  It
        also will adjust the batch PO total per the row PO total.
        """
        batch = row.batch
        product = row.product
        cost = row.product.cost_for_vendor(batch.vendor)
        assert cost
        row.upc = product.upc
        row.brand_name = unicode(product.brand or '')
        row.description = product.description
        row.size = product.size
        if product.department:
            row.department_number = product.department.number
            row.department_name = product.department.name
        else:
            row.department_number = None
            row.department_name = None
        row.vendor_code = cost.code
        row.case_quantity = cost.case_size

        if batch.mode == self.enum.PURCHASE_BATCH_MODE_NEW:
            row.po_unit_cost = cost.unit_cost
            row.po_total = (row.po_unit_cost * (row.units_ordered or 0)) + (
                row.po_unit_cost * (row.cases_ordered or 0) * row.case_quantity)
            batch.po_total = (batch.po_total or 0) + row.po_total
        elif batch.mode in (self.enum.PURCHASE_BATCH_MODE_RECEIVING,
                            self.enum.PURCHASE_BATCH_MODE_COSTING):
            row.invoice_unit_cost = cost.unit_cost
            row.invoice_total = (row.invoice_unit_cost * (row.units_received or 0)) + (
                row.invoice_unit_cost * (row.cases_received or 0) * row.case_quantity)
            batch.invoice_total = (batch.invoice_total or 0) + row.invoice_total

        if batch.mode == self.enum.PURCHASE_BATCH_MODE_NEW:
            row.status_code = row.STATUS_OK

        elif batch.mode in (self.enum.PURCHASE_BATCH_MODE_RECEIVING,
                            self.enum.PURCHASE_BATCH_MODE_COSTING):
            if row.cases_received is None and row.units_received is None:
                row.status_code = row.STATUS_INCOMPLETE
            elif row.cases_received != row.cases_ordered or row.units_received != row.units_ordered:
                row.status_code = row.STATUS_ORDERED_RECEIVED_DIFFER
            else:
                row.status_code = row.STATUS_OK

    def execute(self, batch, user, progress=None):
        """
        Default behavior for executing a purchase batch will create a new
        purchase, by invoking :meth:`make_purchase()`.
        """
        session = orm.object_session(batch)

        if batch.mode == self.enum.PURCHASE_BATCH_MODE_NEW:
            return self.make_purchase(batch, user, progress=progress)

        elif batch.mode == self.enum.PURCHASE_BATCH_MODE_RECEIVING:
            with session.no_autoflush:
                return self.receive_purchase(batch, progress=progress)

        elif batch.mode == self.enum.PURCHASE_BATCH_MODE_COSTING:
            # TODO: finish this...
            # with session.no_autoflush:
            #     return self.cost_purchase(batch, progress=progress)
            purchase = batch.purchase
            purchase.invoice_date = batch.invoice_date
            purchase.status = self.enum.PURCHASE_STATUS_COSTED
            return purchase

        assert False

    def make_purchase(self, batch, user, progress=None):
        """
        Effectively clones the given batch, creating a new Purchase in the
        Rattail system.
        """
        session = orm.object_session(batch)
        purchase = model.Purchase()

        # TODO: should be smarter and only copy certain fields here
        skip_fields = [
            'date_received',
        ]
        for prop in orm.object_mapper(batch).iterate_properties:
            if prop.key in skip_fields:
                continue
            if hasattr(purchase, prop.key):
                setattr(purchase, prop.key, getattr(batch, prop.key))

        def clone(row, i):
            item = model.PurchaseItem()
            # TODO: should be smarter and only copy certain fields here
            for prop in orm.object_mapper(row).iterate_properties:
                if hasattr(item, prop.key):
                    setattr(item, prop.key, getattr(row, prop.key))
            purchase.items.append(item)

        assert self.progress_loop(clone, batch.active_rows(), progress,
                                  message="Creating purchase items")

        purchase.created = make_utc()
        purchase.created_by = user
        purchase.status = self.enum.PURCHASE_STATUS_ORDERED
        session.add(purchase)
        batch.purchase = purchase
        return purchase

    def receive_purchase(self, batch, progress=None):
        """
        Update the purchase for the given batch, to indicate received status.
        """
        session = orm.object_session(batch)
        purchase = batch.purchase
        if not purchase:
            batch.purchase = purchase = model.Purchase()

            # TODO: should be smarter and only copy certain fields here
            skip_fields = [
                'date_received',
            ]
            for prop in orm.object_mapper(batch).iterate_properties:
                if prop.key in skip_fields:
                    continue
                if hasattr(purchase, prop.key):
                    setattr(purchase, prop.key, getattr(batch, prop.key))

        purchase.invoice_number = batch.invoice_number
        purchase.invoice_date = batch.invoice_date
        purchase.invoice_total = batch.invoice_total
        purchase.date_received = batch.date_received

        # determine which fields we'll copy when creating new purchase item
        copy_fields = []
        for prop in orm.class_mapper(model.PurchaseItem).iterate_properties:
            if hasattr(model.PurchaseBatchRow, prop.key):
                copy_fields.append(prop.key)

        def update(row, i):
            item = row.item
            if not item:
                row.item = item = model.PurchaseItem()
                for field in copy_fields:
                    setattr(item, field, getattr(row, field))
                purchase.items.append(item)

            item.cases_received = row.cases_received or 0
            item.units_received = row.units_received or 0
            item.invoice_line_number = row.invoice_line_number
            item.invoice_case_cost = row.invoice_case_cost
            item.invoice_unit_cost = row.invoice_unit_cost
            item.invoice_total = row.invoice_total

        with session.no_autoflush:
            assert self.progress_loop(update, batch.active_rows(), progress,
                                      message="Updating purchase line items")

        purchase.status = self.enum.PURCHASE_STATUS_RECEIVED
        return purchase
