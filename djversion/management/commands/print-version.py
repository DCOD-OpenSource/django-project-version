from typing import Any, Dict, List

from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

from djversion.utils import get_version


__all__: List[str] = ["Command"]


class Command(BaseCommand):
    """Version management command."""

    help: str = str(_("Print project version"))  # noqa: A003

    def handle(self, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Perform command.

        :param args: additional args
        :type args: List[Any]
        :param kwargs: additional args
        :type kwargs: Dict[str, Any]
        """
        self.stdout.write(get_version())
