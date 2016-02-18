# -*- coding: utf-8 -*-

# django-project-version
# djversion/apps.py

from __future__ import unicode_literals

from django.apps import AppConfig

__all__ = ["Config", ]


class Config(AppConfig):

    name = "djversion"
    verbose_name = "Django project version"
