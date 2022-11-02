#!/usr/bin/env python3
import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


requirements = [
    # use environment.yml
]


setup(
    name="mypackage",
    version="0.5.0",
    url="https://github.com/camerart/mypackage",
    author="Fred Qi",
    author_email="fred.qi@ieee.org",
    description="Deep learning template with pytorch and lightning.",
    long_description=read("README.md"),
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "mypackage=mypackage.cli:main"
        ]
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
)
