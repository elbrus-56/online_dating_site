from django.urls import path

from register_user.views import RegisterUser

urlpatterns = [
    path('create/', RegisterUser.as_view(), name='register_user'),
]

