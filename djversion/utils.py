# -*- coding: utf-8 -*-

# django-project-version
# djversion/utils.py

from __future__ import unicode_literals

from datetime import date, datetime

from django.templatetags.l10n import localize

from djversion.settings import VERSION, UPDATED, FORMAT_STRING

__all__ = ["get_version", ]


def get_version():
    """
    Return formatted version string.
    """

    if all([VERSION, UPDATED, any([isinstance(UPDATED, date), isinstance(UPDATED, datetime), ]), ]):

        return FORMAT_STRING.format(**{"version": VERSION, "updated": UPDATED, })
    elif VERSION:

        return VERSION
    elif UPDATED:

        return localize(UPDATED) if any([isinstance(UPDATED, date), isinstance(UPDATED, datetime), ]) else ""
    else:

        return ""
