# -*- coding: utf-8 -*-

# django-project-version
# djversion/settings.py

from __future__ import unicode_literals

from django.conf import settings

__all__ = [
    "VERSION",
    "UPDATED",
    "FORMAT_STRING",
]


VERSION = getattr(settings, "DJVERSION_VERSION", None)
UPDATED = getattr(settings, "DJVERSION_UPDATED", None)
FORMAT_STRING = getattr(settings, "DJVERSION_FORMAT_STRING", "{version} ({updated})")
