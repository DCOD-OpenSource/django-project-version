# -*- coding: utf-8 -*-

# django-project-version
# tests/templatetags/test_djversion_tags.py


from typing import List  # pylint: disable=W0611

from django.test import TestCase

from djversion.templatetags.djversion_tags import project_version


__all__ = ["ProjectVersionTemplatetagTest"]  # type: List[str]


class ProjectVersionTemplatetagTest(TestCase):
    """
    Project version templatetag tests.
    """

    def test_project_version(self) -> None:
        """
        Must return formatted version tag.
        """

        result = project_version()  # type: str

        self.assertIsInstance(obj=result, cls=str)
        self.assertEqual(first=result, second="1.0.1 (Aug. 24, 1991)")
