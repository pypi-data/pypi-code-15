from zope.schema.interfaces import IObject
from zope.interface import Interface
from zope import schema


class IFileManager(Interface):
    """Interface to create uploaders and downloaders."""

    async def upload(self):
        pass

    async def download(self):
        pass

    async def tus_post(self):
        pass

    async def tus_patch(self):
        pass

    async def tus_options(self):
        pass

    async def tus_head(self):
        pass


class IFile(Interface):

    contentType = schema.BytesLine(
        title=u'Content Type',
        description=u'The content type identifies the type of data.',
        default=b'',
        required=False
    )

    filename = schema.TextLine(title=u'Filename', required=False, default=None)

    data = schema.Bytes(
        title=u'Data',
        description=u'The actual content.',
        required=False,
    )

    def getSize():
        """Return the byte-size of the data of the object."""


# File Field

class IFileField(IObject):
    """Field for storing IFile objects."""


class IStorage(Interface):
    """Store file data."""

    def store(data, blob):
        """Store the data into the blob
        Raises NonStorable if data is not storable.
        """


class NotStorable(Exception):
    """Data is not storable."""
