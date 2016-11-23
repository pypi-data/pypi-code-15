"""
argparse module that sets default subparser
"""
from __future__ import absolute_import

import argparse
import sys


# http://stackoverflow.com/a/26379693/703144
class ArgumentParser(argparse.ArgumentParser):
    def set_default_subparser(self, name, args=None):
        """default subparser selection. Call after setup, just before parse_args()
        name: is the name of the subparser to call by default
        args: if set is the argument list handed to parse_args()

        , tested with 2.7, 3.2, 3.3, 3.4
        it works with 2.6 assuming argparse is installed
        """
        subparser_found = False
        for arg in sys.argv[1:]:
            if arg in ['-h', '--help']:  # global help if no subparser
                break
        else:
            for x in self._subparsers._actions:
                if not isinstance(x, argparse._SubParsersAction):
                    continue
                for sp_name in x._name_parser_map.keys():
                    if sp_name in sys.argv[1:]:
                        subparser_found = True
            if not subparser_found:
                # insert default in first position, this implies no
                # global options without a sub_parsers specified
                if args is None:
                    sys.argv.insert(1, name)
                else:
                    args.insert(0, name)

    def parse_args(self, args=None, namespace=None, default_subparser=None, default_subparser_args=None):
        if default_subparser:
            self.set_default_subparser(default_subparser, args=default_subparser_args)

        return super(ArgumentParser, self).parse_args(args, namespace)
