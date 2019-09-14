# -*- coding: utf-8 -*-

# django-project-version
# djversion/urls.py


from typing import List, Union  # pylint: disable=W0611

from django.conf.urls import url
from django.urls.resolvers import URLPattern, URLResolver  # pylint: disable=W0611

from djversion.rest import VersionView


__all__ = ["urlpatterns"]  # type: List[str]


urlpatterns = [
    url(r"^$", VersionView.as_view(), name="version-view")
]  # type: List[Union[URLPattern, URLResolver]]
