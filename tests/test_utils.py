# -*- coding: utf-8 -*-

# django-djversion
# tests/test_utils.py


import pathlib
import shutil
from typing import List  # pylint: disable=W0611

from django.test import TestCase
from django.test.utils import override_settings
from django.utils import translation
import git

from djversion.conf import settings
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

    @override_settings(
        DJVERSION_VERSION=None,
        DJVERSION_UPDATED=None,
        DJVERSION_GIT_REPO_PATH="./tmp",
        DJVERSION_GIT_USE_TAG=True,
    )
    def test_get_version__with_git_tag(self) -> None:
        """
        Util must return current tag from git repo from path.

        :return: nothing.
        :rtype: None.
        """

        path = pathlib.Path(settings.DJVERSION_GIT_REPO_PATH)  # type: ignore
        test = path.joinpath("TEST")  # type: pathlib.Path
        repo = git.Repo.init(str(path.absolute()))  # type: git.Repo
        with repo.config_writer() as config:
            author = git.Actor(name="TEST", email="test@example.com")  # type: git.Actor
            committer = git.Actor(
                name="TEST", email="test@example.com"
            )  # type: git.Actor
            config.set_value(section="user", option="name", value="TEST")
            config.set_value(section="user", option="email", value="test@example.com")
            test.absolute().open("wb").close()
            repo.index.add([str(test.absolute())])
            repo.index.commit(message="TEST", author=author, committer=committer)
            repo.create_tag("0.0.1", message="v0.0.1")
            config.write()
            config.release()
        version = get_version()  # type: str
        shutil.rmtree(path)

        self.assertEqual(first=version, second="0.0.1")

    @override_settings(
        DJVERSION_VERSION=None,
        DJVERSION_UPDATED=None,
        DJVERSION_GIT_REPO_PATH="./tmp",
        DJVERSION_GIT_USE_COMMIT=True,
    )
    def test_get_version__with_git_commit(self) -> None:
        """
        Util must return last commit from git repo from path.

        :return: nothing.
        :rtype: None.
        """

        path = pathlib.Path(settings.DJVERSION_GIT_REPO_PATH)  # type: ignore
        test = path.joinpath("TEST")  # type: pathlib.Path
        repo = git.Repo.init(str(path.absolute()))  # type: git.Repo
        with repo.config_writer() as config:
            author = git.Actor(name="TEST", email="test@example.com")  # type: git.Actor
            committer = git.Actor(
                name="TEST", email="test@example.com"
            )  # type: git.Actor
            config.set_value(section="user", option="name", value="TEST")
            config.set_value(section="user", option="email", value="test@example.com")
            test.absolute().open("wb").close()
            repo.index.add([str(test.absolute())])
            commit = repo.index.commit(
                message="TEST", author=author, committer=committer
            )
            config.write()
            config.release()
        version = get_version()  # type: str
        shutil.rmtree(path)

        self.assertEqual(first=version, second=commit.hexsha)
