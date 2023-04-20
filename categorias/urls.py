from django.urls import path
from . import views

urlpatterns = [
    path("categorias/", views.CategoryView.as_view()),
    # path("categorias/<pk>/"),  # Retrieve, Update and Delete Categoria API
    # path("categorias/<pk>/produtos/"),  # Listar produtos de uma categoria
]
