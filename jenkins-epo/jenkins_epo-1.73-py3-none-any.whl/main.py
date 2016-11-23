# This file is part of jenkins-epo
#
# jenkins-epo is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or any later version.
#
# jenkins-epo is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# jenkins-epo.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import asyncio
import bdb
import functools
import inspect
import logging
import sys


from .bot import Bot
from .cache import CACHE
from .github import GITHUB
from .settings import SETTINGS
from . import procedures


logger = logging.getLogger('jenkins_epo')


def loop(wrapped):
    if SETTINGS.LOOP:
        @asyncio.coroutine
        def wrapper(*args, **kwargs):
            while True:
                res = wrapped(*args, **kwargs)
                if asyncio.iscoroutine(res):
                    yield from res

                logger.info("Looping in %s seconds", SETTINGS.LOOP)
                yield from asyncio.sleep(SETTINGS.LOOP)
        functools.update_wrapper(wrapper, wrapped)
        return wrapper
    else:
        return wrapped


@loop
@asyncio.coroutine
def bot():
    """Poll GitHub to find something to do"""
    yield from procedures.whoami()
    bot = Bot(queue_empty=None)

    for head in procedures.iter_heads():
        try:
            head.repository.load_settings()
        except Exception:
            logger.exception("Failed to load %s settings.", head.repository)
            continue

        head.last_commit.fetch_payload()
        if head.last_commit.is_outdated:
            logger.debug(
                'Skipping %s because older than %s weeks.',
                head, SETTINGS.COMMIT_MAX_WEEKS,
            )
            continue

        logger.info("Working on %s.", head)
        try:
            bot.run(head)
        except Exception:
            if SETTINGS.LOOP:
                logger.exception("Failed to process %s:", head)
            else:
                raise

    CACHE.purge()
    CACHE.save()
    logger.info(
        "GitHub poll done. %s remaining API calls.",
        GITHUB.x_ratelimit_remaining,
    )


def list_extensions():
    bot = Bot()
    for extension in bot.extensions:
        print(extension.stage, extension.name)


@asyncio.coroutine
def list_heads():
    """List heads to build"""
    yield from procedures.whoami()
    for head in procedures.iter_heads():
        print(head)


def command_exitcode(command_func):
    try:
        command_func()
    except bdb.BdbQuit:
        logger.debug('Graceful exit from debugger')
        return 0
    except Exception:
        logger.exception('Unhandled error')

        if not SETTINGS.DEBUG:
            return 1

        try:
            import ipdb as pdb
        except ImportError:
            import pdb

        pdb.post_mortem(sys.exc_info()[2])
        logger.debug('Graceful exit from debugger')

        return 1


def main(argv=None):
    argv = argv or sys.argv
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', metavar='COMMAND')
    for command in [bot, list_extensions, list_heads]:
        subparser = subparsers.add_parser(
            command.__name__.replace('_', '-'),
            help=inspect.cleandoc(command.__doc__ or '').split('\n')[0],
        )
        subparser.set_defaults(command_func=command)

    args = parser.parse_args(argv)
    try:
        command_func = args.command_func
    except AttributeError:
        command_func = parser.print_usage

    if asyncio.iscoroutinefunction(command_func):
        def run_async():
            loop = asyncio.get_event_loop()
            task = loop.create_task(command_func())
            try:
                loop.run_until_complete(task)
            except BaseException:
                if task.done():
                    task.exception()  # Consume task exception
                else:
                    task.cancel()
                loop.close()
                raise

        sys.exit(command_exitcode(run_async))
    else:
        sys.exit(command_exitcode(command_func))
