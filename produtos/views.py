from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .models import Produto
from categorias.models import Categoria
from django.shortcuts import get_object_or_404


class ProductView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_params = self.request.query_params.get("categoria")

        if category_params:
            queryset = Produto.objects.filter(
                categorias__nome__icontains=category_params
            )
            return queryset

        return super().get_queryset()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer


class RemoveCategoryView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"
    lookup_field = "id"

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        category_id = self.kwargs["category_id"]

        category = get_object_or_404(Categoria, id=category_id)
        product = get_object_or_404(Produto, id=product_id)

        product.categorias.remove(category)

        return super().get_queryset()
