# -*- coding: utf-8 -*-

# django-project-version
# tests/test_context_processors.py


from typing import Dict, List

from django.test import TestCase
from django.http import HttpRequest

from djversion.context_processors import version


__all__: List[str] = ["VersionContextProcessorTest"]


class VersionContextProcessorTest(TestCase):
    """Version context processor tests."""

    def test_version(self) -> None:
        """Must return formatted new context variable with version."""
        request: HttpRequest = HttpRequest()
        result: Dict[str, str] = version(request=request)

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2={"VERSION": "1.0.1 (Aug. 24, 1991)"})
