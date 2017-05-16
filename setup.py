#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-project-version
# setup.py

from setuptools import (
    setup,
    find_packages,
)


# metadata
VERSION = (0, 2, 3)
__version__ = ".".join(map(str, VERSION))
setup(
    name="django-project-version",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "Django",
    ],
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="Django reusable app to show your project version",
    license="MIT",
    url="https://github.com/DCOD-OpenSource/django-project-version/",
    download_url="https://github.com/DCOD-OpenSource/django-project-version/archive/{version}.tar.gz".format(**{"version": __version__, }),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
    ]
)
