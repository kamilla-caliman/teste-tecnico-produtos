from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "products"]
        depth = 1
        extra_kwargs = {"products": {"read_only": True}}


class CategoryInProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
