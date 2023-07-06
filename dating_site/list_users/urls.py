from django.urls import path

from list_users.views import ListUsers


urlpatterns = [
    path('list/', ListUsers.as_view(), name='list_users'),
]
