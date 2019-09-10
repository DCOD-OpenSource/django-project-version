# -*- coding: utf-8 -*-

# django-project-version
# tests/settings.py


import pathlib
import sys
from typing import Dict, List, Union  # pylint: disable=W0611


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "django-project-version-test-key"  # type: str

# configure databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "django-project-version-tests.sqlite3",
    }
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
INSTALLED_APPS = ["django_nose", "djversion"]  # type: List[str]

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

# djversion settings
