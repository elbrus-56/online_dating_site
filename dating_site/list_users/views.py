from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from list_users.filter import MyFilter
from list_users.serializers import ListUsersSerializer

User = get_user_model()


class ListUsers(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.exclude(username='admin')
    serializer_class = ListUsersSerializer
    filterset_class = MyFilter

    def get(self, request, *args, **kwargs):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        print(content)
        return self.list(request, *args, **kwargs)
