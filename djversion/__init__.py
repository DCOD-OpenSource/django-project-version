# -*- coding: utf-8 -*-

# django-project-version
# djversion/__init__.py

from __future__ import unicode_literals

__all__ = [
    "models",
    "templatetags",
    "settings",
    "context_processors",
    "utils",
    "apps",
    "default_app_config",
]


default_app_config = "djversion.apps.Config"
