from produtos.models import Produto
from categorias.models import Categoria
from django.test import TestCase


class ProductsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category_data = {"nome": "Categoria Teste"}
        cls.category = Categoria.objects.create(**cls.category_data)
        cls.products_data = {
            "nome": "Produto 1",
            "descricao": "Produto teste",
            "preco": 15.20,
        }

        cls.product = Produto.objects.create(**cls.products_data)
        cls.product.categorias.add(cls.category)

    def test_name_max_length(self):
        max_length = self.product._meta.get_field("nome").max_length

        self.assertEqual(max_length, 225)

    def test_preco_max_digits(self):
        max_digits = self.product._meta.get_field("preco").max_digits

        self.assertEqual(max_digits, 8)

    def test_preco_decimal_places(self):
        decimal_places = self.product._meta.get_field("preco").decimal_places

        self.assertEqual(decimal_places, 2)

    def test_products_can_have_multiple_categories(self):
        categories = [Categoria.objects.create(nome="teste") for _ in range(5)]

        for category in categories:
            self.product.categorias.add(category)

        self.assertEqual(len(categories) + 1, self.product.categorias.count())
