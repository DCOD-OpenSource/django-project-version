# -*- coding: utf-8 -*-

# django-project-version
# djversion/utils.py


from datetime import date, datetime
from typing import List  # pylint: disable=W0611

from django.templatetags.l10n import localize

from djversion.conf import settings


__all__ = ["get_version"]  # type: List[str]


def get_version() -> str:
    """
    Format version string.

    :return: formatted version string.
    :rtype: str.
    """

    if all(
        [
            settings.DJVERSION_VERSION,
            settings.DJVERSION_UPDATED,
            any(
                [
                    isinstance(settings.DJVERSION_UPDATED, date),
                    isinstance(settings.DJVERSION_UPDATED, datetime),
                ]
            ),
            settings.DJVERSION_FORMAT_STRING,
        ]
    ):

        return settings.DJVERSION_FORMAT_STRING.format(
            **{
                "version": settings.DJVERSION_VERSION,
                "updated": localize(settings.DJVERSION_UPDATED),
            }
        )
    elif settings.DJVERSION_VERSION:

        return settings.DJVERSION_VERSION
    elif settings.DJVERSION_UPDATED:

        return (
            localize(settings.DJVERSION_UPDATED)
            if any(
                [
                    isinstance(settings.DJVERSION_UPDATED, date),
                    isinstance(settings.DJVERSION_UPDATED, datetime),
                ]
            )
            else ""
        )
    else:

        return ""
