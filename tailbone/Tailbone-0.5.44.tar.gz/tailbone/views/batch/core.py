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
Base views for maintaining "new-style" batches.

.. note::
   This is all still somewhat experimental.
"""

from __future__ import unicode_literals, absolute_import

import os
import datetime
import logging
from cStringIO import StringIO

from sqlalchemy import orm

from rattail.db import model, Session as RattailSession
from rattail.threads import Thread
from rattail.csvutil import UnicodeDictWriter
from rattail.util import load_object

import formalchemy
from pyramid import httpexceptions
from pyramid.renderers import render_to_response
from pyramid.response import FileResponse
from pyramid_simpleform import Form
from webhelpers.html import HTML, tags

from tailbone import forms, newgrids as grids
from tailbone.db import Session
from tailbone.views import MasterView, SearchableAlchemyGridView, CrudView
from tailbone.forms.renderers.batch import FileFieldRenderer
from tailbone.grids.search import BooleanSearchFilter, EnumSearchFilter
from tailbone.progress import SessionProgress


log = logging.getLogger(__name__)


class BatchMasterView(MasterView):
    """
    Base class for all "batch master" views.
    """
    default_handler_spec = None
    has_rows = True
    rows_deletable = True
    rows_downloadable = True
    refreshable = True
    refresh_after_create = False
    edit_with_rows = False

    def __init__(self, request):
        super(BatchMasterView, self).__init__(request)
        self.handler = self.get_handler()

    def get_handler(self):
        """
        Returns a `BatchHandler` instance for the view.  All (?) custom batch
        views should define a default handler class; however this may in all
        (?)  cases be overridden by config also.  The specific setting required
        to do so will depend on the 'key' for the type of batch involved, e.g.
        assuming the 'vendor_catalog' batch:

        .. code-block:: ini

           [rattail.batch]
           vendor_catalog.handler = myapp.batch.vendorcatalog:CustomCatalogHandler

        Note that the 'key' for a batch is generally the same as its primary
        table name, although technically it is whatever value returns from the
        ``batch_key`` attribute of the main batch model class.
        """
        key = self.model_class.batch_key
        spec = self.rattail_config.get('rattail.batch', '{}.handler'.format(key),
                                       default=self.default_handler_spec)
        if spec:
            return load_object(spec)(self.rattail_config)
        return self.batch_handler_class(self.rattail_config)

    def template_kwargs_view(self, **kwargs):
        batch = kwargs['instance']
        kwargs['batch'] = batch
        kwargs['handler'] = self.handler
        kwargs['execute_title'] = self.get_execute_title(batch)
        kwargs['execute_enabled'] = self.executable(batch)
        if kwargs['execute_enabled'] and self.has_execution_options:
            kwargs['rendered_execution_options'] = self.render_execution_options(batch)
        return kwargs

    def render_execution_options(self, batch):
        form = self.make_execution_options_form(batch)
        kwargs = {
            'batch': batch,
            'form': forms.FormRenderer(form),
        }
        kwargs = self.get_exec_options_kwargs(**kwargs)
        return self.render('exec_options', kwargs)

    def get_exec_options_kwargs(self, **kwargs):
        return kwargs

    def get_instance_title(self, batch):
        return batch.id_str or unicode(batch)

    def _preconfigure_grid(self, g):
        """
        Apply some commonly-useful pre-configuration to the main batch grid.
        """
        g.joiners['created_by'] = lambda q: q.join(model.User,
                                                   model.User.uuid == self.model_class.created_by_uuid)
        g.joiners['executed_by'] = lambda q: q.outerjoin(model.User,
                                                         model.User.uuid == self.model_class.executed_by_uuid)

        g.filters['executed'].default_active = True
        g.filters['executed'].default_verb = 'is_null'

        g.sorters['created_by'] = g.make_sorter(model.User.username)
        g.sorters['executed_by'] = g.make_sorter(model.User.username)

        g.default_sortkey = 'created'
        g.default_sortdir = 'desc'

        g.id.set(label="ID", renderer=forms.renderers.BatchIDFieldRenderer)
        g.created_by.set(label="Created by", renderer=forms.renderers.UserFieldRenderer)
        g.cognized_by.set(renderer=forms.renderers.UserFieldRenderer)
        g.executed_by.set(label="Executed by", renderer=forms.renderers.UserFieldRenderer)

    def configure_grid(self, g):
        """
        Apply final configuration to the main batch grid.  Custom batch views
        are encouraged to override this method.
        """
        g.configure(
            include=[
                g.id,
                g.created,
                g.created_by,
                g.executed,
                g.executed_by,
            ],
            readonly=True)

    def _preconfigure_fieldset(self, fs):
        """
        Apply some commonly-useful pre-configuration to the main batch
        fieldset.
        """
        fs.id.set(label="Batch ID", readonly=True, renderer=forms.renderers.BatchIDFieldRenderer)

        fs.created.set(readonly=True)
        fs.created_by.set(label="Created by", renderer=forms.renderers.UserFieldRenderer,
                          readonly=True)
        fs.cognized_by.set(label="Cognized by", renderer=forms.renderers.UserFieldRenderer)
        fs.executed_by.set(label="Executed by", renderer=forms.renderers.UserFieldRenderer)

        if self.creating and self.request.user:
            batch = fs.model
            batch.created_by_uuid = self.request.user.uuid

    def configure_fieldset(self, fs):
        """
        Apply final configuration to the main batch fieldset.  Custom batch
        views are encouraged to override this method.
        """
        if self.creating:
            fs.configure()

        else:
            batch = fs.model
            if batch.executed:
                fs.configure(
                    include=[
                        fs.id,
                        fs.created,
                        fs.created_by,
                        fs.executed,
                        fs.executed_by,
                    ])
            else:
                fs.configure(
                    include=[
                        fs.id,
                        fs.created,
                        fs.created_by,
                    ])

    def _postconfigure_fieldset(self, fs):
        if self.creating:
            unwanted = [
                'id',
                'rowcount',
                'created',
                'created_by',
                'cognized',
                'cognized_by',
                'executed',
                'executed_by',
                'purge',
                'data_rows',
            ]
            for field in unwanted:
                if field in fs.render_fields:
                    delattr(fs, field)
        else:
            batch = fs.model
            if not batch.executed:
                unwanted = [
                    'executed',
                    'executed_by',
                ]
                for field in unwanted:
                    if field in fs.render_fields:
                        delattr(fs, field)

    def save_create_form(self, form):
        self.before_create(form)

        with Session.no_autoflush:

            # transfer form data to batch instance
            form.fieldset.sync()
            batch = form.fieldset.model

            # current user is batch creator
            batch.created_by = self.request.user or self.late_login_user()

            # destroy initial batch and re-make using handler
            kwargs = self.get_batch_kwargs(batch)
            Session.expunge(batch)
            batch = self.handler.make_batch(Session(), **kwargs)

        Session.flush()

        # TODO: this needs work yet surely...
        # if batch has input data file, let handler properly establish that
        filename = getattr(batch, 'filename', None)
        if filename:
            path = os.path.join(self.upload_dir, filename)
            self.handler.set_input_file(batch, path)
            os.remove(path)

        # return this object to replace the original
        return batch

    def get_batch_kwargs(self, batch):
        """
        Return a kwargs dict for use with ``self.handler.make_batch()``, using
        the given batch as a template.
        """
        kwargs = {}
        if batch.created_by:
            kwargs['created_by'] = batch.created_by
        elif batch.created_by_uuid:
            kwargs['created_by_uuid'] = batch.created_by_uuid
        if hasattr(batch, 'filename'):
            kwargs['filename'] = batch.filename
        return kwargs

    # TODO: deprecate / remove this (is it used at all now?)
    def init_batch(self, batch):
        """
        Initialize a new batch.  Derived classes can override this to
        effectively provide default values for a batch, etc.  This method is
        invoked after a batch has been fully prepared for insertion to the
        database, but before the push to the database occurs.

        Note that the return value of this function matters; if it is boolean
        false then the batch will not be persisted at all, and the user will be
        redirected to the "create batch" page.
        """
        return True

    def redirect_after_create(self, batch):
        if self.handler.requires_prefill(batch):
            return self.redirect(self.get_action_url('prefill', batch))
        elif self.refresh_after_create:
            return self.redirect(self.get_action_url('refresh', batch))
        else:
            return self.redirect(self.get_action_url('view', batch))

    # TODO: some of this at least can go to master now right?
    def edit(self):
        """
        Don't allow editing a batch which has already been executed.
        """
        self.editing = True
        batch = self.get_instance()
        if batch.executed:
            return self.redirect(self.get_action_url('view', batch))

        if self.edit_with_rows:
            grid = self.make_row_grid(batch=batch)

            # If user just refreshed the page with a reset instruction, issue a
            # redirect in order to clear out the query string.
            if self.request.GET.get('reset-to-default-filters') == 'true':
                return self.redirect(self.request.current_route_url(_query=None))

            if self.request.params.get('partial'):
                self.request.response.content_type = b'text/html'
                self.request.response.text = grid.render_grid()
                return self.request.response

        form = self.make_form(batch)
        if self.request.method == 'POST':
            if form.validate():
                self.save_edit_form(form)
                self.request.session.flash("{} has been updated: {}".format(
                    self.get_model_title(), self.get_instance_title(batch)))
                return self.redirect_after_edit(batch)

        context = {
            'instance': batch,
            'instance_title': self.get_instance_title(batch),
            'instance_deletable': self.deletable_instance(batch),
            'form': form,
            'batch': batch,
            'execute_title': self.get_execute_title(batch),
            'execute_enabled': self.executable(batch),
        }

        if self.edit_with_rows:
            context['rows_grid'] = grid
        if context['execute_enabled'] and self.has_execution_options:
            context['rendered_execution_options'] = self.render_execution_options(batch)

        return self.render_to_response('edit', context)

    def rows_creatable_for(self, batch):
        """
        Only allow creating new rows on a batch if it hasn't yet been executed.
        """
        return not batch.executed

    def create_row(self):
        """
        Only allow creating a new row if the batch hasn't yet been executed.
        """
        batch = self.get_instance()
        if batch.executed:
            self.request.session.flash("You cannot add new rows to a batch which has been executed")
            return self.redirect(self.get_action_url('view', batch))
        return super(BatchMasterView, self).create_row()

    def make_default_row_grid_tools(self, batch):
        if self.rows_creatable and not batch.executed:
            permission_prefix = self.get_permission_prefix()
            if self.request.has_perm('{}.create_row'.format(permission_prefix)):
                link = tags.link_to("Create a new {}".format(self.get_row_model_title()),
                                    self.get_action_url('create_row', batch))
                return HTML.tag('p', c=link)

    def make_batch_row_grid_tools(self, batch):
        if not batch.executed and self.request.has_perm('{}.edit'.format(self.get_permission_prefix())):
            url = self.request.route_url('{}.delete_rows'.format(self.get_route_prefix()), uuid=batch.uuid)
            return HTML.tag('p', c=tags.link_to("Delete all rows matching current search", url))

    def make_row_grid_tools(self, batch):
        return (self.make_default_row_grid_tools(batch) or '') + (self.make_batch_row_grid_tools(batch) or '')

    def redirect_after_edit(self, batch):
        """
        If refresh flag is set, do that; otherwise go (back) to view/edit page.
        """
        if self.request.params.get('refresh') == 'true':
            return self.redirect(self.get_action_url('refresh', batch))
        if self.edit_with_rows:
            return self.redirect(self.get_action_url('edit', batch))
        return self.redirect(self.get_action_url('view', batch))

    def delete_instance(self, batch):
        """
        Delete all data (files etc.) for the batch.
        """
        if hasattr(batch, 'delete_data'):
            batch.delete_data(self.rattail_config)
        del batch.data_rows[:]
        super(BatchMasterView, self).delete_instance(batch)

    def get_fallback_templates(self, template):
        return [
            '/newbatch/{}.mako'.format(template),
            '/master/{}.mako'.format(template),
        ]

    def editable_instance(self, batch):
        return not bool(batch.executed)

    def executable(self, batch):
        return self.handler.executable(batch)

    def batch_refreshable(self, batch):
        """
        Return a boolean indicating whether the given batch should allow a
        refresh operation.
        """
        # TODO: deprecate/remove this?
        if not self.refreshable:
            return False

        # (this is how it should be done i think..)
        if callable(self.handler.refreshable):
            return self.handler.refreshable(batch)

        # TODO: deprecate/remove this
        return self.handler.refreshable and not batch.executed

    @property
    def has_execution_options(self):
        return bool(self.execution_options_schema)

    # TODO
    execution_options_schema = None

    def make_execution_options_form(self, batch):
        """
        Return a proper Form for execution options.
        """
        defaults = {}
        for field in self.execution_options_schema.fields:
            key = 'batch.{}.execute_option.{}'.format(batch.batch_key, field)
            value = self.request.session.get(key)
            if value:
                defaults[field] = value
        return Form(self.request, schema=self.execution_options_schema,
                    defaults=defaults or None)

    def get_execute_title(self, batch):
        if hasattr(self.handler, 'get_execute_title'):
            return self.handler.get_execute_title(batch)
        return "Execute this batch"

    def prefill(self):
        """
        View which will attempt to prefill all data for the batch.  What
        exactly this means will depend on the type of batch etc.
        """
        batch = self.get_instance()
        route_prefix = self.get_route_prefix()
        permission_prefix = self.get_permission_prefix()

        # showing progress requires a separate thread; start that first
        progress_key = '{}.prefill'.format(route_prefix)
        progress = SessionProgress(self.request, progress_key)
        thread = Thread(target=self.prefill_thread, args=(batch.uuid, progress))
        thread.start()

        # Send user to progress page.
        kwargs = {
            'key': progress_key,
            'cancel_url': self.get_action_url('view', batch),
            'cancel_msg': "Batch prefill was canceled.",
        }

        # TODO: This seems hacky...it exists for (only) one specific scenario.
        if not self.request.has_perm('{}.view'.format(permission_prefix)):
            kwargs['cancel_url'] = self.request.route_url('{}.create'.format(route_prefix))

        return self.render_progress(kwargs)

    def prefill_thread(self, batch_uuid, progress):
        """
        Thread target for prefilling batch data with progress indicator.
        """
        # mustn't use tailbone web session here
        session = RattailSession()
        batch = session.query(self.model_class).get(batch_uuid)
        try:
            self.handler.make_initial_rows(batch, progress=progress)
        except Exception as error:
            session.rollback()
            log.warning("batch pre-fill failed: {}".format(batch), exc_info=True)
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = "Batch pre-fill failed: {} {}".format(error.__class__.__name__, error)
                progress.session.save()
            return

        session.commit()
        session.refresh(batch)
        session.close()

        # finalize progress
        if progress:
            progress.session.load()
            progress.session['complete'] = True
            progress.session['success_url'] = self.get_action_url('view', batch)
            progress.session.save()

    def refresh(self):
        """
        View which will attempt to refresh all data for the batch.  What
        exactly this means will depend on the type of batch etc.
        """
        batch = self.get_instance()
        route_prefix = self.get_route_prefix()
        permission_prefix = self.get_permission_prefix()

        # TODO: deprecate / remove this
        cognizer = self.request.user
        if not cognizer:
            uuid = self.request.session.pop('late_login_user', None)
            cognizer = Session.query(model.User).get(uuid) if uuid else None

        # TODO: refresh should probably always imply/use progress
        # If handler doesn't declare the need for progress indicator, things
        # are nice and simple.
        if not getattr(self.handler, 'show_progress', True):
            self.refresh_data(Session, batch, cognizer=cognizer)
            self.request.session.flash("Batch data has been refreshed.")

            # TODO: This seems hacky...it exists for (only) one specific scenario.
            if not self.request.has_perm('{}.view'.format(permission_prefix)):
                return self.redirect(self.request.route_url('{}.create'.format(route_prefix)))

            return self.redirect(self.get_action_url('view', batch))

        # Showing progress requires a separate thread; start that first.
        key = '{}.refresh'.format(self.model_class.__tablename__)
        progress = SessionProgress(self.request, key)
        # success_url = self.request.route_url('vendors.scangenius.create') if not self.request.user else None
        
        # TODO: This seems hacky...it exists for (only) one specific scenario.
        success_url = None
        if not self.request.user:
            success_url = self.request.route_url('{}.create'.format(route_prefix))
            
        thread = Thread(target=self.refresh_thread, args=(batch.uuid, progress,
                                                          cognizer.uuid if cognizer else None,
                                                          success_url))
        thread.start()

        # Send user to progress page.
        kwargs = {
            'key': key,
            'cancel_url': self.get_action_url('view', batch),
            'cancel_msg': "Batch refresh was canceled.",
            }

        # TODO: This seems hacky...it exists for (only) one specific scenario.
        if not self.request.has_perm('{}.view'.format(permission_prefix)):
            kwargs['cancel_url'] = self.request.route_url('{}.create'.format(route_prefix))

        return self.render_progress(kwargs)

    def refresh_data(self, session, batch, cognizer=None, progress=None):
        """
        Instruct the batch handler to refresh all data for the batch.
        """
        # TODO: deprecate/remove this
        if hasattr(self.handler, 'refresh_data'):
            self.handler.refresh_data(session, batch, progress=progress)
            batch.cognized = datetime.datetime.utcnow()
            batch.cognized_by = cognizer or session.merge(self.request.user)

        else: # the future
            self.handler.refresh(batch, progress=progress)

    def refresh_thread(self, batch_uuid, progress=None, cognizer_uuid=None, success_url=None):
        """
        Thread target for refreshing batch data with progress indicator.
        """
        # Refresh data for the batch, with progress.  Note that we must use the
        # rattail session here; can't use tailbone because it has web request
        # transaction binding etc.
        session = RattailSession()
        batch = session.query(self.model_class).get(batch_uuid)
        cognizer = session.query(model.User).get(cognizer_uuid) if cognizer_uuid else None
        try:
            self.refresh_data(session, batch, cognizer=cognizer, progress=progress)
        except Exception as error:
            session.rollback()
            log.warning("refreshing data for batch failed: {}".format(batch), exc_info=True)
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = "Data refresh failed: {} {}".format(error.__class__.__name__, error)
                progress.session.save()
            return

        session.commit()
        session.refresh(batch)
        session.close()

        # Finalize progress indicator.
        if progress:
            progress.session.load()
            progress.session['complete'] = True
            progress.session['success_url'] = success_url or self.get_action_url('view', batch)
            progress.session.save()

    ########################################
    # batch rows
    ########################################

    def get_row_instance_title(self, row):
        return "Row {}".format(row.sequence)

    def _preconfigure_row_grid(self, g):

        g.filters['status_code'].label = "Status"
        g.filters['status_code'].set_value_renderer(grids.filters.EnumValueRenderer(self.model_row_class.STATUS))

        g.default_sortkey = 'sequence'

        g.sequence.set(label="Seq.")
        g.status_code.set(label="Status",
                          renderer=StatusRenderer(self.model_row_class.STATUS))

    def get_row_data(self, batch):
        """
        Generate the base data set for a rows grid.
        """
        return self.Session.query(self.model_row_class)\
                      .filter(self.model_row_class.batch == batch)\
                      .filter(self.model_row_class.removed == False)

    def row_editable(self, row):
        """
        Batch rows are editable only until batch has been executed.
        """
        return self.rows_editable and not row.batch.executed

    def row_edit_action_url(self, row, i):
        if self.row_editable(row):
            return self.get_row_action_url('edit', row)

    def row_deletable(self, row):
        """
        Batch rows are deletable only until batch has been executed.
        """
        return self.rows_deletable and not row.batch.executed

    def row_delete_action_url(self, row, i):
        if self.row_deletable(row):
            return self.get_row_action_url('delete', row)

    def _preconfigure_row_fieldset(self, fs):
        fs.sequence.set(readonly=True)
        fs.status_code.set(renderer=StatusRenderer(self.model_row_class.STATUS),
                           label="Status", readonly=True)
        fs.status_text.set(readonly=True)
        fs.removed.set(readonly=True)
        try:
            fs.product.set(readonly=True, renderer=forms.renderers.ProductFieldRenderer)
        except AttributeError:
            pass

    def configure_row_fieldset(self, fs):
        fs.configure()
        del fs.batch

    def template_kwargs_view_row(self, **kwargs):
        kwargs['batch_model_title'] = kwargs['parent_model_title']
        return kwargs

    def get_parent(self, row):
        return row.batch

    def delete_row(self):
        """
        "Delete" a row from the batch.  This sets the ``removed`` flag on the
        row but does not truly delete it.
        """
        row = self.Session.query(self.model_row_class).get(self.request.matchdict['uuid'])
        if not row:
            raise httpexceptions.HTTPNotFound()
        row.removed = True
        return self.redirect(self.get_action_url('view', self.get_parent(row)))

    def bulk_delete_rows(self):
        """
        "Delete" all rows matching the current row grid view query.  This sets
        the ``removed`` flag on the rows but does not truly delete them.
        """
        query = self.get_effective_row_query()
        query.update({'removed': True}, synchronize_session=False)
        return self.redirect(self.get_action_url('view', self.get_instance()))

    def execute(self):
        """
        Execute a batch.  Starts a separate thread for the execution, and
        displays a progress indicator page.
        """
        batch = self.get_instance()
        if self.request.method == 'POST':

            kwargs = {}
            if self.has_execution_options:
                form = self.make_execution_options_form(batch)
                assert form.validate() # TODO
                kwargs.update(form.data)
                for key, value in form.data.iteritems():
                    # TODO: properly serialize option values?
                    self.request.session['batch.{}.execute_option.{}'.format(batch.batch_key, key)] = unicode(value)

            key = '{}.execute'.format(self.model_class.__tablename__)
            kwargs['progress'] = SessionProgress(self.request, key)
            thread = Thread(target=self.execute_thread, args=(batch.uuid, self.request.user.uuid), kwargs=kwargs)
            thread.start()

            return self.render_progress({
                'key': key,
                'cancel_url': self.get_action_url('view', batch),
                'cancel_msg': "Batch execution was canceled.",
            })

        self.request.session.flash("Sorry, you must POST to execute a batch.", 'error')
        return self.redirect(self.get_action_url('view', batch))

    def execute_thread(self, batch_uuid, user_uuid, progress=None, **kwargs):
        """
        Thread target for executing a batch with progress indicator.
        """
        # Execute the batch, with progress.  Note that we must use the rattail
        # session here; can't use tailbone because it has web request
        # transaction binding etc.
        session = RattailSession()
        batch = session.query(self.model_class).get(batch_uuid)
        user = session.query(model.User).get(user_uuid)
        try:
            result = self.handler.execute(batch, user=user, progress=progress, **kwargs)

        # If anything goes wrong, rollback and log the error etc.
        except Exception as error:
            session.rollback()
            log.exception("execution failed for batch: {}".format(batch))
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = "Batch execution failed: {}: {}".format(type(error).__name__, error)
                progress.session.save()

        # If no error, check result flag (false means user canceled).
        else:
            if result:
                batch.executed = datetime.datetime.utcnow()
                batch.executed_by = user
                session.commit()
                # TODO: this doesn't always work...?
                self.request.session.flash("{} has been executed: {}".format(
                    self.get_model_title(), batch.id_str))
            else:
                session.rollback()

            session.refresh(batch)
            success_url = self.get_execute_success_url(batch, result, **kwargs)
            session.close()

            if progress:
                progress.session.load()
                progress.session['complete'] = True
                progress.session['success_url'] = success_url
                progress.session.save()

    def get_execute_success_url(self, batch, result, **kwargs):
        return self.get_action_url('view', batch)

    def csv(self):
        """
        Download batch data as CSV.
        """
        batch = self.get_instance()
        fields = self.get_csv_fields()
        data = StringIO()
        writer = UnicodeDictWriter(data, fields)
        writer.writeheader()
        for row in batch.data_rows:
            if not row.removed:
                writer.writerow(self.get_csv_row(row, fields))
        response = self.request.response
        response.text = data.getvalue().decode('utf_8')
        data.close()
        response.content_length = len(response.text)
        response.content_type = b'text/csv'
        response.content_disposition = b'attachment; filename=batch.csv'
        return response

    def get_csv_fields(self):
        """
        Return the list of fields to be written to CSV download.
        """
        fields = []
        mapper = orm.class_mapper(self.model_row_class)
        for prop in mapper.iterate_properties:
            if isinstance(prop, orm.ColumnProperty):
                if prop.key != 'removed' and not prop.key.endswith('uuid'):
                    fields.append(prop.key)
        return fields

    def get_csv_row(self, row, fields):
        """
        Return a dict for use when writing the row's data to CSV download.
        """
        csvrow = {}
        for field in fields:
            value = getattr(row, field)
            csvrow[field] = '' if value is None else unicode(value)
        return csvrow

    @classmethod
    def defaults(cls, config):
        cls._batch_defaults(config)
        cls._defaults(config)

    @classmethod
    def _batch_defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        url_prefix = cls.get_url_prefix()
        permission_prefix = cls.get_permission_prefix()
        model_title = cls.get_model_title()
        model_title_plural = cls.get_model_title_plural()

        # TODO: currently must do this here (in addition to `_defaults()` or
        # else the perm group label will not display correctly...
        config.add_tailbone_permission_group(permission_prefix, model_title_plural, overwrite=False)

        # prefill row data
        config.add_route('{}.prefill'.format(route_prefix), '{}/{{uuid}}/prefill'.format(url_prefix))
        config.add_view(cls, attr='prefill', route_name='{}.prefill'.format(route_prefix),
                        permission='{}.create'.format(permission_prefix))

        # refresh batch data
        config.add_route('{}.refresh'.format(route_prefix), '{}/{{uuid}}/refresh'.format(url_prefix))
        config.add_view(cls, attr='refresh', route_name='{}.refresh'.format(route_prefix),
                        permission='{}.refresh'.format(permission_prefix))
        config.add_tailbone_permission(permission_prefix, '{}.refresh'.format(permission_prefix),
                                       "Refresh data for {}".format(model_title))

        # bulk delete rows
        config.add_route('{}.delete_rows'.format(route_prefix), '{}/{{uuid}}/rows/delete'.format(url_prefix))
        config.add_view(cls, attr='bulk_delete_rows', route_name='{}.delete_rows'.format(route_prefix),
                        permission='{}.edit'.format(permission_prefix))

        # execute batch
        config.add_route('{}.execute'.format(route_prefix), '{}/{{uuid}}/execute'.format(url_prefix))
        config.add_view(cls, attr='execute', route_name='{}.execute'.format(route_prefix),
                        permission='{}.execute'.format(permission_prefix))
        config.add_tailbone_permission(permission_prefix, '{}.execute'.format(permission_prefix),
                                       "Execute {}".format(model_title))

        # download rows as CSV
        if cls.rows_downloadable:
            config.add_route('{}.csv'.format(route_prefix), '{}/{{uuid}}/csv'.format(url_prefix))
            config.add_view(cls, attr='csv', route_name='{}.csv'.format(route_prefix),
                            permission='{}.csv'.format(permission_prefix))
            config.add_tailbone_permission(permission_prefix, '{}.csv'.format(permission_prefix),
                                           "Download {} rows as CSV".format(model_title))


class FileBatchMasterView(BatchMasterView):
    """
    Base class for all file-based "batch master" views.
    """

    @property
    def upload_dir(self):
        """
        The path to the root upload folder, to be used as the ``storage_path``
        argument for the file field renderer.
        """
        uploads = os.path.join(
            self.rattail_config.require('rattail', 'batch.files'),
            'uploads')
        uploads = self.rattail_config.get('tailbone', 'batch.uploads',
                                          default=uploads)
        if not os.path.exists(uploads):
            os.makedirs(uploads)
        return uploads

    def preconfigure_grid(self, g):
        super(FileBatchMasterView, self).preconfigure_grid(g)
        g.created.set(label="Uploaded")
        g.created_by.set(label="Uploaded by")

    def _preconfigure_fieldset(self, fs):
        super(FileBatchMasterView, self)._preconfigure_fieldset(fs)
        fs.created.set(label="Uploaded")
        fs.created_by.set(label="Uploaded by")
        fs.filename.set(label="Data File", renderer=FileFieldRenderer.new(self))
        if self.editing:
            fs.filename.set(readonly=True)

    def configure_fieldset(self, fs):
        """
        Apply final configuration to the main batch fieldset.  Custom batch
        views are encouraged to override this method.
        """
        if self.creating:
            fs.configure(
                include=[
                    fs.filename,
                ])

        else:
            batch = fs.model
            if batch.executed:
                fs.configure(
                    include=[
                        fs.id,
                        fs.created,
                        fs.created_by,
                        fs.filename,
                        fs.executed,
                        fs.executed_by,
                    ])
            else:
                fs.configure(
                    include=[
                        fs.id,
                        fs.created,
                        fs.created_by,
                        fs.filename,
                    ])

    def download(self):
        """
        View for downloading the data file associated with a batch.
        """
        batch = self.get_instance()
        if not batch:
            raise httpexceptions.HTTPNotFound()
        path = batch.filepath(self.rattail_config)
        response = FileResponse(path, request=self.request)
        response.headers[b'Content-Length'] = str(os.path.getsize(path))
        filename = os.path.basename(batch.filename).encode('ascii', 'replace')
        response.headers[b'Content-Disposition'] = b'attachment; filename="{}"'.format(filename)
        return response

    @classmethod
    def defaults(cls, config):
        cls._filebatch_defaults(config)
        cls._batch_defaults(config)
        cls._defaults(config)

    @classmethod
    def _filebatch_defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        url_prefix = cls.get_url_prefix()
        permission_prefix = cls.get_permission_prefix()
        model_title = cls.get_model_title()
        model_title_plural = cls.get_model_title_plural()

        # fix permission group title
        config.add_tailbone_permission_group(permission_prefix, model_title_plural)

        # download batch data file
        config.add_route('{}.download'.format(route_prefix), '{}/{{uuid}}/download'.format(url_prefix))
        config.add_view(cls, attr='download', route_name='{}.download'.format(route_prefix),
                        permission='{}.download'.format(permission_prefix))
        config.add_tailbone_permission(permission_prefix, '{}.download'.format(permission_prefix),
                                       "Download existing {} data file".format(model_title))


class BaseGrid(SearchableAlchemyGridView):
    """
    Base view for batch and batch row grid views.  You should not derive from
    this class, but :class:`BatchGrid` or :class:`BatchRowGrid` instead.
    """

    @property
    def config_prefix(self):
        """
        Config prefix for the grid view.  This is used to keep track of current
        filtering and sorting, within the user's session.  Derived classes may
        override this.
        """
        return self.mapped_class.__name__.lower()

    @property
    def permission_prefix(self):
        """
        Permission prefix for the grid view.  This is used to automatically
        protect certain views common to all batches.  Derived classes can
        override this.
        """
        return self.route_prefix

    def join_map_extras(self):
        """
        Derived classes can override this.  The value returned will be used to
        supplement the default join map.
        """
        return {}

    def filter_map_extras(self):
        """
        Derived classes can override this.  The value returned will be used to
        supplement the default filter map.
        """
        return {}

    def make_filter_map(self, **kwargs):
        """
        Make a filter map by combining kwargs from the base class, with extras
        supplied by a derived class.
        """
        extras = self.filter_map_extras()
        exact = extras.pop('exact', None)
        if exact:
            kwargs.setdefault('exact', []).extend(exact)
        ilike = extras.pop('ilike', None)
        if ilike:
            kwargs.setdefault('ilike', []).extend(ilike)
        kwargs.update(extras)
        return super(BaseGrid, self).make_filter_map(**kwargs)

    def filter_config_extras(self):
        """
        Derived classes can override this.  The value returned will be used to
        supplement the default filter config.
        """
        return {}

    def sort_map_extras(self):
        """
        Derived classes can override this.  The value returned will be used to
        supplement the default sort map.
        """
        return {}

    def _configure_grid(self, grid):
        """
        Internal method for configuring the grid.  This is meant only for base
        classes; derived classes should not need to override it.
        """

    def configure_grid(self, grid):
        """
        Derived classes can override this.  Customizes a grid which has already
        been created with defaults by the base class.
        """


class BatchGrid(BaseGrid):
    """
    Base grid view for batches, which can be filtered and sorted.
    """

    @property
    def batch_class(self):
        raise NotImplementedError

    @property
    def mapped_class(self):
        return self.batch_class

    @property
    def batch_display(self):
        """
        Singular display text for the batch type, e.g. "Vendor Invoice".
        Override this as necessary.
        """
        return self.batch_class.__name__

    @property
    def batch_display_plural(self):
        """
        Plural display text for the batch type, e.g. "Vendor Invoices".
        Override this as necessary.
        """
        return "{0}s".format(self.batch_display)

    def join_map(self):
        """
        Provides the default join map for batch grid views.  Derived classes
        should *not* override this, but :meth:`join_map_extras()` instead.
        """
        map_ = {
            'created_by':
                lambda q: q.join(model.User, model.User.uuid == self.batch_class.created_by_uuid),
            'executed_by':
                lambda q: q.outerjoin(model.User, model.User.uuid == self.batch_class.executed_by_uuid),
            }
        map_.update(self.join_map_extras())
        return map_

    def filter_map(self):
        """
        Provides the default filter map for batch grid views.  Derived classes
        should *not* override this, but :meth:`filter_map_extras()` instead.
        """

        def executed_is(q, v):
            if v == 'True':
                return q.filter(self.batch_class.executed != None)
            else:
                return q.filter(self.batch_class.executed == None)

        def executed_nt(q, v):
            if v == 'True':
                return q.filter(self.batch_class.executed == None)
            else:
                return q.filter(self.batch_class.executed != None)

        return self.make_filter_map(
            executed={'is': executed_is, 'nt': executed_nt})

    def filter_config(self):
        """
        Provides the default filter config for batch grid views.  Derived
        classes should *not* override this, but :meth:`filter_config_extras()`
        instead.
        """
        defaults = self.filter_config_extras()
        config = self.make_filter_config(
            filter_factory_executed=BooleanSearchFilter,
            filter_type_executed='is',
            executed=False,
            include_filter_executed=True)
        defaults.update(config)
        return defaults

    def sort_map(self):
        """
        Provides the default sort map for batch grid views.  Derived classes
        should *not* override this, but :meth:`sort_map_extras()` instead.
        """
        map_ = self.make_sort_map(
            created_by=self.sorter(model.User.username),
            executed_by=self.sorter(model.User.username))
        map_.update(self.sort_map_extras())
        return map_

    def sort_config(self):
        """
        Provides the default sort config for batch grid views.  Derived classes
        may override this.
        """
        return self.make_sort_config(sort='created', dir='desc')

    def grid(self):
        """
        Creates the grid for the view.  Derived classes should *not* override
        this, but :meth:`configure_grid()` instead.
        """
        g = self.make_grid()
        g.created_by.set(renderer=forms.renderers.UserFieldRenderer)
        g.cognized_by.set(renderer=forms.renderers.UserFieldRenderer)
        g.executed_by.set(renderer=forms.renderers.UserFieldRenderer)
        self._configure_grid(g)
        self.configure_grid(g)
        if self.request.has_perm('{0}.view'.format(self.permission_prefix)):
            g.viewable = True
            g.view_route_name = '{0}.view'.format(self.route_prefix)
        if self.request.has_perm('{0}.edit'.format(self.permission_prefix)):
            g.editable = True
            g.edit_route_name = '{0}.edit'.format(self.route_prefix)
        if self.request.has_perm('{0}.delete'.format(self.permission_prefix)):
            g.deletable = True
            g.delete_route_name = '{0}.delete'.format(self.route_prefix)
        return g

    def _configure_grid(self, grid):
        grid.created_by.set(label="Created by")
        grid.executed_by.set(label="Executed by")

    def configure_grid(self, grid):
        """
        Derived classes can override this.  Customizes a grid which has already
        been created with defaults by the base class.
        """
        g = grid
        g.configure(
            include=[
                g.created,
                g.created_by,
                g.executed,
                g.executed_by,
                ],
            readonly=True)

    def render_kwargs(self):
        """
        Add some things to the template context: batch type display name, route
        and permission prefixes.
        """
        return {
            'batch_display': self.batch_display,
            'batch_display_plural': self.batch_display_plural,
            'route_prefix': self.route_prefix,
            'permission_prefix': self.permission_prefix,
            }


class FileBatchGrid(BatchGrid):
    """
    Base grid view for batches, which involve primarily a file upload.
    """

    def _configure_grid(self, g):
        super(FileBatchGrid, self)._configure_grid(g)
        g.created.set(label="Uploaded")
        g.created_by.set(label="Uploaded by")

    def configure_grid(self, grid):
        """
        Derived classes can override this.  Customizes a grid which has already
        been created with defaults by the base class.
        """
        g = grid
        g.configure(
            include=[
                g.created,
                g.created_by,
                g.filename,
                g.executed,
                g.executed_by,
                ],
            readonly=True)


class BaseCrud(CrudView):
    """
    Base CRUD view for batches and batch rows.
    """
    flash = {}

    @property
    def home_route(self):
        """
        The "home" route for the batch type, i.e. its grid view.
        """
        return self.route_prefix

    @property
    def permission_prefix(self):
        """
        Permission prefix used to generically protect certain views common to
        all batches.  Derived classes can override this.
        """
        return self.route_prefix

    def flash_create(self, model):
        if 'create' in self.flash:
            self.request.session.flash(self.flash['create'])
        else:
            super(BaseCrud, self).flash_create(model)

    def flash_update(self, model):
        if 'update' in self.flash:
            self.request.session.flash(self.flash['update'])
        else:
            super(BaseCrud, self).flash_update(model)

    def flash_delete(self, model):
        if 'delete' in self.flash:
            self.request.session.flash(self.flash['delete'])
        else:
            super(BaseCrud, self).flash_delete(model)


class BatchCrud(BaseCrud):
    """
    Base CRUD view for batches.
    """
    refreshable = False
    flash = {}

    @property
    def batch_class(self):
        raise NotImplementedError

    @property
    def batch_row_class(self):
        raise NotImplementedError

    @property
    def mapped_class(self):
        return self.batch_class

    @classmethod
    def get_route_prefix(cls):
        return cls.route_prefix

    @property
    def permission_prefix(self):
        """
        Permission prefix for the grid view.  This is used to automatically
        protect certain views common to all batches.  Derived classes can - and
        typically should - override this.
        """
        return self.route_prefix

    @property
    def batch_display_plural(self):
        """
        Plural display text for the batch type.
        """
        return "{0}s".format(self.batch_display)

    def __init__(self, request):
        self.request = request
        self.handler = self.get_handler()

    def get_handler(self):
        """
        Returns a `BatchHandler` instance for the view.  Derived classes may
        override this as needed.  The default is to create an instance of
        :attr:`batch_handler_class`.
        """
        return self.batch_handler_class(self.request.rattail_config)

    def fieldset(self, model):
        """
        Creates the fieldset for the view.  Derived classes should *not*
        override this, but :meth:`configure_fieldset()` instead.
        """
        fs = self.make_fieldset(model)
        fs.created.set(readonly=True)
        fs.created_by.set(label="Created by", renderer=forms.renderers.UserFieldRenderer,
                          readonly=True)
        fs.cognized_by.set(label="Cognized by", renderer=forms.renderers.UserFieldRenderer)
        fs.executed_by.set(label="Executed by", renderer=forms.renderers.UserFieldRenderer)
        self.configure_fieldset(fs)
        if self.creating:
            del fs.created
            del fs.created_by
            if 'cognized' in fs.render_fields:
                del fs.cognized
            if 'cognized_by' in fs.render_fields:
                del fs.cognized_by
            if 'executed' in fs.render_fields:
                del fs.executed
            if 'executed_by' in fs.render_fields:
                del fs.executed_by
        else:
            batch = fs.model
            if not batch.executed:
                if 'executed' in fs.render_fields:
                    del fs.executed
                if 'executed_by' in fs.render_fields:
                    del fs.executed_by
        return fs

    def configure_fieldset(self, fieldset):
        """
        Derived classes can override this.  Customizes a fieldset which has
        already been created with defaults by the base class.
        """
        fs = fieldset
        fs.configure(
            include=[
                fs.created,
                fs.created_by,
                # fs.cognized,
                # fs.cognized_by,
                fs.executed,
                fs.executed_by,
                ])

    def init_batch(self, batch):
        """
        Initialize a new batch.  Derived classes can override this to
        effectively provide default values for a batch, etc.  This method is
        invoked after a batch has been fully prepared for insertion to the
        database, but before the push to the database occurs.

        Note that the return value of this function matters; if it is boolean
        false then the batch will not be persisted at all, and the user will be
        redirected to the "create batch" page.
        """
        return True

    def save_form(self, form):
        """
        Save the uploaded data file if necessary, etc.  If batch initialization
        fails, don't persist the batch at all; the user will be sent back to
        the "create batch" page in that case.
        """
        # Transfer form data to batch instance.
        form.fieldset.sync()
        batch = form.fieldset.model

        # For new batches, assign current user as creator, etc.
        if self.creating:
            with Session.no_autoflush:
                batch.created_by = self.request.user or self.late_login_user()

            # Expunge batch from session to prevent it from being flushed
            # during init.  This is done as a convenience to views which
            # provide an init method.  Some batches may have required fields
            # which aren't filled in yet, but the view may need to query the
            # database to obtain the values.  This will cause a session flush,
            # and the missing fields will trigger data integrity errors.
            Session.expunge(batch)
            self.batch_inited = self.init_batch(batch)
            if self.batch_inited:
                Session.add(batch)
                Session.flush()

    def update(self):
        """
        Don't allow editing a batch which has already been executed.
        """
        batch = self.get_model_from_request()
        if not batch:
            raise httpexceptions.HTTPNotFound()
        if batch.executed:
            raise httpexceptions.HTTPFound(location=self.view_url(batch.uuid))
        return self.crud(batch)

    def post_create_url(self, form):
        """
        Redirect to view batch after creating a batch.
        """
        batch = form.fieldset.model
        Session.flush()
        return self.view_url(batch.uuid)

    def post_update_url(self, form):
        """
        Redirect back to edit batch page after editing a batch, unless the
        refresh flag is set, in which case do that.
        """
        if self.request.params.get('refresh') == 'true':
            return self.refresh_url()
        return self.request.current_route_url()

    def template_kwargs(self, form):
        """
        Add some things to the template context: current batch model, batch
        type display name, route and permission prefixes, batch row grid.
        """
        batch = form.fieldset.model
        batch.refreshable = self.refreshable
        kwargs = {
            'batch': batch,
            'batch_display': self.batch_display,
            'batch_display_plural': self.batch_display_plural,
            'execute_title': self.handler.get_execute_title(batch),
            'route_prefix': self.route_prefix,
            'permission_prefix': self.permission_prefix,
            }
        if not self.creating:
            kwargs['execute_enabled'] = self.executable(batch)
        return kwargs

    def executable(self, batch):
        return self.handler.executable(batch)

    def flash_create(self, batch):
        if 'create' in self.flash:
            self.request.session.flash(self.flash['create'])
        else:
            super(BatchCrud, self).flash_create(batch)

    def flash_delete(self, batch):
        if 'delete' in self.flash:
            self.request.session.flash(self.flash['delete'])
        else:
            super(BatchCrud, self).flash_delete(batch)

    def current_batch(self):
        """
        Return the current batch, based on the UUID within the URL.
        """
        return Session.query(self.mapped_class).get(self.request.matchdict['uuid'])

    def refresh(self):
        """
        View which will attempt to refresh all data for the batch.  What
        exactly this means will depend on the type of batch etc.
        """
        batch = self.current_batch()

        # If handler doesn't declare the need for progress indicator, things
        # are nice and simple.
        if not self.handler.show_progress:
            self.refresh_data(Session, batch)
            self.request.session.flash("Batch data has been refreshed.")
            raise httpexceptions.HTTPFound(location=self.view_url(batch.uuid))

        # Showing progress requires a separate thread; start that first.
        key = '{0}.refresh'.format(self.batch_class.__tablename__)
        progress = SessionProgress(self.request, key)
        thread = Thread(target=self.refresh_thread, args=(batch.uuid, progress))
        thread.start()

        # Send user to progress page.
        kwargs = {
            'key': key,
            'cancel_url': self.view_url(batch.uuid),
            'cancel_msg': "Batch refresh was canceled.",
            }
        return self.render_progress(kwargs)

    def refresh_data(self, session, batch, cognizer=None, progress=None):
        """
        Instruct the batch handler to refresh all data for the batch.
        """
        self.handler.refresh_data(session, batch, progress=progress)
        batch.cognized = datetime.datetime.utcnow()
        if cognizer is not None:
            batch.cognized_by = cognizer
        else:
            batch.cognized_by = session.merge(self.request.user)

    def refresh_thread(self, batch_uuid, progress=None, cognizer_uuid=None, success_url=None):
        """
        Thread target for refreshing batch data with progress indicator.
        """
        # Refresh data for the batch, with progress.  Note that we must use the
        # rattail session here; can't use tailbone because it has web request
        # transaction binding etc.
        session = RattailSession()
        batch = session.query(self.batch_class).get(batch_uuid)
        cognizer = session.query(model.User).get(cognizer_uuid) if cognizer_uuid else None
        try:
            self.refresh_data(session, batch, cognizer=cognizer, progress=progress)
        except Exception as error:
            session.rollback()
            log.warning("refreshing data for batch failed: {0}".format(batch), exc_info=True)
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = "Data refresh failed: {0}".format(error)
                progress.session.save()
            return

        session.commit()
        session.refresh(batch)
        session.close()

        # Finalize progress indicator.
        if progress:
            progress.session.load()
            progress.session['complete'] = True
            progress.session['success_url'] = success_url or self.view_url(batch.uuid)
            progress.session.save()
        
    def view_url(self, uuid=None):
        """
        Returns the URL for viewing a batch; defaults to current batch.
        """
        if uuid is None:
            uuid = self.request.matchdict['uuid']
        return self.request.route_url('{0}.view'.format(self.route_prefix), uuid=uuid)

    def refresh_url(self, uuid=None):
        """
        Returns the URL for refreshing a batch; defaults to current batch.
        """
        if uuid is None:
            uuid = self.request.matchdict['uuid']
        return self.request.route_url('{0}.refresh'.format(self.route_prefix), uuid=uuid)

    def execute(self):
        """
        Execute a batch.  Starts a separate thread for the execution, and
        displays a progress indicator page.
        """
        batch = self.current_batch()

        key = '{0}.execute'.format(self.batch_class.__tablename__)
        progress = SessionProgress(self.request, key)
        thread = Thread(target=self.execute_thread, args=(batch.uuid, progress))
        thread.start()

        kwargs = {
            'key': key,
            'cancel_url': self.view_url(batch.uuid),
            'cancel_msg': "Batch execution was canceled.",
            }
        return self.render_progress(kwargs)

    def execute_thread(self, batch_uuid, progress=None):
        """
        Thread target for executing a batch with progress indicator.
        """
        # Execute the batch, with progress.  Note that we must use the rattail
        # session here; can't use tailbone because it has web request
        # transaction binding etc.
        session = RattailSession()
        batch = session.query(self.batch_class).get(batch_uuid)
        try:
            result = self.handler.execute(batch, progress=progress)

        # If anything goes wrong, rollback and log the error etc.
        except Exception as error:
            session.rollback()
            log.exception("execution failed for batch: {0}".format(batch))
            session.close()
            if progress:
                progress.session.load()
                progress.session['error'] = True
                progress.session['error_msg'] = "Batch execution failed: {0}".format(error)
                progress.session.save()

        # If no error, check result flag (false means user canceled).
        else:
            if result:
                batch.executed = datetime.datetime.utcnow()
                batch.executed_by = session.merge(self.request.user)
                session.commit()
            else:
                session.rollback()
            session.refresh(batch)
            session.close()

            if progress:
                progress.session.load()
                progress.session['complete'] = True
                progress.session['success_url'] = self.view_url(batch.uuid)
                progress.session.save()
        
    def csv(self):
        """
        Download batch data as CSV.
        """
        batch = self.current_batch()
        fields = self.get_csv_fields()
        data = StringIO()
        writer = UnicodeDictWriter(data, fields)
        writer.writeheader()
        for row in batch.data_rows:
            if not row.removed:
                writer.writerow(self.get_csv_row(row, fields))
        response = self.request.response
        response.text = data.getvalue().decode('utf_8')
        data.close()
        response.content_length = len(response.text)
        response.content_type = b'text/csv'
        response.content_disposition = b'attachment; filename=batch.csv'
        return response

    def get_csv_fields(self):
        """
        Return the list of fields to be written to CSV download.
        """
        fields = []
        mapper = orm.class_mapper(self.batch_row_class)
        for prop in mapper.iterate_properties:
            if isinstance(prop, orm.ColumnProperty):
                if prop.key != 'removed' and not prop.key.endswith('uuid'):
                    fields.append(prop.key)
        return fields

    def get_csv_row(self, row, fields):
        """
        Return a dict for use when writing the row's data to CSV download.
        """
        csvrow = {}
        for field in fields:
            value = getattr(row, field)
            csvrow[field] = '' if value is None else unicode(value)
        return csvrow


class FileBatchCrud(BatchCrud):
    """
    Base CRUD view for batches which involve a file upload as the first step.
    """
    refreshable = True

    def post_create_url(self, form):
        """
        Redirect to refresh batch after creating a batch.
        """
        batch = form.fieldset.model
        Session.flush()
        return self.refresh_url(batch.uuid)

    @property
    def upload_dir(self):
        """
        The path to the root upload folder, to be used as the ``storage_path``
        argument for the file field renderer.
        """
        uploads = os.path.join(
            self.request.rattail_config.require('rattail', 'batch.files'),
            'uploads')
        uploads = self.request.rattail_config.get(
            'tailbone', 'batch.uploads', default=uploads)
        if not os.path.exists(uploads):
            os.makedirs(uploads)
        return uploads

    def fieldset(self, model):
        """
        Creates the fieldset for the view.  Derived classes should *not*
        override this, but :meth:`configure_fieldset()` instead.
        """
        fs = self.make_fieldset(model)
        fs.created.set(label="Uploaded", readonly=True)
        fs.created_by.set(label="Uploaded by", renderer=forms.renderers.UserFieldRenderer, readonly=True)
        fs.cognized_by.set(label="Cognized by", renderer=forms.renderers.UserFieldRenderer)
        fs.executed_by.set(label="Executed by", renderer=forms.renderers.UserFieldRenderer)
        fs.filename.set(renderer=FileFieldRenderer.new(self), label="Data File")
        self.configure_fieldset(fs)
        if self.creating:
            if 'created' in fs.render_fields:
                del fs.created
            if 'created_by' in fs.render_fields:
                del fs.created_by
            if 'cognized' in fs.render_fields:
                del fs.cognized
            if 'cognized_by' in fs.render_fields:
                del fs.cognized_by
            if 'executed' in fs.render_fields:
                del fs.executed
            if 'executed_by' in fs.render_fields:
                del fs.executed_by
            if 'data_rows' in fs.render_fields:
                del fs.data_rows
        else:
            if self.updating and 'filename' in fs.render_fields:
                fs.filename.set(readonly=True)
            batch = fs.model
            if not batch.executed:
                if 'executed' in fs.render_fields:
                    del fs.executed
                if 'executed_by' in fs.render_fields:
                    del fs.executed_by
        return fs

    def configure_fieldset(self, fieldset):
        """
        Derived classes can override this.  Customizes a fieldset which has
        already been created with defaults by the base class.
        """
        fs = fieldset
        fs.configure(
            include=[
                fs.created,
                fs.created_by,
                fs.filename,
                # fs.cognized,
                # fs.cognized_by,
                fs.executed,
                fs.executed_by,
                ])

    def save_form(self, form):
        """
        Save the uploaded data file if necessary, etc.  If batch initialization
        fails, don't persist the batch at all; the user will be sent back to
        the "create batch" page in that case.
        """
        # Transfer form data to batch instance.
        form.fieldset.sync()
        batch = form.fieldset.model

        # For new batches, assign current user as creator, save file etc.
        if self.creating:
            with Session.no_autoflush:
                batch.created_by = self.request.user or self.late_login_user()

            # Expunge batch from session to prevent it from being flushed
            # during init.  This is done as a convenience to views which
            # provide an init method.  Some batches may have required fields
            # which aren't filled in yet, but the view may need to query the
            # database to obtain the values.  This will cause a session flush,
            # and the missing fields will trigger data integrity errors.
            Session.expunge(batch)
            self.batch_inited = self.init_batch(batch)
            if self.batch_inited:
                Session.add(batch)
                Session.flush()

                # Handler saves a copy of the file and updates the batch filename.
                path = os.path.join(self.upload_dir, batch.filename)
                self.handler.set_data_file(batch, path)
                os.remove(path)

    def post_save(self, form):
        """
        This checks for failed batch initialization when creating a new batch.
        If a failure is detected, the user is redirected to the page for
        creating new batches.  The assumption here is that the
        :meth:`init_batch()` method responsible for indicating the failure will
        have set a flash message for the user with more info.
        """
        if self.creating and not self.batch_inited:
            raise httpexceptions.HTTPFound(location=self.request.route_url(
                '{}.create'.format(self.route_prefix)))

    def pre_delete(self, batch):
        """
        Delete all data (files etc.) for the batch.
        """
        batch.delete_data(self.request.rattail_config)
        del batch.data_rows[:]

    def download(self):
        """
        View for downloading the data file associated with a batch.
        """
        batch = self.current_batch()
        if not batch:
            raise httpexceptions.HTTPNotFound()
        path = self.handler.data_path(batch)
        response = FileResponse(path, request=self.request)
        response.headers[b'Content-Length'] = str(os.path.getsize(path))
        filename = os.path.basename(batch.filename).encode('ascii', 'replace')
        response.headers[b'Content-Disposition'] = b'attachment; filename="{0}"'.format(filename)
        return response


class StatusRenderer(forms.renderers.EnumFieldRenderer):
    """
    Custom renderer for ``status_code`` fields.  Adds ``status_text`` value as
    title attribute if it exists.
    """

    def render_readonly(self, **kwargs):
        value = self.raw_value
        if value is None:
            return ''
        status_code_text = self.enumeration.get(value, unicode(value))
        row = self.field.parent.model
        if row.status_text:
            return HTML.tag('span', title=row.status_text, c=status_code_text)
        return status_code_text


class BatchRowGrid(BaseGrid):
    """
    Base grid view for batch rows, which can be filtered and sorted.  Also it
    can delete all rows matching the current list view query.
    """

    @property
    def row_class(self):
        raise NotImplementedError

    @property
    def mapped_class(self):
        return self.row_class

    @property
    def config_prefix(self):
        """
        Config prefix for the grid view.  This is used to keep track of current
        filtering and sorting, within the user's session.  Derived classes may
        override this.
        """
        return '{0}.{1}'.format(self.mapped_class.__name__.lower(),
                                self.request.matchdict['uuid'])

    @property
    def batch_class(self):
        """
        Model class of the batch to which the rows belong.
        """
        return self.row_class.__batch_class__

    @property
    def batch_display(self):
        """
        Singular display text for the batch type, e.g. "Vendor Invoice".
        Override this as necessary.
        """
        return self.batch_class.__name__

    def current_batch(self):
        """
        Return the current batch, based on the UUID within the URL.
        """
        return Session.query(self.batch_class).get(self.request.matchdict['uuid'])

    def modify_query(self, q):
        q = super(BatchRowGrid, self).modify_query(q)
        q = q.filter(self.row_class.batch == self.current_batch())
        q = q.filter(self.row_class.removed == False)
        return q

    def join_map(self):
        """
        Provides the default join map for batch row grid views.  Derived
        classes should *not* override this, but :meth:`join_map_extras()`
        instead.
        """
        return self.join_map_extras()

    def filter_map(self):
        """
        Provides the default filter map for batch row grid views.  Derived
        classes should *not* override this, but :meth:`filter_map_extras()`
        instead.
        """
        return self.make_filter_map(exact=['status_code'])

    def filter_config(self):
        """
        Provides the default filter config for batch grid views.  Derived
        classes should *not* override this, but :meth:`filter_config_extras()`
        instead.
        """
        kwargs = {'filter_label_status_code': "Status",
                  'filter_factory_status_code': EnumSearchFilter(self.row_class.STATUS)}
        kwargs.update(self.filter_config_extras())
        return self.make_filter_config(**kwargs)

    def sort_map(self):
        """
        Provides the default sort map for batch grid views.  Derived classes
        should *not* override this, but :meth:`sort_map_extras()` instead.
        """
        map_ = self.make_sort_map()
        map_.update(self.sort_map_extras())
        return map_

    def sort_config(self):
        """
        Provides the default sort config for batch grid views.  Derived classes
        may override this.
        """
        return self.make_sort_config(sort='sequence', dir='asc')

    def grid(self):
        """
        Creates the grid for the view.  Derived classes should *not* override
        this, but :meth:`configure_grid()` instead.
        """
        g = self.make_grid()
        g.extra_row_class = self.tr_class
        g.sequence.set(label="Seq.")
        g.status_code.set(label="Status", renderer=StatusRenderer(self.row_class.STATUS))
        self._configure_grid(g)
        self.configure_grid(g)

        batch = self.current_batch()
        g.viewable = True
        g.view_route_name = '{0}.row.view'.format(self.route_prefix)
        # TODO: Fix this check for edit mode.
        edit_mode = self.request.referrer.endswith('/edit')
        if edit_mode and not batch.executed and self.request.has_perm('{0}.edit'.format(self.permission_prefix)):
            # g.editable = True
            # g.edit_route_name = '{0}.rows.edit'.format(self.route_prefix)
            g.deletable = True
            g.delete_route_name = '{0}.rows.delete'.format(self.route_prefix)
        return g

    def tr_class(self, row, i):
        pass

    def render_kwargs(self):
        """
        Add the current batch and route prefix to the template context.
        """
        return {'batch': self.current_batch(),
                'route_prefix': self.route_prefix}

    def bulk_delete(self):
        """
        "Delete" all rows matching the current row grid view query.  This sets
        the ``removed`` flag on the rows but does not truly delete them.
        """
        self.query().update({'removed': True}, synchronize_session=False)
        return httpexceptions.HTTPFound(location=self.request.route_url('{}.view'.format(self.route_prefix),
                                                                        uuid=self.request.matchdict['uuid']))


class ProductBatchRowGrid(BatchRowGrid):
    """
    Base grid view for batch rows which deal directly with products.
    """

    def filter_map(self):
        """
        Provides the default filter map for batch row grid views.  Derived
        classes should *not* override this, but :meth:`filter_map_extras()`
        instead.
        """
        return self.make_filter_map(exact=['status_code'],
                                    ilike=['brand_name', 'description', 'size'],
                                    upc=self.filter_gpc(self.row_class.upc))

    def filter_config(self):
        """
        Provides the default filter config for batch grid views.  Derived
        classes should *not* override this, but :meth:`filter_config_extras()`
        instead.
        """
        kwargs = {'filter_label_status_code': "Status",
                  'filter_factory_status_code': EnumSearchFilter(self.row_class.STATUS),
                  'filter_label_upc': "UPC",
                  'filter_label_brand_name': "Brand"}
        kwargs.update(self.filter_config_extras())
        return self.make_filter_config(**kwargs)


class BatchRowCrud(BaseCrud):
    """
    Base CRUD view for batch rows.
    """

    @property
    def row_class(self):
        raise NotImplementedError

    @property
    def mapped_class(self):
        return self.row_class

    @property
    def batch_class(self):
        """
        Model class of the batch to which the rows belong.
        """
        return self.row_class.__batch_class__

    @property
    def batch_display(self):
        """
        Singular display text for the batch type, e.g. "Vendor Invoice".
        Override this as necessary.
        """
        return self.batch_class.__name__

    def fieldset(self, row):
        """
        Creates the fieldset for the view.  Derived classes should *not*
        override this, but :meth:`configure_fieldset()` instead.
        """
        fs = self.make_fieldset(row)
        self.configure_fieldset(fs)
        return fs

    def configure_fieldset(self, fieldset):
        """
        Derived classes can override this.  Customizes a fieldset which has
        already been created with defaults by the base class.
        """
        fieldset.configure()

    def template_kwargs(self, form):
        """
        Add batch row instance etc. to template context.
        """
        row = form.fieldset.model
        return {
            'row': row,
            'batch_display': self.batch_display,
            'route_prefix': self.route_prefix,
            'permission_prefix': self.permission_prefix,
            }

    def delete(self):
        """
        "Delete" a row from the batch.  This sets the ``removed`` flag on the
        row but does not truly delete it.
        """
        row = self.get_model_from_request()
        if not row:
            raise httpexceptions.HTTPNotFound()
        row.removed = True
        return httpexceptions.HTTPFound(location=self.request.route_url('{}.view'.format(self.route_prefix),
                                                                        uuid=row.batch_uuid))


def defaults(config, batch_grid, batch_crud, row_grid, row_crud, url_prefix,
             route_prefix=None, permission_prefix=None, template_prefix=None):
    """
    Apply default configuration to the Pyramid configurator object, for the
    given batch grid and CRUD views.
    """
    assert batch_grid
    assert batch_crud
    assert url_prefix
    if route_prefix is None:
        route_prefix = batch_grid.route_prefix
    if permission_prefix is None:
        permission_prefix = route_prefix
    if template_prefix is None:
        template_prefix = url_prefix
    template_prefix.rstrip('/')

    # Batches grid
    config.add_route(route_prefix, url_prefix)
    config.add_view(batch_grid, route_name=route_prefix,
                    renderer='{0}/index.mako'.format(template_prefix),
                    permission='{0}.view'.format(permission_prefix))

    # Create batch
    config.add_route('{0}.create'.format(route_prefix), '{0}new'.format(url_prefix))
    config.add_view(batch_crud, attr='create', route_name='{0}.create'.format(route_prefix),
                    renderer='{0}/create.mako'.format(template_prefix),
                    permission='{0}.create'.format(permission_prefix))

    # View batch
    config.add_route('{0}.view'.format(route_prefix), '{0}{{uuid}}'.format(url_prefix))
    config.add_view(batch_crud, attr='read', route_name='{0}.view'.format(route_prefix),
                    renderer='{0}/view.mako'.format(template_prefix),
                    permission='{0}.view'.format(permission_prefix))

    # Edit batch
    config.add_route('{0}.edit'.format(route_prefix), '{0}{{uuid}}/edit'.format(url_prefix))
    config.add_view(batch_crud, attr='update', route_name='{0}.edit'.format(route_prefix),
                    renderer='{0}/edit.mako'.format(template_prefix),
                    permission='{0}.edit'.format(permission_prefix))

    # Refresh batch row data
    config.add_route('{0}.refresh'.format(route_prefix), '{0}{{uuid}}/refresh'.format(url_prefix))
    config.add_view(batch_crud, attr='refresh', route_name='{0}.refresh'.format(route_prefix),
                    permission='{0}.create'.format(permission_prefix))

    # Execute batch
    config.add_route('{0}.execute'.format(route_prefix), '{0}{{uuid}}/execute'.format(url_prefix))
    config.add_view(batch_crud, attr='execute', route_name='{0}.execute'.format(route_prefix),
                    permission='{0}.execute'.format(permission_prefix))

    # Download batch row data as CSV
    config.add_route('{0}.csv'.format(route_prefix), '{0}{{uuid}}/csv'.format(url_prefix))
    config.add_view(batch_crud, attr='csv', route_name='{0}.csv'.format(route_prefix),
                    permission='{0}.csv'.format(permission_prefix))

    # Download batch data file
    if hasattr(batch_crud, 'download'):
        config.add_route('{0}.download'.format(route_prefix), '{0}{{uuid}}/download'.format(url_prefix))
        config.add_view(batch_crud, attr='download', route_name='{0}.download'.format(route_prefix),
                        permission='{0}.download'.format(permission_prefix))

    # Delete batch
    config.add_route('{0}.delete'.format(route_prefix), '{0}{{uuid}}/delete'.format(url_prefix))
    config.add_view(batch_crud, attr='delete', route_name='{0}.delete'.format(route_prefix),
                    permission='{0}.delete'.format(permission_prefix))

    # Batch rows grid
    config.add_route('{0}.rows'.format(route_prefix), '{0}{{uuid}}/rows/'.format(url_prefix))
    config.add_view(row_grid, route_name='{0}.rows'.format(route_prefix),
                    renderer='/batch/rows.mako',
                    permission='{0}.view'.format(permission_prefix))

    # view batch row
    config.add_route('{0}.row.view'.format(route_prefix), '{0}row/{{uuid}}'.format(url_prefix))
    config.add_view(row_crud, attr='read', route_name='{0}.row.view'.format(route_prefix),
                    renderer='{0}/row.view.mako'.format(template_prefix),
                    permission='{0}.view'.format(permission_prefix))

    # Bulk delete batch rows
    config.add_route('{0}.rows.bulk_delete'.format(route_prefix), '{0}{{uuid}}/rows/delete'.format(url_prefix))
    config.add_view(row_grid, attr='bulk_delete', route_name='{0}.rows.bulk_delete'.format(route_prefix),
                    permission='{0}.edit'.format(permission_prefix))

    # Delete batch row
    config.add_route('{0}.rows.delete'.format(route_prefix), '{0}delete-row/{{uuid}}'.format(url_prefix))
    config.add_view(row_crud, attr='delete', route_name='{0}.rows.delete'.format(route_prefix),
                    permission='{0}.edit'.format(permission_prefix))
