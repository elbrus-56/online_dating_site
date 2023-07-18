from django.contrib.auth import get_user_model
from list_users.filter import MyFilter
from list_users.serializers import ListUsersSerializer
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class ListUsers(ListAPIView):
    """
    Эндпоинт для вывода списка участников с возможностью фильтрации
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.exclude(username='admin')
    serializer_class = ListUsersSerializer
    filterset_class = MyFilter
