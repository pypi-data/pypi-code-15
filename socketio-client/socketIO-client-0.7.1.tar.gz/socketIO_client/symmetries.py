from six import indexbytes


try:
    from logging import NullHandler
except ImportError:  # Python 2.6
    from logging import Handler

    class NullHandler(Handler):

        def emit(self, record):
            pass


try:
    memoryview = memoryview
except NameError:
    memoryview = buffer


def get_character(x, index):
    return chr(get_byte(x, index))


def get_byte(x, index):
    return indexbytes(x, index)


def decode_string(x):
    return x.decode('utf-8')


def encode_string(x):
    return x.encode('utf-8')
