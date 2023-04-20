from products.models import Product
from categories.models import Category
from django.test import TestCase


class CategoriesModelView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category_data = {"name": "Categoria Teste"}
        cls.category = Category.objects.create(**cls.category_data)

    def test_name_max_length(self):
        max_length = self.category._meta.get_field("name").max_length

        self.assertEqual(max_length, 225)

    def test_category_can_have_multiple_products(self):
        products_data = {"name": "Teste", "description": "teste", "price": 10.50}

        products = [Product.objects.create(**products_data) for _ in range(5)]

        for product in products:
            self.category.products.add(product)

        self.assertEqual(len(products), self.category.products.count())
