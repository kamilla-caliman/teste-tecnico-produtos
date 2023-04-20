from django.urls import path
from . import views

urlpatterns = [
    path("categorias/", views.CategoryView.as_view()),
    path("categorias/<pk>/", views.CategoryDetailView.as_view()),
]
