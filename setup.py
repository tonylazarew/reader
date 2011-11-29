#!/usr/bin/env python

from distutils.core import setup

setup(
    name="Reader",
    version='0.1',
    description="Reader project is a standalone web-based application which "
                "provides an easy way to gather all your social feeds into "
                "your own server.",
    author="Anton Lazarev",
    author_email="tony@lazarew.me",
    url="http://github.com/tonylazarew/reader",
    packages=[
        "readerd",
        "readerd.scripts",
        "readerd.test",
        "readerd.test.unit",
    ],
    scripts=[
        "bin/readerd"
    ],
)
