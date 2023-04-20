from rest_framework import generics
from .serializers import ProductSerializer
from .models import Produto


class ProductView(generics.ListCreateAPIView):
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
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer
