# -*- coding: utf-8 -*-

# django-djversion
# tests/test_utils.py


import shutil
from typing import List
from pathlib import Path

import git
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.translation import override as override_translation

from djversion.conf import settings
from djversion.utils import get_version


__all__: List[str] = ["GetVersionUtilTest"]


class GetVersionUtilTest(TestCase):
    """get_version util tests."""

    def test_get_version(self) -> None:
        """Util must return current version and updated date formatted using format string."""  # noqa: E501
        self.assertEqual(first=get_version(), second="1.0.1 (Aug. 24, 1991)")

    @override_settings(DJVERSION_FORMAT_STRING="{updated}: {version}")  # noqa: FS003
    @override_translation(language="en")
    def test_get_version__with_custom_format_string(self) -> None:
        """Util must return current version and updated date formatted using custom format string."""  # noqa: E501
        self.assertEqual(first=get_version(), second="Aug. 24, 1991: 1.0.1")

    @override_settings(DJVERSION_UPDATED=None)
    @override_translation(language="en")
    def test_get_version__without_updated(self) -> None:
        """Util must return current version."""
        self.assertEqual(first=get_version(), second="1.0.1")

    @override_settings(DJVERSION_VERSION=None)
    @override_translation(language="en")
    def test_get_version__without_version(self) -> None:
        """Util must return updated."""
        self.assertEqual(first=get_version(), second="Aug. 24, 1991")

    @override_settings(DJVERSION_VERSION=None, DJVERSION_UPDATED=None)
    @override_translation(language="en")
    def test_get_version__without_settings(self) -> None:
        """Util must return empty string."""
        self.assertEqual(first=get_version(), second="")

    @override_settings(
        DJVERSION_VERSION=None,
        DJVERSION_UPDATED=None,
        DJVERSION_GIT_REPO_PATH="./tmp",
        DJVERSION_GIT_USE_TAG=True,
    )
    def test_get_version__with_git_tag(self) -> None:
        """Util must return current tag from git repo from path."""
        path = Path(settings.DJVERSION_GIT_REPO_PATH)  # type: ignore
        test: Path = path.joinpath("TEST")
        repo: git.Repo = git.Repo.init(str(path.absolute()))
        with repo.config_writer() as config:
            config.set_value(section="user", option="name", value="TEST")
            config.set_value(section="user", option="email", value="test@example.com")
            config.write()
            config.release()
        author: git.Actor = git.Actor(name="TEST", email="test@example.com")
        committer: git.Actor = git.Actor(name="TEST", email="test@example.com")
        test.absolute().open("wb").close()
        repo.index.add([str(test.absolute())])
        repo.index.commit(message="TEST", author=author, committer=committer)
        repo.create_tag("0.0.1", message="v0.0.1")
        version: str = get_version()
        shutil.rmtree(path)

        self.assertEqual(first=version, second="0.0.1")

    @override_settings(
        DJVERSION_VERSION=None,
        DJVERSION_UPDATED=None,
        DJVERSION_GIT_REPO_PATH="./tmp",
        DJVERSION_GIT_USE_COMMIT=True,
    )
    def test_get_version__with_git_commit(self) -> None:
        """Util must return last commit from git repo from path."""
        path = Path(settings.DJVERSION_GIT_REPO_PATH)  # type: ignore
        test: Path = path.joinpath("TEST")
        repo: git.Repo = git.Repo.init(str(path.absolute()))
        with repo.config_writer() as config:
            config.set_value(section="user", option="name", value="TEST")
            config.set_value(section="user", option="email", value="test@example.com")
            config.write()
            config.release()
        author: git.Actor = git.Actor(name="TEST", email="test@example.com")
        committer: git.Actor = git.Actor(name="TEST", email="test@example.com")
        test.absolute().open("wb").close()
        repo.index.add([str(test.absolute())])
        commit = repo.index.commit(
            message="TEST", author=author, committer=committer
        )
        version: str = get_version()
        shutil.rmtree(path)

        self.assertEqual(first=version, second=commit.hexsha)
