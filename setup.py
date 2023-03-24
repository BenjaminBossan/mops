#! /usr/bin/env python
# License: 3-clause BSD
import builtins

from setuptools import setup


VERSION = "0.0.0"

DISTNAME = "mops"
DESCRIPTION = "nothing"


def setup_package():
    metadata = dict(
        version=VERSION,
        python_requires=">=3.7",
        install_requires=[],
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
