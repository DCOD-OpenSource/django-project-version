from datetime import date, datetime
from typing import List, Union, Optional

from appconf import AppConf
from django.conf import settings


__all__: List[str] = ["settings"]


class DjangoDjversionAppConf(AppConf):
    """Django djversion settings."""

    VERSION: Optional[str] = getattr(settings, "DJVERSION_VERSION", None)
    UPDATED: Optional[Union[datetime, date]] = getattr(
        settings, "DJVERSION_UPDATED", None
    )
    FORMAT_STRING: str = getattr(
        settings, "DJVERSION_FORMAT_STRING", "{version} ({updated})"  # noqa: FS003
    )
    GIT_REPO_PATH: Optional[str] = getattr(settings, "DJVERSION_GIT_REPO_PATH", None)
    GIT_USE_TAG: bool = getattr(settings, "DJVERSION_GIT_USE_TAG", False)
    GIT_USE_COMMIT: bool = getattr(settings, "DJVERSION_GIT_USE_COMMIT", False)

    class Meta:
        """Config settings."""

        prefix: str = "djversion"
