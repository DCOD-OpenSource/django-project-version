# -*- coding: utf-8 -*-

# django-djversion
# tests/test_rest.py


from typing import List  # pylint: disable=W0611

from django.http import HttpRequest
from django.test import TestCase
from rest_framework.response import Response

from djversion.rest import VersionView


__all__ = ["VersionViewTest"]  # type: List[str]


class VersionViewTest(TestCase):
    """
    Version REST view tests.
    """

    def test_get(self) -> None:
        """
        Method must return response containing version.

        :return: nothing.
        :rtype: None.
        """

        request = HttpRequest()  # type: HttpRequest
        request.method = "GET"

        view = VersionView().as_view()
        result = view(request=request)  # type: Response

        self.assertDictEqual(d1=result.data, d2={"version": "1.0.1 (Aug. 24, 1991)"})
