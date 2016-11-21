"""Mypy type checker command line tool."""

import argparse
import configparser
import os
import re
import sys
import time

from typing import Any, Dict, List, Mapping, Optional, Set, Tuple

from mypy import build
from mypy import defaults
from mypy import git
from mypy import experiments
from mypy import util
from mypy.build import BuildSource, BuildResult, PYTHON_EXTENSIONS
from mypy.errors import CompileError
from mypy.options import Options, BuildType
from mypy.report import reporter_classes

from mypy.version import __version__

PY_EXTENSIONS = tuple(PYTHON_EXTENSIONS)


def main(script_path: str) -> None:
    """Main entry point to the type checker.

    Args:
        script_path: Path to the 'mypy' script (used for finding data files).
    """
    t0 = time.time()
    if script_path:
        bin_dir = find_bin_directory(script_path)
    else:
        bin_dir = None
    sources, options = process_options(sys.argv[1:])
    serious = False
    try:
        res = type_check_only(sources, bin_dir, options)
        a = res.errors
    except CompileError as e:
        a = e.messages
        if not e.use_stdout:
            serious = True
    if options.junit_xml:
        t1 = time.time()
        util.write_junit_xml(t1 - t0, serious, a, options.junit_xml)
    if a:
        f = sys.stderr if serious else sys.stdout
        for m in a:
            f.write(m + '\n')
        sys.exit(1)


def find_bin_directory(script_path: str) -> str:
    """Find the directory that contains this script.

    This is used by build to find stubs and other data files.
    """
    # Follow up to 5 symbolic links (cap to avoid cycles).
    for i in range(5):
        if os.path.islink(script_path):
            script_path = readlinkabs(script_path)
        else:
            break
    return os.path.dirname(script_path)


def readlinkabs(link: str) -> str:
    """Return an absolute path to symbolic link destination."""
    # Adapted from code by Greg Smith.
    assert os.path.islink(link)
    path = os.readlink(link)
    if os.path.isabs(path):
        return path
    return os.path.join(os.path.dirname(link), path)


def type_check_only(sources: List[BuildSource],
        bin_dir: str, options: Options) -> BuildResult:
    # Type-check the program and dependencies and translate to Python.
    return build.build(sources=sources,
                       bin_dir=bin_dir,
                       options=options)


FOOTER = """environment variables:
MYPYPATH     additional module search path"""


class SplitNamespace(argparse.Namespace):
    def __init__(self, standard_namespace: object, alt_namespace: object, alt_prefix: str) -> None:
        self.__dict__['_standard_namespace'] = standard_namespace
        self.__dict__['_alt_namespace'] = alt_namespace
        self.__dict__['_alt_prefix'] = alt_prefix

    def _get(self) -> Tuple[Any, Any]:
        return (self._standard_namespace, self._alt_namespace)

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith(self._alt_prefix):
            setattr(self._alt_namespace, name[len(self._alt_prefix):], value)
        else:
            setattr(self._standard_namespace, name, value)

    def __getattr__(self, name: str) -> Any:
        if name.startswith(self._alt_prefix):
            return getattr(self._alt_namespace, name[len(self._alt_prefix):])
        else:
            return getattr(self._standard_namespace, name)


def parse_version(v: str) -> Tuple[int, int]:
    m = re.match(r'\A(\d)\.(\d+)\Z', v)
    if m:
        return int(m.group(1)), int(m.group(2))
    else:
        raise argparse.ArgumentTypeError(
            "Invalid python version '{}' (expected format: 'x.y')".format(v))


def process_options(args: List[str],
                    require_targets: bool = True
                    ) -> Tuple[List[BuildSource], Options]:
    """Parse command line arguments."""

    # Make the help output a little less jarring.
    help_factory = (lambda prog:
                    argparse.RawDescriptionHelpFormatter(prog=prog, max_help_position=28))
    parser = argparse.ArgumentParser(prog='mypy', epilog=FOOTER,
                                     fromfile_prefix_chars='@',
                                     formatter_class=help_factory)

    # Unless otherwise specified, arguments will be parsed directly onto an
    # Options object.  Options that require further processing should have
    # their `dest` prefixed with `special-opts:`, which will cause them to be
    # parsed into the separate special_opts namespace object.
    parser.add_argument('-v', '--verbose', action='count', dest='verbosity',
                        help="more verbose messages")
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s ' + __version__)
    parser.add_argument('--python-version', type=parse_version, metavar='x.y',
                        help='use Python x.y')
    parser.add_argument('--platform', action='store', metavar='PLATFORM',
                        help="typecheck special-cased code for the given OS platform "
                        "(defaults to sys.platform).")
    parser.add_argument('-2', '--py2', dest='python_version', action='store_const',
                        const=defaults.PYTHON2_VERSION, help="use Python 2 mode")
    parser.add_argument('-s', '--silent-imports', action='store_true',
                        help="don't follow imports to .py files")
    parser.add_argument('--almost-silent', action='store_true',
                        help="like --silent-imports but reports the imports as errors")
    parser.add_argument('--disallow-untyped-calls', action='store_true',
                        help="disallow calling functions without type annotations"
                        " from functions with type annotations")
    parser.add_argument('--disallow-untyped-defs', action='store_true',
                        help="disallow defining functions without type annotations"
                        " or with incomplete type annotations")
    parser.add_argument('--check-untyped-defs', action='store_true',
                        help="type check the interior of functions without type annotations")
    parser.add_argument('--disallow-subclassing-any', action='store_true',
                        help="disallow subclassing values of type 'Any' when defining classes")
    parser.add_argument('--warn-incomplete-stub', action='store_true',
                        help="warn if missing type annotation in typeshed, only relevant with"
                        " --check-untyped-defs enabled")
    parser.add_argument('--warn-redundant-casts', action='store_true',
                        help="warn about casting an expression to its inferred type")
    parser.add_argument('--warn-no-return', action='store_true',
                        help="warn about functions that end without returning")
    parser.add_argument('--warn-unused-ignores', action='store_true',
                        help="warn about unneeded '# type: ignore' comments")
    parser.add_argument('--hide-error-context', action='store_true',
                        dest='hide_error_context',
                        help="Hide context notes before errors")
    parser.add_argument('--fast-parser', action='store_true',
                        help="enable experimental fast parser")
    parser.add_argument('-i', '--incremental', action='store_true',
                        help="enable experimental module cache")
    parser.add_argument('--cache-dir', action='store', metavar='DIR',
                        help="store module cache info in the given folder in incremental mode "
                        "(defaults to '{}')".format(defaults.CACHE_DIR))
    parser.add_argument('--strict-optional', action='store_true',
                        dest='strict_optional',
                        help="enable experimental strict Optional checks")
    parser.add_argument('--strict-optional-whitelist', metavar='GLOB', nargs='*',
                        help="suppress strict Optional errors in all but the provided files "
                        "(experimental -- read documentation before using!).  "
                        "Implies --strict-optional.  Has the undesirable side-effect of "
                        "suppressing other errors in non-whitelisted files.")
    parser.add_argument('--junit-xml', help="write junit.xml to the given file")
    parser.add_argument('--pdb', action='store_true', help="invoke pdb on fatal error")
    parser.add_argument('--show-traceback', '--tb', action='store_true',
                        help="show traceback on fatal error")
    parser.add_argument('--stats', action='store_true', dest='dump_type_stats', help="dump stats")
    parser.add_argument('--inferstats', action='store_true', dest='dump_inference_stats',
                        help="dump type inference stats")
    parser.add_argument('--custom-typing', metavar='MODULE', dest='custom_typing_module',
                        help="use a custom typing module")
    parser.add_argument('--custom-typeshed-dir', metavar='DIR',
                        help="use the custom typeshed in DIR")
    parser.add_argument('--scripts-are-modules', action='store_true',
                        help="Script x becomes module x instead of __main__")
    parser.add_argument('--config-file',
                        help="Configuration file, must have a [mypy] section "
                        "(defaults to {})".format(defaults.CONFIG_FILE))
    parser.add_argument('--show-column-numbers', action='store_true',
                        dest='show_column_numbers',
                        help="Show column numbers in error messages")
    parser.add_argument('--find-occurrences', metavar='CLASS.MEMBER',
                        dest='special-opts:find_occurrences',
                        help="print out all usages of a class member (experimental)")
    # hidden options
    # --shadow-file a.py tmp.py will typecheck tmp.py in place of a.py.
    # Useful for tools to make transformations to a file to get more
    # information from a mypy run without having to change the file in-place
    # (e.g. by adding a call to reveal_type).
    parser.add_argument('--shadow-file', metavar='PATH', nargs=2, dest='shadow_file',
                        help=argparse.SUPPRESS)
    # --debug-cache will disable any cache-related compressions/optimizations,
    # which will make the cache writing process output pretty-printed JSON (which
    # is easier to debug).
    parser.add_argument('--debug-cache', action='store_true', help=argparse.SUPPRESS)
    # deprecated options
    parser.add_argument('--silent', action='store_true', dest='special-opts:silent',
                        help=argparse.SUPPRESS)
    parser.add_argument('-f', '--dirty-stubs', action='store_true',
                        dest='special-opts:dirty_stubs',
                        help=argparse.SUPPRESS)
    parser.add_argument('--use-python-path', action='store_true',
                        dest='special-opts:use_python_path',
                        help=argparse.SUPPRESS)

    report_group = parser.add_argument_group(
        title='report generation',
        description='Generate a report in the specified format.')
    for report_type in sorted(reporter_classes):
        report_group.add_argument('--%s-report' % report_type.replace('_', '-'),
                                  metavar='DIR',
                                  dest='special-opts:%s_report' % report_type)

    code_group = parser.add_argument_group(title='How to specify the code to type check')
    code_group.add_argument('-m', '--module', action='append', metavar='MODULE',
                            dest='special-opts:modules',
                            help="type-check module; can repeat for more modules")
    # TODO: `mypy -p A -p B` currently silently ignores ignores A
    # (last option wins).  Perhaps -c, -m and -p could just be
    # command-line flags that modify how we interpret self.files?
    code_group.add_argument('-c', '--command', action='append', metavar='PROGRAM_TEXT',
                            dest='special-opts:command',
                            help="type-check program passed in as string")
    code_group.add_argument('-p', '--package', metavar='PACKAGE', dest='special-opts:package',
                            help="type-check all files in a directory")
    code_group.add_argument(metavar='files', nargs='*', dest='special-opts:files',
                            help="type-check given files or directories")

    # Parse arguments once into a dummy namespace so we can get the
    # filename for the config file.
    dummy = argparse.Namespace()
    parser.parse_args(args, dummy)
    config_file = dummy.config_file or defaults.CONFIG_FILE

    # Parse config file first, so command line can override.
    options = Options()
    if config_file and os.path.exists(config_file):
        parse_config_file(options, config_file)

    # Parse command line for real, using a split namespace.
    special_opts = argparse.Namespace()
    parser.parse_args(args, SplitNamespace(options, special_opts, 'special-opts:'))

    # --use-python-path is no longer supported; explain why.
    if special_opts.use_python_path:
        parser.error("Sorry, --use-python-path is no longer supported.\n"
                     "If you are trying this because your code depends on a library module,\n"
                     "you should really investigate how to obtain stubs for that module.\n"
                     "See https://github.com/python/mypy/issues/1411 for more discussion."
                     )

    # warn about deprecated options
    if special_opts.silent:
        print("Warning: --silent is deprecated; use --silent-imports",
              file=sys.stderr)
        options.silent_imports = True
    if special_opts.dirty_stubs:
        print("Warning: -f/--dirty-stubs is deprecated and no longer necessary. Mypy no longer "
              "checks the git status of stubs.",
              file=sys.stderr)

    # Check for invalid argument combinations.
    if require_targets:
        code_methods = sum(bool(c) for c in [special_opts.modules,
                                            special_opts.command,
                                            special_opts.package,
                                            special_opts.files])
        if code_methods == 0:
            parser.error("Missing target module, package, files, or command.")
        elif code_methods > 1:
            parser.error("May only specify one of: module, package, files, or command.")

    # Set build flags.
    if options.strict_optional_whitelist is not None:
        # TODO: Deprecate, then kill this flag
        options.strict_optional = True
    if options.strict_optional:
        experiments.STRICT_OPTIONAL = True
    if special_opts.find_occurrences:
        experiments.find_occurrences = special_opts.find_occurrences.split('.')
        if len(experiments.find_occurrences) < 2:
            parser.error("Can only find occurrences of class members.")
        if len(experiments.find_occurrences) != 2:
            parser.error("Can only find occurrences of non-nested class members.")

    # Set reports.
    for flag, val in vars(special_opts).items():
        if flag.endswith('_report') and val is not None:
            report_type = flag[:-7].replace('_', '-')
            report_dir = val
            options.report_dirs[report_type] = report_dir

    # Set target.
    if special_opts.modules:
        options.build_type = BuildType.MODULE
        targets = [BuildSource(None, m, None) for m in special_opts.modules]
        return targets, options
    elif special_opts.package:
        if os.sep in special_opts.package or os.altsep and os.altsep in special_opts.package:
            fail("Package name '{}' cannot have a slash in it."
                 .format(special_opts.package))
        options.build_type = BuildType.MODULE
        lib_path = [os.getcwd()] + build.mypy_path()
        targets = build.find_modules_recursive(special_opts.package, lib_path)
        if not targets:
            fail("Can't find package '{}'".format(special_opts.package))
        return targets, options
    elif special_opts.command:
        options.build_type = BuildType.PROGRAM_TEXT
        return [BuildSource(None, None, '\n'.join(special_opts.command))], options
    else:
        targets = []
        for f in special_opts.files:
            if f.endswith(PY_EXTENSIONS):
                targets.append(BuildSource(f, crawl_up(f)[1], None))
            elif os.path.isdir(f):
                sub_targets = expand_dir(f)
                if not sub_targets:
                    fail("There are no .py[i] files in directory '{}'"
                         .format(f))
                targets.extend(sub_targets)
            else:
                mod = os.path.basename(f) if options.scripts_are_modules else None
                targets.append(BuildSource(f, mod, None))
        return targets, options


def keyfunc(name: str) -> Tuple[int, str]:
    """Determines sort order for directory listing.

    The desirable property is foo < foo.pyi < foo.py.
    """
    base, suffix = os.path.splitext(name)
    for i, ext in enumerate(PY_EXTENSIONS):
        if suffix == ext:
            return (i, base)
    return (-1, name)


def expand_dir(arg: str, mod_prefix: str = '') -> List[BuildSource]:
    """Convert a directory name to a list of sources to build."""
    f = get_init_file(arg)
    if mod_prefix and not f:
        return []
    seen = set()  # type: Set[str]
    sources = []
    if f and not mod_prefix:
        top_dir, top_mod = crawl_up(f)
        mod_prefix = top_mod + '.'
    if mod_prefix:
        sources.append(BuildSource(f, mod_prefix.rstrip('.'), None))
    names = os.listdir(arg)
    names.sort(key=keyfunc)
    for name in names:
        path = os.path.join(arg, name)
        if os.path.isdir(path):
            sub_sources = expand_dir(path, mod_prefix + name + '.')
            if sub_sources:
                seen.add(name)
                sources.extend(sub_sources)
        else:
            base, suffix = os.path.splitext(name)
            if base == '__init__':
                continue
            if base not in seen and '.' not in base and suffix in PY_EXTENSIONS:
                seen.add(base)
                src = BuildSource(path, mod_prefix + base, None)
                sources.append(src)
    return sources


def crawl_up(arg: str) -> Tuple[str, str]:
    """Given a .py[i] filename, return (root directory, module).

    We crawl up the path until we find a directory without
    __init__.py[i], or until we run out of path components.
    """
    dir, mod = os.path.split(arg)
    mod = strip_py(mod) or mod
    assert '.' not in mod
    while dir and get_init_file(dir):
        dir, base = os.path.split(dir)
        if not base:
            break
        if mod == '__init__' or not mod:
            mod = base
        else:
            mod = base + '.' + mod
    return dir, mod


def strip_py(arg: str) -> Optional[str]:
    """Strip a trailing .py or .pyi suffix.

    Return None if no such suffix is found.
    """
    for ext in PY_EXTENSIONS:
        if arg.endswith(ext):
            return arg[:-len(ext)]
    return None


def get_init_file(dir: str) -> Optional[str]:
    """Check whether a directory contains a file named __init__.py[i].

    If so, return the file's name (with dir prefixed).  If not, return
    None.

    This prefers .pyi over .py (because of the ordering of PY_EXTENSIONS).
    """
    for ext in PY_EXTENSIONS:
        f = os.path.join(dir, '__init__' + ext)
        if os.path.isfile(f):
            return f
    return None


# For most options, the type of the default value set in options.py is
# sufficient, and we don't have to do anything here.  This table
# exists to specify types for values initialized to None or container
# types.
config_types = {
    # TODO: Check validity of python version
    'python_version': lambda s: tuple(map(int, s.split('.'))),
    'strict_optional_whitelist': lambda s: s.split(),
    'custom_typing_module': str,
    'custom_typeshed_dir': str,
    'mypy_path': lambda s: [p.strip() for p in re.split('[,:]', s)],
    'junit_xml': str,
}


def parse_config_file(options: Options, filename: str) -> None:
    """Parse a config file into an Options object.

    Errors are written to stderr but are not fatal.
    """
    parser = configparser.RawConfigParser()
    try:
        parser.read(filename)
    except configparser.Error as err:
        print("%s: %s" % (filename, err), file=sys.stderr)
        return
    if 'mypy' not in parser:
        print("%s: No [mypy] section in config file" % filename, file=sys.stderr)
        return

    section = parser['mypy']
    prefix = '%s: [%s]' % (filename, 'mypy')
    updates, report_dirs = parse_section(prefix, options, section)
    for k, v in updates.items():
        setattr(options, k, v)
    options.report_dirs.update(report_dirs)

    for name, section in parser.items():
        if name.startswith('mypy-'):
            prefix = '%s: [%s]' % (filename, name)
            updates, report_dirs = parse_section(prefix, options, section)
            if report_dirs:
                print("%s: Per-module sections should not specify reports (%s)" %
                      (prefix, ', '.join(s + '_report' for s in sorted(report_dirs))),
                      file=sys.stderr)
            if set(updates) - Options.PER_MODULE_OPTIONS:
                print("%s: Per-module sections should only specify per-module flags (%s)" %
                      (prefix, ', '.join(sorted(set(updates) - Options.PER_MODULE_OPTIONS))),
                      file=sys.stderr)
                updates = {k: v for k, v in updates.items() if k in Options.PER_MODULE_OPTIONS}
            globs = name[5:]
            for glob in globs.split(','):
                # For backwards compatibility, replace (back)slashes with dots.
                glob = glob.replace(os.sep, '.')
                if os.altsep:
                    glob = glob.replace(os.altsep, '.')
                options.per_module_options[glob] = updates


def parse_section(prefix: str, template: Options,
                  section: Mapping[str, str]) -> Tuple[Dict[str, object], Dict[str, str]]:
    """Parse one section of a config file.

    Returns a dict of option values encountered, and a dict of report directories.
    """
    results = {}
    report_dirs = {}  # type: Dict[str, str]
    for key in section:
        key = key.replace('-', '_')
        if key in config_types:
            ct = config_types[key]
        else:
            dv = getattr(template, key, None)
            if dv is None:
                if key.endswith('_report'):
                    report_type = key[:-7].replace('_', '-')
                    if report_type in reporter_classes:
                        report_dirs[report_type] = section.get(key)
                    else:
                        print("%s: Unrecognized report type: %s" % (prefix, key),
                              file=sys.stderr)
                    continue
                print("%s: Unrecognized option: %s = %s" % (prefix, key, section[key]),
                      file=sys.stderr)
                continue
            ct = type(dv)
        v = None  # type: Any
        try:
            if ct is bool:
                v = section.getboolean(key)  # type: ignore  # Until better stub
            elif callable(ct):
                v = ct(section.get(key))
            else:
                print("%s: Don't know what type %s should have" % (prefix, key), file=sys.stderr)
                continue
        except ValueError as err:
            print("%s: %s: %s" % (prefix, key, err), file=sys.stderr)
            continue
        results[key] = v
    return results, report_dirs


def fail(msg: str) -> None:
    sys.stderr.write('%s\n' % msg)
    sys.exit(1)
