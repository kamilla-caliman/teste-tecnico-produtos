from rest_framework import serializers
from .models import Categoria


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            "id",
            "nome",
        ]
