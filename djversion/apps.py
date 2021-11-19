# -*- coding: utf-8 -*-

# django-project-version
# djversion/apps.py


from typing import List

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["DjangoDjversionConfig"]


class DjangoDjversionConfig(AppConfig):
    """Application config."""

    name: str = "djversion"
    verbose_name: str = _("Django project version")
