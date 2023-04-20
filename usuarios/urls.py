from django.urls import path
from . import views
from rest_framework.authtoken import views as v


urlpatterns = [
    path("users/", views.CreateAccountView.as_view()),
    path("users/login/", v.obtain_auth_token),
    path("users/logout/", views.LogoutView.as_view()),
]
