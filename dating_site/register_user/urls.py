from django.urls import path
from django.contrib.auth.views import LogoutView
from register_user.views import RegisterUser, LoginUser

urlpatterns = [
    path('create/', RegisterUser.as_view(), name='register_user'),
]

