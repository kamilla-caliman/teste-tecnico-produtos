from rest_framework import serializers
from .models import Produto
from categorias.models import Categoria
from categorias.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Produto:
        categories_data = validated_data.pop("categorias")
        product = Produto.objects.create(**validated_data)

        for category in categories_data:
            categoryExists = Categoria.objects.filter(
                nome__iexact=category["nome"]
            ).first()

            if not categoryExists:
                categoryExists = Categoria.objects.create(**category)

            product.categorias.add(categoryExists)

        return product

    def update(self, instance: Produto, validated_data: dict) -> Produto:
        if "categorias" in validated_data:
            categories_data = validated_data.pop("categorias")

            for category in categories_data:
                categoryExists = Categoria.objects.filter(
                    nome__iexact=category["nome"]
                ).first()

                if not categoryExists:
                    categoryExists = Categoria.objects.create(**category)

                instance.categorias.add(categoryExists)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    categorias = CategorySerializer(many=True)

    class Meta:
        model = Produto
        fields = [
            "id",
            "nome",
            "descricao",
            "preco",
            "categorias",
            "data_cadastro",
            "data_atualizacao",
        ]
        extra_kwargs = {
            "data_cadastro": {"read_only": True},
            "data_atualizacao": {"read_only": True},
        }
