import contextlib
from io import StringIO
from typing import List

from django.test import TestCase
from django.core.management import call_command


__all__: List[str] = ["PrintVersionManagementCommandTest"]


class PrintVersionManagementCommandTest(TestCase):
    """Print version management command tests."""

    def test_handle(self) -> None:
        """Must return version to stdout."""
        out = StringIO()

        with contextlib.redirect_stdout(out):
            call_command("print-version")

        result = out.getvalue().strip()

        self.assertEqual(first=result, second="1.0.1 (Aug. 24, 1991)")
