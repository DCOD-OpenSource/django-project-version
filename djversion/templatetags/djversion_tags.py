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


@register.assignment_tag()
def project_version():
    """
    Formatted version string templatetag.
    """

    return get_version()
