# -*- coding: utf-8 -*-

# django-project-version
# tests/settings.py


import sys
import random
import pathlib
from datetime import date
from typing import Dict, List, Union  # pylint: disable=W0611


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "".join(
    [
        random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")  # nosec
        for i in range(50)
    ]
)  # type: str

# configure databases
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}  # type: Dict[str, Dict[str, str]]

# configure templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]  # type: List[Dict[str, Union[str, List[str], bool, Dict[str, str]]]]


# add testing related apps
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django_nose",
    "djversion",
]  # type: List[str]

# add nose test runner
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"  # type: str

# configure nose test runner
NOSE_ARGS = [
    "--rednose",
    "--force-color",
    "--with-timer",
    "--with-doctest",
    "--with-coverage",
    "--cover-inclusive",
    "--cover-erase",
    "--cover-package=djversion",
    "--logging-clear-handlers",
]  # type: List[str]

# configure urls
ROOT_URLCONF = "djversion.urls"  # type: str

# drf settings
REST_FRAMEWORK = {"DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"]}


# djversion settings
DJVERSION_VERSION = "1.0.1"  # type: str
DJVERSION_UPDATED = date(1991, 8, 24)  # type: date
DJVERSION_FORMAT_STRING = "{version} ({updated})"  # type: str
