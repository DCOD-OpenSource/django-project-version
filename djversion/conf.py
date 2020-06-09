# -*- coding: utf-8 -*-

# django-project-version
# djversion/conf.py


from datetime import date, datetime  # pylint: disable=W0611
from typing import List, Union, Optional  # pylint: disable=W0611

from appconf import AppConf
from django.conf import settings


__all__ = ["settings"]  # type: List[str]


class DjangoDjversionAppConf(AppConf):
    """
    Django djversion settings.
    """

    VERSION = getattr(settings, "DJVERSION_VERSION", None)  # type: Optional[str]
    UPDATED = getattr(
        settings, "DJVERSION_UPDATED", None
    )  # type: Optional[Union[datetime, date]]
    FORMAT_STRING = getattr(
        settings, "DJVERSION_FORMAT_STRING", "{version} ({updated})"
    )  # type: str
    GIT_REPO_PATH = getattr(
        settings, "DJVERSION_GIT_REPO_PATH", None
    )  # type: Optional[str]
    GIT_USE_TAG = getattr(settings, "DJVERSION_GIT_USE_TAG", False)  # type: bool
    GIT_USE_COMMIT = getattr(settings, "DJVERSION_GIT_USE_COMMIT", False)  # type: bool

    class Meta:
        """
        Config settings.
        """

        prefix = "djversion"  # type: str
