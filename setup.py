#!/usr/bin/env python

from distutils.core import setup

setup(
    name="Reader",
    version='0.1',
    description=
        "Reader project is a standalone web-based application and backend "
        "service which provides an easy way to gather all your social feeds "
        "into your own server.",
    author="Anton Lazarev",
    author_email="tony@lazarew.me",
    url="http://github.com/tonylazarew/reader",
    packages=[
        "readerpr",
        "readerpr.daemon",
        "readerpr.daemon.contentplugins",
        "readerpr.scripts",
        "readerpr.test",
        "readerpr.test.unit",
        "readerpr.webface",
    ],
    scripts=[
        "bin/readerd",
        "bin/rwebface"
    ],
)
