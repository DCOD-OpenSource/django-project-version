# -*- coding: utf-8 -*-

# django-project-version
# tests/settings.py


import sys
import pathlib
from datetime import date
from random import SystemRandom
from typing import Dict, List, Union


# black magic to use imports from library code
path = pathlib.Path(__file__).absolute()
project = path.parent.parent.parent
sys.path.insert(0, str(project))

# secret key
SECRET_KEY: str = "".join(
    [
        SystemRandom().choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")
        for i in range(50)
    ]
)

# configure databases
DATABASES: Dict[str, Dict[str, str]] = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

# configure templates
TEMPLATES: List[Dict[str, Union[str, List[str], bool, Dict[str, str]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]


# add testing related apps
INSTALLED_APPS: List[str] = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "djversion",
]

# configure urls
ROOT_URLCONF: str = "djversion.urls"

# drf settings
REST_FRAMEWORK: Dict[str, List[str]] = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"]
}


# djversion settings
DJVERSION_VERSION: str = "1.0.1"
DJVERSION_UPDATED: date = date(1991, 8, 24)
DJVERSION_FORMAT_STRING: str = "{version} ({updated})"  # noqa: FS003
