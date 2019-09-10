# -*- coding: utf-8 -*-

# django-project-version
# djversion/utils.py


from datetime import date, datetime
from typing import List  # pylint: disable=W0611

from django.templatetags.l10n import localize

from djversion.settings import UPDATED, VERSION, FORMAT_STRING


__all__ = ["get_version"]  # type: List[str]


def get_version() -> str:
    """
    Format version string.

    :return: formatted version string.
    :rtype: str.
    """

    if all(
        [
            VERSION,
            UPDATED,
            any([isinstance(UPDATED, date), isinstance(UPDATED, datetime)]),
        ]
    ):

        return FORMAT_STRING.format(**{"version": VERSION, "updated": UPDATED})
    elif VERSION:

        return VERSION
    elif UPDATED:

        return (
            localize(UPDATED)
            if any([isinstance(UPDATED, date), isinstance(UPDATED, datetime)])
            else ""
        )
    else:

        return ""
