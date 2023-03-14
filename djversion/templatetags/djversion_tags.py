from typing import List

from django import template

from djversion.utils import get_version


__all__: List[str] = ["project_version"]


register = template.Library()


@register.simple_tag()
def project_version() -> str:
    """
    Formatted version string templatetag.

    :return: formatted project version
    :rtype: str
    """
    return get_version()
