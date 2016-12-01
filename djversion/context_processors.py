# -*- coding: utf-8 -*-

# django-project-version
# djversion/context_processors.py

from __future__ import unicode_literals

from djversion.utils import get_version


__all__ = [
    "version",
]


def version(request):
    """
    Return formatted version string named as "VERSION" to context.
    Args:
        request: (django.http.request.HttpRequest) django request instance.
    Returns:
        dict: dict with "VERSION" key with value of project version.
    """

    return {
        "VERSION": get_version(),
    }
