from typing import Any, Dict, List, Type

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import CharField, Serializer
from rest_framework.permissions import AllowAny, BasePermission

from djversion.utils import get_version


__all__: List[str] = ["VersionSerializer", "VersionView"]


class VersionSerializer(Serializer):  # type: ignore
    """Version serializer."""

    version = CharField(
        label=_("version"), help_text=_("project version"), read_only=True
    )


class VersionView(GenericAPIView):  # type: ignore
    """Version view."""

    permission_classes: List[Type[BasePermission]] = [AllowAny]
    serializer_class: Type[VersionSerializer] = VersionSerializer
    pagination_class = None
    filter_backends = None  # type: ignore

    def get(self, request, **kwargs: Dict[str, Any]) -> Response:
        """
        Handle GET http request.

        :param request: django request instance
        :type request: HttpRequest
        :param kwargs: additional args
        :type kwargs: Dict[str, Any]
        :return: serialized custom queryset response
        :rtype: Response
        """
        data: Dict[str, str] = {"version": get_version()}
        serializer = self.get_serializer(instance=data)

        return Response(serializer.data)
