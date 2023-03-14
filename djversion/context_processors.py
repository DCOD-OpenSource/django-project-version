from typing import Dict, List

from django.http import HttpRequest

from djversion.utils import get_version


__all__: List[str] = ["version"]


def version(request: HttpRequest) -> Dict[str, str]:
    """
    Return formatted version string named as "VERSION" to context.

    :param request: django HTTP request object
    :type request: HttpRequest
    :return: formatted version string named as "VERSION"
    :rtype: Dict[str, str]
    """
    return {"VERSION": get_version()}
