from django.urls import path

from list_users.views import ListUsers
from match_users.views import MatchUsers

urlpatterns = [
    path('list/', ListUsers.as_view(), name='list_users'),
]
