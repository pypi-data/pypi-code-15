"""Unit tests for flake8.options.config.MergedConfigParser."""
import os

import mock
import pytest

from flake8.options import config
from flake8.options import manager


@pytest.fixture
def optmanager():
    """Generate an OptionManager with simple values."""
    return manager.OptionManager(prog='flake8', version='3.0.0a1')


@pytest.mark.parametrize('args,extra_config_files', [
    (None, None),
    (None, []),
    (None, ['foo.ini']),
    ('flake8/', []),
    ('flake8/', ['foo.ini']),
])
def test_creates_its_own_config_file_finder(args, extra_config_files,
                                            optmanager):
    """Verify we create a ConfigFileFinder correctly."""
    class_path = 'flake8.options.config.ConfigFileFinder'
    with mock.patch(class_path) as ConfigFileFinder:
        parser = config.MergedConfigParser(
            option_manager=optmanager,
            extra_config_files=extra_config_files,
            args=args,
        )

    assert parser.program_name == 'flake8'
    ConfigFileFinder.assert_called_once_with(
        'flake8',
        args,
        extra_config_files or [],
    )


def test_parse_cli_config(optmanager):
    """Parse the specified config file as a cli config file."""
    optmanager.add_option('--exclude', parse_from_config=True,
                          comma_separated_list=True,
                          normalize_paths=True)
    optmanager.add_option('--ignore', parse_from_config=True,
                          comma_separated_list=True)
    parser = config.MergedConfigParser(optmanager)

    parsed_config = parser.parse_cli_config(
        'tests/fixtures/config_files/cli-specified.ini'
    )
    assert parsed_config == {
        'ignore': ['E123', 'W234', 'E111'],
        'exclude': [
            os.path.abspath('foo/'),
            os.path.abspath('bar/'),
            os.path.abspath('bogus/'),
        ]
    }


@pytest.mark.parametrize('filename,is_configured_by', [
    ('tests/fixtures/config_files/cli-specified.ini', True),
    ('tests/fixtures/config_files/no-flake8-section.ini', False),
])
def test_is_configured_by(filename, is_configured_by, optmanager):
    """Verify the behaviour of the is_configured_by method."""
    parsed_config, _ = config.ConfigFileFinder._read_config(filename)
    parser = config.MergedConfigParser(optmanager)

    assert parser.is_configured_by(parsed_config) is is_configured_by


def test_parse_user_config(optmanager):
    """Verify parsing of user config files."""
    optmanager.add_option('--exclude', parse_from_config=True,
                          comma_separated_list=True,
                          normalize_paths=True)
    optmanager.add_option('--ignore', parse_from_config=True,
                          comma_separated_list=True)
    parser = config.MergedConfigParser(optmanager)

    with mock.patch.object(parser.config_finder, 'user_config_file') as usercf:
        usercf.return_value = 'tests/fixtures/config_files/cli-specified.ini'
        parsed_config = parser.parse_user_config()

    assert parsed_config == {
        'ignore': ['E123', 'W234', 'E111'],
        'exclude': [
            os.path.abspath('foo/'),
            os.path.abspath('bar/'),
            os.path.abspath('bogus/'),
        ]
    }


def test_parse_local_config(optmanager):
    """Verify parsing of local config files."""
    optmanager.add_option('--exclude', parse_from_config=True,
                          comma_separated_list=True,
                          normalize_paths=True)
    optmanager.add_option('--ignore', parse_from_config=True,
                          comma_separated_list=True)
    parser = config.MergedConfigParser(optmanager)
    config_finder = parser.config_finder

    with mock.patch.object(config_finder, 'local_config_files') as localcfs:
        localcfs.return_value = [
            'tests/fixtures/config_files/cli-specified.ini'
        ]
        parsed_config = parser.parse_local_config()

    assert parsed_config == {
        'ignore': ['E123', 'W234', 'E111'],
        'exclude': [
            os.path.abspath('foo/'),
            os.path.abspath('bar/'),
            os.path.abspath('bogus/'),
        ]
    }


def test_merge_user_and_local_config(optmanager):
    """Verify merging of parsed user and local config files."""
    optmanager.add_option('--exclude', parse_from_config=True,
                          comma_separated_list=True,
                          normalize_paths=True)
    optmanager.add_option('--ignore', parse_from_config=True,
                          comma_separated_list=True)
    optmanager.add_option('--select', parse_from_config=True,
                          comma_separated_list=True)
    parser = config.MergedConfigParser(optmanager)
    config_finder = parser.config_finder

    with mock.patch.object(config_finder, 'local_config_files') as localcfs:
        localcfs.return_value = [
            'tests/fixtures/config_files/local-config.ini'
        ]
        with mock.patch.object(config_finder,
                               'user_config_file') as usercf:
            usercf.return_value = ('tests/fixtures/config_files/'
                                   'user-config.ini')
            parsed_config = parser.merge_user_and_local_config()

    assert parsed_config == {
        'exclude': [
            os.path.abspath('docs/')
        ],
        'ignore': ['D203'],
        'select': ['E', 'W', 'F'],
    }


@mock.patch('flake8.options.config.ConfigFileFinder')
def test_parse_isolates_config(ConfigFileManager, optmanager):
    """Verify behaviour of the parse method with isolated=True."""
    parser = config.MergedConfigParser(optmanager)

    assert parser.parse(isolated=True) == {}
    assert parser.config_finder.local_configs.called is False
    assert parser.config_finder.user_config.called is False


@mock.patch('flake8.options.config.ConfigFileFinder')
def test_parse_uses_cli_config(ConfigFileManager, optmanager):
    """Verify behaviour of the parse method with a specified config."""
    parser = config.MergedConfigParser(optmanager)

    parser.parse(cli_config='foo.ini')
    parser.config_finder.cli_config.assert_called_once_with('foo.ini')


@pytest.mark.parametrize('config_fixture_path', [
    'tests/fixtures/config_files/cli-specified.ini',
    'tests/fixtures/config_files/cli-specified-with-inline-comments.ini',
    'tests/fixtures/config_files/cli-specified-without-inline-comments.ini',
])
def test_parsed_configs_are_equivalent(optmanager, config_fixture_path):
    """Verify the each file matches the expected parsed output.

    This is used to ensure our documented behaviour does not regress.
    """
    optmanager.add_option('--exclude', parse_from_config=True,
                          comma_separated_list=True,
                          normalize_paths=True)
    optmanager.add_option('--ignore', parse_from_config=True,
                          comma_separated_list=True)
    parser = config.MergedConfigParser(optmanager)
    config_finder = parser.config_finder

    with mock.patch.object(config_finder, 'local_config_files') as localcfs:
        localcfs.return_value = [config_fixture_path]
        with mock.patch.object(config_finder,
                               'user_config_file') as usercf:
            usercf.return_value = []
            parsed_config = parser.merge_user_and_local_config()

    assert parsed_config['ignore'] == ['E123', 'W234', 'E111']
    assert parsed_config['exclude'] == [
        os.path.abspath('foo/'),
        os.path.abspath('bar/'),
        os.path.abspath('bogus/'),
    ]


@pytest.mark.parametrize('config_file', [
    'tests/fixtures/config_files/config-with-hyphenated-options.ini'
])
def test_parsed_hyphenated_and_underscored_names(optmanager, config_file):
    """Verify we find hyphenated option names as well as underscored.

    This tests for options like --max-line-length and --enable-extensions
    which are able to be specified either as max-line-length or
    max_line_length in our config files.
    """
    optmanager.add_option('--max-line-length', parse_from_config=True,
                          type='int')
    optmanager.add_option('--enable-extensions', parse_from_config=True,
                          comma_separated_list=True)
    parser = config.MergedConfigParser(optmanager)
    config_finder = parser.config_finder

    with mock.patch.object(config_finder, 'local_config_files') as localcfs:
        localcfs.return_value = [config_file]
        with mock.patch.object(config_finder,
                               'user_config_file') as usercf:
            usercf.return_value = []
            parsed_config = parser.merge_user_and_local_config()

    assert parsed_config['max_line_length'] == 110
    assert parsed_config['enable_extensions'] == ['H101', 'H235']
