from rest_framework import serializers
from .models import Categoria


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome", "produtos"]
        depth = 1
        extra_kwargs = {"produtos": {"read_only": True}}


class CategoryInProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome"]
