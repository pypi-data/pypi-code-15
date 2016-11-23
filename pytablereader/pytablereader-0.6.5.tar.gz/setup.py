import os.path
import setuptools
import sys


REQUIREMENT_DIR = "requirements"

needs_pytest = set(["pytest", "test", "ptr"]).intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []


with open("README.rst") as fp:
    long_description = fp.read()

with open(os.path.join("docs", "pages", "introduction", "summary.txt")) as f:
    summary = f.read()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_require = [line.strip() for line in f if line.strip()]

setuptools.setup(
    name="pytablereader",
    version="0.6.5",
    url="https://github.com/thombashi/pytablereader",

    author="Tsuyoshi Hombashi",
    author_email="gogogo.vm@gmail.com",
    description=summary,
    include_package_data=True,
    install_requires=install_requires,
    keywords=[
        "table", "reader",
        "CSV", "Excel", "HTML", "JSON", "Markdown", "MediaWiki",
    ],
    long_description=long_description,
    license="MIT License",
    packages=setuptools.find_packages(exclude=["test*"]),
    setup_requires=pytest_runner,
    tests_require=tests_require,

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
