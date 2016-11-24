from setuptools import setup
from pathlib import Path

here = Path(__file__).resolve().parent


setup(
    name='sorna-common',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.6.0.dev0',
    description='Sorna common libraries',
    long_description='',
    url='https://github.com/lablup/sorna-common',
    author='Lablup Inc.',
    author_email='joongi@lablup.com',
    license='LGPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Environment :: No Input/Output (Daemon)',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],

    packages=['sorna.proto', 'sorna'],
    namespace_packages=['sorna'],

    install_requires=['simplejson', 'pyzmq', 'aiozmq',
                      'aiohttp', 'async_timeout'],
    extras_require={
        'dev': [],
        'test': [],
    },
    data_files=[],

    entry_points={
        'console_scripts': [],
    },
)
