# encoding: utf-8
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from .ttypes import *

ERROR_BACKOFF = {
    15 : 1000,
    18 : 1000,
    16 : 1000,
    17 : 1000,
    7 : 1000,
    14 : 1000,
    19 : 1000,
}
ERROR_RETRY_TYPE = {
    15 :   0,
    18 :   0,
    16 :   0,
    17 :   0,
    7 :   0,
    14 :   1,
    19 :   2,
}
MAX_RETRY = 3
