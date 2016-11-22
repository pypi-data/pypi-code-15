from setuptools import setup

setup(
    name='diandao',
    version="0.2.15",
    url='https://git.oschina.net/diandao/pylib',
    license='MIT',
    author='idollo',
    author_email='stone58@qq.com',
    description='diandao python libs.',
    long_description=__doc__,
    packages=['diandao', 'diandao.flask'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask==0.10.1',
        'Flask-Script==2.0.5',
        'SQLAlchemy==1.0.9',
        'redis>=2.10.5',
        'hiredis==0.2.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
