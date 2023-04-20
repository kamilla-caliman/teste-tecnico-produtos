from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer
from .models import Categoria


class CategoryView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Categoria.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Categoria.objects.all()
