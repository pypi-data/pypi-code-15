import copy
import errno
import inspect
import logging
import logging.handlers
import os
import requests
import socket
import subprocess
import sys
import traceback
from collections import OrderedDict, Callable
from difflib import SequenceMatcher
from functools import wraps
from six import iteritems
from subprocess import Popen, PIPE

from pymongo import MongoClient
from gymail.core import send_mail


def _wrap_with(code):

    def inner(text, bold=False):
        c = code
        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)
    return inner


tor_proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}
red, green, yellow = _wrap_with('31'), _wrap_with('32'), _wrap_with('33')
blue, magenta, cyan, blue = _wrap_with('34'), _wrap_with('35'), _wrap_with('36'), _wrap_with('37')


class SetupLogger():
    """Logs to syslog and console with some format conveniences. Instantiating class here, because other functions in
       here are dependent on this logger. So import the instance log from here and don't create a new instance of
       SetupLogger unless you want to derive from it."""

    def __init__(self, verbose):
        self.logger = logging.getLogger()  # Initializing Logger
        syslog_handler = logging.handlers.SysLogHandler('/dev/log')
        self.logger.addHandler(syslog_handler)  # Add SysLogHandler
        self.console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.console_handler.setFormatter(formatter)
        self.logger.addHandler(self.console_handler)
        if verbose == "vvv":
            self.logger.setLevel(logging.DEBUG)
        elif verbose == "vv":
            self.logger.setLevel(logging.INFO)
        elif verbose == "v":
            self.logger.setLevel(logging.ERROR)

    def info(self, message, newline=0, v=True):
        """Automatically log the current function details."""
        if newline > 0:
            self.newline(newline)
        if v:
            self.logger.info(message)

    def error(self, message, v=True):
        func = inspect.currentframe().f_back.f_code
        if v:
            self.logger.error("{0} {1}".format(func.co_name, red(message)))

    def warning(self, message, v=True):
        func = inspect.currentframe().f_back.f_code
        if v:
            self.logger.warning("{0} {1}".format(func.co_name, cyan(message)))

    def debug(self, message, v=True):
        func = inspect.currentframe().f_back.f_code
        if v:
            self.logger.debug("{0} {1}".format(func.co_name, magenta(message)))

    def newline(self, how_many_lines=1):
        for i in range(how_many_lines):
            self.logger.info('')


log = SetupLogger('vvv')


def _isfile(f, hn=False):
    """Checks if file is a file, either locally or remotely."""
    cmd = ["file", "-b", f]
    if hn and not islocal(hn):
        cmd = ["ssh", hn] + cmd
    p1 = Popen(cmd, stdout=PIPE)
    out = p1.communicate()[0].decode("UTF-8")
    if "No such file" in out:
        return None
    elif "directory" in out:
        return False
    else:
        return True


def islocal(hn1):
    """Checks if the hostname is the local hostname"""
    hn2 = socket.gethostname()
    log.debug("hn1: %s hn2: %s" % (hn1, hn2))
    if hn1 in hn2 or hn2 in hn1:
        return True
    else:
        return False


def rsync(src, dst, remote_host=None, exclude=list(), tor=False, rsync_args=None):
    """Rsync wrapper with exclude and remote_host"""
    src = os.path.normpath(src)
    torsocks = ["torsocks"] if tor else []
    if not rsync_args:
        rsync_args = ["-avHAXx"]
    if remote_host:
        p1 = Popen(torsocks + ["rsync"] + rsync_args + exclude + [src, "{0}:{1}".format(remote_host, dst)], stdout=PIPE)
    else:
        p1 = Popen(["rsync"] + rsync_args + exclude + [src, dst], stdout=PIPE)
    log.info(p1.communicate())
    log.info(p1.returncode)
    if p1.returncode != 0:
        log.error("Rsync error. sendmail")


def is_number(s):
    """Checks if given parameter is a number or not"""
    try:
        float(s)
        return True
    except ValueError:
        return False


def find_mountpoint(path, hn=False):
    """Returns mountpoint from local or given remote system (requires ssh alias for hostname to be configured)."""
    cmd = ["findmnt", "-T", path, "-n", "-o", "TARGET"]
    log.debug("hn: %s, path %s" % (hn, path))
    if hn and not islocal(hn):
        cmd = ["ssh", hn] + cmd
        log.debug("cmd: %s" % str(cmd))
    p1 = Popen(cmd, stdout=PIPE, stderr=PIPE)
    path, err = p1.communicate()
    path = path.decode("UTF-8").strip()
    log.debug("err: %s" % err)
    log.info("mountpoint is: %s" % path)
    return path


def format_exception(e):
    """Usage:  except Exception as e: log.error(format_exception(e))"""
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))
    exception_str = "Traceback (most recent call last):\n"
    exception_str += "".join(exception_list)
    exception_str = exception_str[:-1]  # Removing the last \n
    return exception_str


def listdir_fullpath(d):
    """List dirs in given director with their fullpath."""
    return [os.path.join(d, f) for f in os.listdir(d)]


def remote_file_content(hn, fn):
    """Returns files content UTF-8 decoded via ssh by the given hostname and filename."""
    log.info("content of %s:%s (hn:filename)" % (hn, fn))
    p1 = Popen(["ssh", hn, "sudo", "/usr/bin/cat", fn], stdout=PIPE)
    return p1.communicate()[0].decode("UTF-8").split("\n")


def try_func(func, *args, **kwargs):
    """Try except wrapper."""
    try:
        val = func(*args, **kwargs)
        return val
    except Exception as e:
        log.error(format_exception(e))
        return False


def similar(a, b):
    """Returns float from 0 to 1 of how similar two strings are."""
    return SequenceMatcher(None, a, b).ratio()


def mkdir_p(dirs):
    """Equivalent to linux command `mkdir -p`. Also accepts list of directories."""
    if isinstance(dirs, str):
        dirs = [dirs]
    elif isinstance(dirs, list):
        pass
    else:
        log.error("Pass a string or a list of strings to this function. Returning.")
        return
    for x in dirs:
        if not os.path.exists(x):
            try:
                os.makedirs(x)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(path):
                    pass
                else:
                    log.error("Could not create directory")
                    pass
        else:
            log.info("Directory exists already.")


def umount(mp, lazy=False, fuser=False):
    """Umounts given mountpoint. Can umount also with lazy switch."""
    cmd_umount, cmd_lazy_umount = (["/usr/bin/umount"], ["/usr/bin/umount", "-l"])
    if fuser:
        cmd_umount, cmd_lazy_umount = (["/usr/bin/fusermount", "-u"], ["/usr/bin/fusermount", "-u", "-z"])
    cmd = cmd_lazy_umount if lazy else cmd_umount
    log.debug(cmd)
    p1 = Popen(cmd + [mp], stdout=PIPE, stderr=PIPE)
    out, err = p1.communicate()
    log.info("umount: out: %s, err: %s" % (out, err))
    log.info("Unmounted mp %s" % mp)


def mount(dev, mp):
    """Mounts a dev to mountpoint. If mp is occupied it'll try to umount first."""
    if os.path.ismount(mp):
        log.warning("Already mounted. Trying to unmount.")
        umount(mp)
        if os.path.ismount(mp):
            log.warning("Still mounted. Trying lazy unmount.")
            try_func(umount, mp, lazy=True)
            if os.path.ismount(mp):
                log.error("Couldn't be unmounted.")
                return False
    cmd_mount = ["mount", dev, mp]
    try:
        p1 = Popen(cmd_mount, stdin=PIPE)
        out, err = p1.communicate()
        log.debug("out: %s, err: %s" % (out, err))
        if p1.returncode == 0 and os.path.ismount(mp):
            log.info("Mounted %s to %s" % (dev, mp))
            return True
        else:
            log.error("Mounting failed. Error: %s\n%s" % (out, err))
            return False
    except Exception as e:
        log.error(format_exception(e))
        return False


def systemd_services_up(services):
    """Checks if given systems services are up, if not it exists."""
    for x in services:
        p = Popen(["systemctl", "is-active", x], stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        out = out.decode("utf-8").strip()
        if "failed" == out:
            log.info("Exiting, because dependent services are down: %s" % services)
            sys.exit()


def my_ip(proxies=None):
    kwargs = { "proxies": proxies } if proxies else {}
    url = 'http://myip.dnsomatic.com'
    r = requests.get(url, **kwargs)
    return r.text


def download(filename, download_link, proxies=None, tor=False):
    """Download file from given download link to given local filename path."""
    with open(filename, 'wb') as f:
        kwargs = {}
        if tor:
            log.debug("requests with tor enabled, using requests >=2.10 with socks5 support.")
            log.debug("Current IP: %s" % my_ip(proxies=tor_proxies))
            kwargs = { "proxies": tor_proxies }
        elif proxies:
            log.debug("Using custom proxies.")
            log.debug("Current IP: %s" % my_ip(proxies=proxies))
            kwargs = { "proxies": proxies }
        response = requests.get(download_link, stream=True, **kwargs)
        if not response.ok:
            send_mail(event="error", subject=os.path.basename(__file__),
                      message="Download from %s failed. Site possibly down." % download_link)
            return False
        for block in response.iter_content(1024):
            f.write(block)
    return True


def newest_dir(b='.'):
    """Returns newest (=last modified) directory of given path."""
    all_dirs = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd): all_dirs.append(bd)
    newest_dir = max(all_dirs, key=os.path.getmtime)
    return newest_dir


def handle_exceptions(fn):
    """Decorator for functions/methods to catch exceptions, apply with @handle_exception above method."""
    @wraps(fn)
    def wrapper(self, *args, **kw):
        try:
            return fn(self, *args, **kw)
        except Exception as e:
            log.error("Catched error with handle_exception decorator")
            log.error(format_exception(e))
    return wrapper


def multilog(only_first=False, **kwargs):
    """Convenience method, which prints the formated kwargs to log.debug(). If only_first is True, then only first
    element of a list is printed to the logs, though strings are still printed completely."""
    merged = str()
    for k, v in iteritems(kwargs):
        if only_first and isinstance(v, list):
            if v:
                v = v[0]
        m = "{0}: {1},".format(k, v)
        if len(m) > 80:
            m = "\n{0}\n".format(m)
        merged += m
    log.debug(merged)


def replace_all(text, d):
    """Allows you to replace multiple strings. It uses the key of the given dictionary d to match a string in the text
    and the associated value as replacement. E.g. d = {"hi": "bye", "no": "yes"} will replace hi with bye and no with
    yes."""
    for i, j in d.items():
        text = text.replace(i, j)
    return text


def createmongo(database, collection):
    """Connects to given database and returns specified collection."""
    client = MongoClient()
    db = getattr(client, database)
    collection = getattr(db, collection)
    return collection


def grep(path, text):
    """grep wrapper"""
    p1 = Popen(["grep", "-lR", text, path], stdout=PIPE)
    fn = p1.communicate()[0].decode("UTF-8").split()
    return fn


def liget(l, idx, default=None):
    """Tries to get element of list by index, similar to dict.get(). If it fails it returns default"""
    try:
        return l[idx]
    except IndexError:
        return default


def isempty(fn, isfile=None):
    """Returns True if file is empty, if not empty False and if the file doesn't exist None."""
    try:
        res = (os.stat(fn).st_size == 0)
        if isfile:
            if os.path.isfile(fn):
                return res
        else:
            return res
    except:
        return None


def consecutive_comb(li):
    """Alternatively:
    for x, y in itertools.combinations(range(len(li) + 1), 2):
        yield li[x:y]
    """
    combs= list()
    for x in range(len(li)):
        for y in range(len(li)):
             z = li[x:y+1]
             if z:
                 combs.append(z)
    return combs


class DefaultOrderedDict(OrderedDict):
    """ Source: http://stackoverflow.com/a/6190500/562769"""

    def __init__(self, default_factory=None, *a, **kw):
        if (default_factory is not None and
           not isinstance(default_factory, Callable)):
            raise TypeError('first argument must be callable')
        OrderedDict.__init__(self, *a, **kw)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return OrderedDict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __reduce__(self):
        if self.default_factory is None:
            args = tuple()
        else:
            args = self.default_factory,
        return type(self), args, None, None, self.items()

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        return type(self)(self.default_factory, self)

    def __deepcopy__(self, memo):
        import copy
        return type(self)(self.default_factory,
                          copy.deepcopy(self.items()))

    def __repr__(self):
        return 'OrderedDefaultDict(%s, %s)' % (self.default_factory,
                                               OrderedDict.__repr__(self))


def rchown(path, user, group):
    """Recursively chowns given path with given user/group"""
    p = Popen(["chown", "-R", "%s:%s" % (user, group), path], stdout=PIPE, stderr=PIPE)
    o, e = p.communicate()
    if e:
        log.error(e)


class Map(dict):
    """Extends the dictionary object, so that you can access the dictionary keys like attributes.

    Example: m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    Then you'd be able to access the dictionary as such: `person.age`. So it's a convenience class.
    Source: http://stackoverflow.com/a/32107024
    """ 
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


def ismount_remote(host, path):
    """Checks if a directory is mounted on a host accessible with SSH.

    Alternatively with shlex.quote: ["ssh", host, "mountpoint {}".format(shlex.quote(path))])
    """
    status = subprocess.call(
        ["ssh", host, "mountpoint", path])
    if status == 0:
        return True
    if status == 1:
        return False
    raise Exception('SSH failed')
