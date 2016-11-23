# Copyright (c) 2013 Simplistix Ltd, 2015-2016 Chris Withers
# See license.txt for license details.

import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

setup(
    name='mush',
    version='2.5.0',
    author='Chris Withers',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description="Type-based dependency injection for scripts.",
    long_description=open(
            os.path.join(base_dir, 'docs', 'description.txt')
    ).read(),
    url='http://pypi.python.org/pypi/mush',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=['nose', 'nose-cov', 'coveralls', 'mock', 'manuel', 'testfixtures',
              'argparse', 'nose-fixes'],
        build=['sphinx', 'pkginfo', 'setuptools-git', 'wheel', 'twine']
    ))
