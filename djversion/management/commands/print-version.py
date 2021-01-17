# -*- coding: utf-8 -*-

# django-project-version
# djversion/management/commands/print-version.py


from typing import Any, Dict, List  # pylint: disable=W0611

from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

from djversion.utils import get_version


__all__ = ["Command"]  # type: List[str]


class Command(BaseCommand):
    """
    Version management command.
    """

    help = str(_("Print project version"))

    def handle(self, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Perform command.

        :param args: additional args
        :type args: List[Any]
        :param kwargs: additional args
        :type kwargs: Dict[str, Any]
        """

        self.stdout.write(get_version())
