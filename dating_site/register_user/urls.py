from django.urls import path
from django.contrib.auth.views import LogoutView
from register_user.views import RegisterUser, LoginUser

urlpatterns = [
    path('create/', RegisterUser.as_view(), name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path("logout/", LogoutView.as_view(), name="logout"),
]

