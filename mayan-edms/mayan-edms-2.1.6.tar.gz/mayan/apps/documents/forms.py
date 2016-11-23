from __future__ import absolute_import, unicode_literals

import logging
from operator import itemgetter

from django import forms
from django.core.exceptions import PermissionDenied
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

from acls.models import AccessControlList
from common.forms import DetailForm, ModelForm
from permissions import Permission

from .models import (
    Document, DocumentType, DocumentPage, DocumentTypeFilename
)
from .literals import DEFAULT_ZIP_FILENAME, PAGE_RANGE_CHOICES
from .permissions import permission_document_create
from .widgets import DocumentPagesCarouselWidget, DocumentPageImageWidget

logger = logging.getLogger(__name__)


# Document page forms
class DocumentPageForm(DetailForm):
    class Meta:
        fields = ()
        model = DocumentPage

    def __init__(self, *args, **kwargs):
        zoom = kwargs.pop('zoom', 100)
        rotation = kwargs.pop('rotation', 0)
        super(DocumentPageForm, self).__init__(*args, **kwargs)
        self.fields['page_image'].initial = self.instance
        self.fields['page_image'].widget.attrs.update({
            'zoom': zoom,
            'rotation': rotation
        })

    page_image = forms.CharField(
        label=_('Page image'), widget=DocumentPageImageWidget()
    )


# Document forms


class DocumentPreviewForm(forms.Form):
    def __init__(self, *args, **kwargs):
        document = kwargs.pop('instance', None)
        super(DocumentPreviewForm, self).__init__(*args, **kwargs)
        self.fields['preview'].initial = document
        try:
            self.fields['preview'].label = _(
                'Document pages (%d)'
            ) % document.page_count
        except AttributeError:
            self.fields['preview'].label = _('Document pages (%d)') % 0

    preview = forms.CharField(widget=DocumentPagesCarouselWidget())


class DocumentForm(ModelForm):
    """
    Form sub classes from DocumentForm used only when editing a document
    """
    class Meta:
        fields = ('label', 'description', 'language')
        model = Document
        sorted_fields = {'language': itemgetter(1)}

    def __init__(self, *args, **kwargs):
        document_type = kwargs.pop('document_type', None)

        super(DocumentForm, self).__init__(*args, **kwargs)

        # Is a document (documents app edit) and has been saved (sources
        # app upload)?
        if self.instance and self.instance.pk:
            document_type = self.instance.document_type

        filenames_qs = document_type.filenames.filter(enabled=True)
        if filenames_qs.count():
            self.fields[
                'document_type_available_filenames'
            ] = forms.ModelChoiceField(
                queryset=filenames_qs,
                required=False,
                label=_('Quick document rename')
            )

    def clean(self):
        if 'document_type_available_filenames' in self.cleaned_data:
            if self.cleaned_data['document_type_available_filenames']:
                self.cleaned_data['label'] = self.cleaned_data[
                    'document_type_available_filenames'
                ]

        return self.cleaned_data


class DocumentPropertiesForm(DetailForm):
    """
    Detail class form to display a document file based properties
    """
    def __init__(self, *args, **kwargs):
        document = kwargs['instance']

        extra_fields = [
            {
                'label': _('Date added'),
                'field': 'date_added',
                'widget': forms.widgets.DateTimeInput
            },
            {'label': _('UUID'), 'field': 'uuid'},
        ]

        if document.latest_version:
            extra_fields += (
                {
                    'label': _('File mimetype'),
                    'field': lambda x: document.file_mimetype or _('None')
                },
                {
                    'label': _('File encoding'),
                    'field': lambda x: document.file_mime_encoding or _(
                        'None'
                    )
                },
                {
                    'label': _('File size'),
                    'field': lambda document: filesizeformat(
                        document.size
                    ) if document.size else '-'
                },
                {'label': _('Exists in storage'), 'field': 'exists'},
                {
                    'label': _('File path in storage'),
                    'field': 'latest_version.file'
                },
                {'label': _('Checksum'), 'field': 'checksum'},
                {'label': _('Pages'), 'field': 'page_count'},
            )

        kwargs['extra_fields'] = extra_fields
        super(DocumentPropertiesForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ('document_type', 'description', 'language')
        model = Document


class DocumentTypeSelectForm(forms.Form):
    """
    Form to select the document type of a document to be created, used
    as form #1 in the document creation wizard
    """

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        logger.debug('user: %s', user)
        super(DocumentTypeSelectForm, self).__init__(*args, **kwargs)

        queryset = DocumentType.objects.all()
        try:
            Permission.check_permissions(user, (permission_document_create,))
        except PermissionDenied:
            queryset = AccessControlList.objects.filter_by_access(
                permission_document_create, user, queryset
            )

        self.fields['document_type'] = forms.ModelChoiceField(
            empty_label=None, label=_('Document type'), queryset=queryset,
            required=True, widget=forms.widgets.Select(attrs={'size': 10})
        )


class DocumentTypeFilenameForm_create(forms.ModelForm):
    """
    Model class form to create a new document type filename
    """
    class Meta:
        fields = ('filename',)
        model = DocumentTypeFilename


class DocumentDownloadForm(forms.Form):
    compressed = forms.BooleanField(
        label=_('Compress'), required=False,
        help_text=_(
            'Download the document in the original format or in a compressed '
            'manner. This option is selectable only when downloading one '
            'document, for multiple documents, the bundle will always be '
            'downloads as a compressed file.'
        )
    )
    zip_filename = forms.CharField(
        initial=DEFAULT_ZIP_FILENAME, label=_('Compressed filename'),
        required=False,
        help_text=_(
            'The filename of the compressed file that will contain the '
            'documents to be downloaded, if the previous option is selected.'
        )
    )

    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.pop('queryset', None)
        super(DocumentDownloadForm, self).__init__(*args, **kwargs)
        if self.queryset.count() > 1:
            self.fields['compressed'].initial = True
            self.fields['compressed'].widget.attrs.update({'disabled': True})


class PrintForm(forms.Form):
    page_group = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAGE_RANGE_CHOICES
    )
    page_range = forms.CharField(label=_('Page range'), required=False)
