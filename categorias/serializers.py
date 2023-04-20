from rest_framework import serializers
from rest_framework.views import status
from .models import Categoria
from produtos.models import Produto


class CategorySerializer(serializers.ModelSerializer):
    def update(self, instance: Categoria, validated_data: dict) -> Categoria:
        if "produtos" in validated_data:
            product_data = validated_data.pop("produtos")
            for product in product_data:
                productExists = Produto.objects.filter(
                    nome__iexact=product["nome"]
                ).first()
                if not productExists:
                    raise serializers.ValidationError(
                        {"mensagem": "Produto não encontrado."},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                instance.categorias.add(productExists)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Categoria
        fields = ["id", "nome", "produtos"]
        depth = 1
        # extra_kwargs = {"produtos": {"read_only": True}}


class CategoryInProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["nome"]
