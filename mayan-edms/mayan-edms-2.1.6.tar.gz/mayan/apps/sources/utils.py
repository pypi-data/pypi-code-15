from .forms import (
    POP3EmailSetupForm, IMAPEmailSetupForm,
    StagingFolderSetupForm, StagingUploadForm, WatchFolderSetupForm,
    WebFormSetupForm, WebFormUploadForm
)
from .literals import (
    SOURCE_CHOICE_EMAIL_IMAP, SOURCE_CHOICE_EMAIL_POP3, SOURCE_CHOICE_STAGING,
    SOURCE_CHOICE_WATCH, SOURCE_CHOICE_WEB_FORM
)
from .models import (
    IMAPEmail, POP3Email, StagingFolderSource, WatchFolderSource, WebFormSource
)


def get_class(source_type):
    if source_type == SOURCE_CHOICE_WEB_FORM:
        return WebFormSource
    elif source_type == SOURCE_CHOICE_STAGING:
        return StagingFolderSource
    elif source_type == SOURCE_CHOICE_WATCH:
        return WatchFolderSource
    elif source_type == SOURCE_CHOICE_EMAIL_POP3:
        return POP3Email
    elif source_type == SOURCE_CHOICE_EMAIL_IMAP:
        return IMAPEmail


def get_form_class(source_type):
    if source_type == SOURCE_CHOICE_WEB_FORM:
        return WebFormSetupForm
    elif source_type == SOURCE_CHOICE_STAGING:
        return StagingFolderSetupForm
    elif source_type == SOURCE_CHOICE_WATCH:
        return WatchFolderSetupForm
    elif source_type == SOURCE_CHOICE_EMAIL_POP3:
        return POP3EmailSetupForm
    elif source_type == SOURCE_CHOICE_EMAIL_IMAP:
        return IMAPEmailSetupForm


def get_upload_form_class(source_type):
    if source_type == SOURCE_CHOICE_WEB_FORM:
        return WebFormUploadForm
    elif source_type == SOURCE_CHOICE_STAGING:
        return StagingUploadForm
