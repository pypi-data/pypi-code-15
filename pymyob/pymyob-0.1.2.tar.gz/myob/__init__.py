from .api import Myob  # noqa
from .credentials import PartnerCredentials  # noqa

VERSION = (0, 1, 2)

__version__ = '.'.join(str(x) for x in VERSION[:(2 if VERSION[2] == 0 else 3)])  # noqa
