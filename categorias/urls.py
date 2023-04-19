from django.urls import path

urlpatterns = [
    path("categoria/"),  # ListCreate API
    path("categoria/<pk>/"),  # Retrieve, Update and Delete Categoria API
    path("categoria/<pk>/produtos/"),  # Listar produtos de uma categoria
]
