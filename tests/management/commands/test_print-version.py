# -*- coding: utf-8 -*-

# django-project-version
# tests/management/commands/test_print-version.py
import contextlib
from io import StringIO
from typing import List  # pylint: disable=W0611

from django.core.management import call_command
from django.test import TestCase


__all__ = ["PrintVersionManagementCommandTest"]  # type: List[str]


class PrintVersionManagementCommandTest(TestCase):
    """
    Print version management command tests.
    """

    def test_handle(self) -> None:
        """
        Must return version to stdout.

        :return: nothing.
        :rtype: None.
        """

        out = StringIO()

        with contextlib.redirect_stdout(out):
            call_command("print-version")

        result = out.getvalue().strip()

        self.assertEqual(first=result, second="1.0.1 (Aug. 24, 1991)")
