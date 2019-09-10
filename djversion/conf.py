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

    class Meta:

        prefix = "djversion"  # type: str
