from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

setup(
    name = 'sysexecute',
    packages = ['sysexecute'], # this must be the same as the name above
    version = '1.0.3',
    description = 'A library for simplified executing of system commands',
    long_description = long_description,
    author = 'Jason Harris',
    author_email = 'jason@jasonfharris.com',
    license='MIT',
    url = 'https://github.com/jasonfharris/sysexecute',
    download_url = 'https://github.com/jasonfharris/sysexecute/tarball/1.0.3',
    keywords = ['execute', 'shell', 'system'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: System :: Shells',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
        ],
    install_requires = ['argparse', 'argcomplete']
)