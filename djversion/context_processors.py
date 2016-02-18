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
    Return formatted version string named as 'VERSION' to context.
    """

    return {
        "VERSION": get_version(),
    }
