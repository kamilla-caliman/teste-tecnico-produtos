from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path("users/", views.CreateAccountView.as_view()),
    # path("users/<int:pk>/", views.UserDetailView.as_view()),
    # path("users/address/<int:pk>/", views.AdressDetailView.as_view()),
    # path("users/login/", obtain_auth_token),
    path("users/login/", views.LoginView.as_view()),
    path("users/logout/", views.LogoutView.as_view()),
]
