from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.CreateAccountView.as_view()),
    path("users/login/", views.LoginView.as_view()),
    path("users/logout/", views.LogoutView.as_view()),
]
