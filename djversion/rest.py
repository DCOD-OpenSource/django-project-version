# -*- coding: utf-8 -*-

# django-project-version
# djversion/rest.py


from typing import Any, Dict, List, Type  # pylint: disable=W0611

from django.utils.translation import ugettext_lazy as _
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, BasePermission  # pylint: disable=W0611
from rest_framework.response import Response
from rest_framework.serializers import CharField, Serializer

from djversion.utils import get_version


__all__ = ["VersionSerializer", "VersionView"]  # type: List[str]


class VersionSerializer(Serializer):
    """
    Version serializer.
    """

    version = CharField(
        label=_("version"), help_text=_("project version"), read_only=True
    )  # type: CharField


class VersionView(GenericAPIView):
    """
    Version view.
    """

    permission_classes = [AllowAny]  # type: List[Type[BasePermission]]
    serializer_class = VersionSerializer  # type: Type[VersionSerializer]

    def get(self, request, **kwargs: Dict[str, Any]) -> Response:
        """
        Handle GET http request.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: Dict[str, Any].
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        data = {"version": get_version()}  # type: Dict[str, str]
        serializer = self.get_serializer(instance=data)

        return Response(serializer.data)
