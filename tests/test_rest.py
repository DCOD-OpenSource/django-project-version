# -*- coding: utf-8 -*-

# django-djversion
# tests/test_rest.py


from typing import List

from django.test import TestCase
from django.http import HttpRequest
from rest_framework.response import Response

from djversion.rest import VersionView


__all__: List[str] = ["VersionViewTest"]


class VersionViewTest(TestCase):
    """Version REST view tests."""

    def test_get(self) -> None:
        """Method must return response containing version."""
        request: HttpRequest = HttpRequest()
        request.method = "GET"

        view = VersionView().as_view()
        result: Response = view(request=request)

        self.assertDictEqual(d1=result.data, d2={"version": "1.0.1 (Aug. 24, 1991)"})
