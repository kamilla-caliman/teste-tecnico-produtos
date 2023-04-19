from rest_framework import generics
from .serializers import ProductSerializer
from .models import Produto


class ProductView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer
