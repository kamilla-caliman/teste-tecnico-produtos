from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .models import Product
from categories.models import Category
from django.shortcuts import get_object_or_404


class ProductView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_params = self.request.query_params.get("category")

        if category_params:
            queryset = Product.objects.filter(
                categories__name__icontains=category_params
            )
            return queryset

        return super().get_queryset()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RemoveCategoryView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"
    lookup_field = "id"

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        category_id = self.kwargs["category_id"]

        category = get_object_or_404(Category, id=category_id)
        product = get_object_or_404(Product, id=product_id)

        product.categories.remove(category)

        return super().get_queryset()
