from typing import List, Union

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver

from djversion.rest import VersionView


__all__: List[str] = ["urlpatterns"]


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    re_path(r"^$", VersionView.as_view(), name="version-view")
]
