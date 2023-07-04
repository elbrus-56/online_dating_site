from django.urls import path

from match_users.views import MatchUsers

urlpatterns = [
    path('<int:pk>/match', MatchUsers.as_view(), name='match_users'),
]
