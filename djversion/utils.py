# -*- coding: utf-8 -*-

# django-project-version
# djversion/utils.py


from datetime import date, datetime
from typing import List  # pylint: disable=W0611

from django.templatetags.l10n import localize

from djversion.conf import settings


# trying to import git lib in case of this functionality is unnecessary
try:
    from git import Repo
except ImportError:
    Repo = None


__all__ = ["get_version"]  # type: List[str]


def get_version() -> str:
    """
    Format version string.

    :return: formatted version string
    :rtype: str
    """

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

        return settings.DJVERSION_FORMAT_STRING.format(
            **{
                "version": settings.DJVERSION_VERSION,
                "updated": localize(settings.DJVERSION_UPDATED),
            }
        )
    elif settings.DJVERSION_VERSION:

        return settings.DJVERSION_VERSION
    elif settings.DJVERSION_UPDATED:

        return (
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

                return tag.name if tag else ""
            elif settings.DJVERSION_GIT_USE_COMMIT:  # type: ignore

                return repo.head.commit.hexsha if repo.head.commit else ""
            else:

                return ""
        except Exception:

            return ""
    else:

        return ""
