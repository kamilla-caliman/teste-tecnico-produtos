from products.models import Product
from categories.models import Category
from django.test import TestCase


class ProductsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category_data = {"name": "Categoria Teste"}
        cls.category = Category.objects.create(**cls.category_data)
        cls.products_data = {
            "name": "Produto 1",
            "description": "Produto teste",
            "price": 15.20,
        }

        cls.product = Product.objects.create(**cls.products_data)
        cls.product.categories.add(cls.category)

    def test_name_max_length(self):
        max_length = self.product._meta.get_field("name").max_length

        self.assertEqual(max_length, 225)

    def test_price_max_digits(self):
        max_digits = self.product._meta.get_field("price").max_digits

        self.assertEqual(max_digits, 8)

    def test_price_decimal_places(self):
        decimal_places = self.product._meta.get_field("price").decimal_places

        self.assertEqual(decimal_places, 2)

    def test_products_can_have_multiple_categories(self):
        categories = [Category.objects.create(name="teste") for _ in range(5)]

        for category in categories:
            self.product.categories.add(category)

        self.assertEqual(len(categories) + 1, self.product.categories.count())
