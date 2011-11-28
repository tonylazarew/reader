#!/usr/bin/env python

from distutils.core import setup

setup(
    name="readerd",
    version='0.1',
    description="Reader daemon application",
    author="Anton Lazarev",
    author_email="tony@lazarew.me",
    url="http://github.com/tonylazarew/reader",
    packages=["readerd"],
    scripts=["bin/readerd"],
)
