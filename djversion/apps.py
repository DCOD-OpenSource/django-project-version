# -*- coding: utf-8 -*-

# django-project-version
# djversion/apps.py


from typing import List  # pylint: disable=W0611

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__ = ["DjangoDjversionConfig"]  # type: List[str]


class DjangoDjversionConfig(AppConfig):
    """
    Application config.
    """

    name = "djversion"  # type: str
    verbose_name = _("Django project version")  # type: str
