# -*- coding: utf-8 -*-

# django-project-version
# djversion/context_processors.py


from typing import Dict, List  # pylint: disable=W0611

from django.http import HttpRequest

from djversion.utils import get_version


__all__ = ["version"]  # type: List[str]


def version(request: HttpRequest) -> Dict[str, str]:
    """
    Return formatted version string named as "VERSION" to context.

    :param request: django HTTP request object
    :type request: HttpRequest
    :return: formatted version string named as "VERSION"
    :rtype: Dict[str, str]
    """

    return {"VERSION": get_version()}
