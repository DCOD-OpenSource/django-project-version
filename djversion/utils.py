from typing import List
from datetime import date, datetime

from django.templatetags.l10n import localize

from djversion.conf import settings


# trying to import git lib in case of this functionality is unnecessary
try:
    from git import Repo
except ImportError:
    Repo = None  # type: ignore


__all__: List[str] = ["get_version"]


def get_version() -> str:  # noqa: CCR001
    """
    Format version string.

    :return: formatted version string
    :rtype: str
    """
    version = ""
    if all(
        [
            settings.DJVERSION_VERSION,
            settings.DJVERSION_UPDATED,
            any(
                [
                    isinstance(settings.DJVERSION_UPDATED, date),
                    isinstance(settings.DJVERSION_UPDATED, datetime),
                ]
            ),
            settings.DJVERSION_FORMAT_STRING,
        ]
    ):
        version = settings.DJVERSION_FORMAT_STRING.format(
            version=settings.DJVERSION_VERSION,
            updated=localize(settings.DJVERSION_UPDATED),
        )
    elif settings.DJVERSION_VERSION:
        version = settings.DJVERSION_VERSION
    elif settings.DJVERSION_UPDATED:
        version = (
            localize(settings.DJVERSION_UPDATED)
            if any(
                [
                    isinstance(settings.DJVERSION_UPDATED, date),
                    isinstance(settings.DJVERSION_UPDATED, datetime),
                ]
            )
            else ""
        )
    elif all([Repo, settings.DJVERSION_GIT_REPO_PATH]):  # type: ignore
        try:
            repo = Repo(settings.DJVERSION_GIT_REPO_PATH)  # type: ignore
            if settings.DJVERSION_GIT_USE_TAG:  # type: ignore
                tag = next(
                    (tag for tag in repo.tags if tag.commit == repo.head.commit), None
                )
                version = tag.name if tag else ""
            elif settings.DJVERSION_GIT_USE_COMMIT:  # type: ignore
                version = repo.head.commit.hexsha if repo.head.commit else ""
            else:
                version = ""
        except Exception:  # noqa: PIE786
            version = ""
    else:
        version = ""

    return version  # noqa: R504
