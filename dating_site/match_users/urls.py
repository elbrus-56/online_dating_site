from django.urls import path

from match_users.views import MatchUsers

urlpatterns = [
    path('<str:pk>/match', MatchUsers.as_view(), name='match_users'),
]
