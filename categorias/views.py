from rest_framework import generics
from .serializers import CategorySerializer
from .models import Categoria


class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Categoria.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Categoria.objects.all()


# class ProductsByCategoryView(generics.ListAPIView):
#     ...
