# -*- coding: utf-8 -*-

# django-djversion
# tests/test_utils.py


from typing import List  # pylint: disable=W0611

from django.test import TestCase
from django.test.utils import override_settings
from django.utils import translation

from djversion.utils import get_version


__all__ = ["GetVersionUtilTest"]  # type: List[str]


class GetVersionUtilTest(TestCase):
    """
    get_version util tests.
    """

    def test_get_version(self) -> None:
        """
        Util must return current version and updated date formatted using format string.

        :return: nothing.
        :rtype: None.
        """

        self.assertEqual(first=get_version(), second="1.0.1 (Aug. 24, 1991)")

    @override_settings(DJVERSION_FORMAT_STRING="{updated}: {version}")
    def test_get_version__with_custom_format_string(self) -> None:
        """
        Util must return current version and updated date formatted using custom format string.  # noqa: E501

        :return: nothing.
        :rtype: None.
        """

        with translation.override("en"):
            self.assertEqual(first=get_version(), second="Aug. 24, 1991: 1.0.1")

    @override_settings(DJVERSION_UPDATED=None)
    def test_get_version__without_updated(self) -> None:
        """
        Util must return current version.

        :return: nothing.
        :rtype: None.
        """

        with translation.override("en"):
            self.assertEqual(first=get_version(), second="1.0.1")

    @override_settings(DJVERSION_VERSION=None)
    def test_get_version__without_version(self) -> None:
        """
        Util must return updated.

        :return: nothing.
        :rtype: None.
        """

        with translation.override("en"):
            self.assertEqual(first=get_version(), second="Aug. 24, 1991")

    @override_settings(DJVERSION_VERSION=None, DJVERSION_UPDATED=None)
    def test_get_version__without_settings(self) -> None:
        """
        Util must return empty string.

        :return: nothing.
        :rtype: None.
        """

        with translation.override("en"):
            self.assertEqual(first=get_version(), second="")
