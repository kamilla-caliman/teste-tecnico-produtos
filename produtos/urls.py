from django.urls import path
from . import views

urlpatterns = [
    path("produtos/", views.ProductView.as_view()),  # ListCreate API
    path(
        "produtos/<pk>/", views.ProductDetailView.as_view()
    ),  # Retrieve, Update and Delete API
    path(
        "produtos/<product_id>/categoria/<category_id>/",
        views.RemoveCategoryView.as_view(),
    ),
]
