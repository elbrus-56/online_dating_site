from django.contrib.auth.views import LogoutView
from django.urls import path
from register_user.views import LoginUser, RegisterUser

urlpatterns = [
    path('create/', RegisterUser.as_view(), name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
