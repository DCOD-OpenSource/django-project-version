# -*- coding: utf-8 -*-

# django-project-version
# djversion/templatetags/djversion_tags.py


from typing import List  # pylint: disable=W0611

from django import template

from djversion.utils import get_version


__all__ = ["project_version"]  # type: List[str]


register = template.Library()


@register.simple_tag()
def project_version() -> str:
    """
    Formatted version string templatetag.

    :return: formatted project version
    :rtype: str
    """

    return get_version()
