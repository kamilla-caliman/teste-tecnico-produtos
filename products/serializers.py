from rest_framework import serializers
from .models import Product
from categories.models import Category
from categories.serializers import CategorySerializer, CategoryInProductsSerializer


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Product:
        categories_data = validated_data.pop("categories")
        product = Product.objects.create(**validated_data)

        for category in categories_data:
            categoryExists = Category.objects.filter(
                name__iexact=category["name"]
            ).first()

            if not categoryExists:
                categoryExists = Category.objects.create(**category)

            product.categories.add(categoryExists)

        return product

    def update(self, instance: Product, validated_data: dict) -> Product:
        if "categories" in validated_data:
            categories_data = validated_data.pop("categories")

            for category in categories_data:
                categoryExists = Category.objects.filter(
                    name__iexact=category["name"]
                ).first()

                if not categoryExists:
                    categoryExists = Category.objects.create(**category)

                instance.categories.add(categoryExists)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    categories = CategoryInProductsSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "categories",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
