from django.core.management.base import BaseCommand
from djversion.utils import get_version
import sys


class Command(BaseCommand):
    help = 'Print project version'

    def handle(self, *args, **kwargs):
        print(get_version())
        sys.exit(0)

