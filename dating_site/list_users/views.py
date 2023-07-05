from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from list_users.serializers import ListUsersSerializer

User = get_user_model()


class ListUsers(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.exclude(username='admin')
    serializer_class = ListUsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sex', 'first_name', 'last_name']
