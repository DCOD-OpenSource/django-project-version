# -*- coding: utf-8 -*-

# django-project-version
# djversion/templatetags/djversion_tags.py


from __future__ import unicode_literals

from django import template

from djversion.utils import get_version


__all__ = [
    "project_version",
]


register = template.Library()


@register.simple_tag()
def project_version():
    """
    Formatted version string templatetag.

    Returns:
        str: string with project version or empty string.
    """

    return get_version()
