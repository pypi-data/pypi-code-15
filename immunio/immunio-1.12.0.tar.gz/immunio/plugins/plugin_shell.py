from __future__ import (
    print_function
)
import os
import subprocess
import popen2
import sys

from functools import partial
from immunio.context import get_context
from immunio.logger import log
from immunio.patcher import monkeypatch


# Set plugin name so it can be enabled and disabled.
NAME = "shell"


def add_hooks(run_hook, get_agent_func=None, timer=None):
    """
    Add hooks for shell commands.
    """
    meta = {
        "version": ".".join(map(str, sys.version_info[:3])),  # Py version
    }

    hook_os_popen(run_hook, timer)
    hook_os_system(run_hook, timer)
    hook_subprocess_Popen(run_hook, timer)
    hook_popen2(run_hook)
#    hook_popen2_popen3_init(run_hook)
#    hook_popen2_popen4_init(run_hook)

    return meta


def hook_os_popen(run_hook, timer):
    """
    Add our hook into os.popen
    """
    # Replace the original 'os.popen'
    @monkeypatch(os, 'popen', timer=timer,
                 report_name="plugin.python.shell.os_popen")
    def _our_os_popen(orig_os_popen, *args, **kwargs):
        log.debug("os.popen(%(args)s, %(kwargs)s)", {
            "args": args,
            "kwargs": kwargs,
            })
        _, loose_context, stack = get_context()
        run_hook("file_io", {
            "method": "os.popen",
            "parameters": args[:1], # just send command
            "information": kwargs,
            "stack": stack,
            "context_key": loose_context,
            "cwd": os.getcwd()
        })
        return orig_os_popen(*args, **kwargs)


def hook_os_system(run_hook, timer):
    """
    Add our hook into os.system
    """
    # Replace the original 'os.system'
    @monkeypatch(os, 'system', timer=timer,
                 report_name="plugin.python.shell.os_system")
    def _our_os_system(orig_os_system, *args, **kwargs):
        log.debug("os.system(%(args)s, %(kwargs)s)", {
            "args": args,
            "kwargs": kwargs,
            })
        _, loose_context, stack = get_context()
        run_hook("file_io", {
            "method": "os.system",
            "parameters": args[:1], # just send command
            "information": kwargs,
            "stack": stack,
            "context_key": loose_context,
            "cwd": os.getcwd()
        })
        return orig_os_system(*args, **kwargs)


def hook_subprocess_Popen(run_hook, timer):
    """
    Add our hook into subprocess.Popen
    """
    # Replace the original
    @monkeypatch(subprocess.Popen, "_execute_child", timer=timer,
                 report_name="plugin.python.shell.subprocess_execute_child")
    def _our_execute_child(orig_execute_child, *args, **kwargs):
        log.debug("subprocess.Popen._execute_child(%(args)s, %(kwargs)s)", {
            "args": args,
            "kwargs": kwargs,
            })
        # argument ten is Shell. Only run the hook if it's true
        # and the command will be interpreted by a shell
        if args[10] or kwargs.get('shell'):
            _, loose_context, stack = get_context()
            run_hook("file_io", {
                "method": "subprocess.Popen._execute_child",
                #drop the first argument which is Popen() self
                "parameters": args[1:2], # just send command
                "information": kwargs,
                "stack": stack,
                "context_key": loose_context,
                "cwd": os.getcwd()
            })
        return orig_execute_child(*args, **kwargs)


def hook_popen2(run_hook):
    def popen2_Popen_patch_init(method, orig_init, *args, **kwargs):
        log.debug("%(method)s(%(args)s, %(kwargs)s)", {
            "method": method,
            "args": args,
            "kwargs": kwargs,
            })
        # argument one is cmd. It's run via a shell if it's a string
        # no shell otherwise.
        if isinstance(args[1], basestring):
            _, loose_context, stack = get_context()
            run_hook("file_io", {
                "method": method,
                # drop the first argument which is Popen3() self
                "parameters": args[1:2], # just send command
                "information": kwargs,
                "stack": stack,
                "context_key": loose_context,
                "cwd": os.getcwd()
            })
        return orig_init(*args, **kwargs)

    monkeypatch(popen2.Popen3, "__init__")(
        partial(popen2_Popen_patch_init, 'popen2.Popen3.__init__',)
    )
    monkeypatch(popen2.Popen4, "__init__")(
        partial(popen2_Popen_patch_init, 'popen2.Popen4.__init__',)
    )

