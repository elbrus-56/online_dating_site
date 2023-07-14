from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from list_users.filter import MyFilter
from list_users.serializers import ListUsersSerializer

User = get_user_model()


class ListUsers(ListAPIView):
    """
    Эндпоинт выводит список участников с возможностью фильтрования
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.exclude(username='admin')
    serializer_class = ListUsersSerializer
    filterset_class = MyFilter

    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)
