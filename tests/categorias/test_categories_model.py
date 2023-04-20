from produtos.models import Produto
from categorias.models import Categoria
from django.test import TestCase
import ipdb


class CategoriesModelView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category_data = {"nome": "Categoria Teste"}
        cls.category = Categoria.objects.create(**cls.category_data)

    def test_name_max_length(self):
        max_length = self.category._meta.get_field("nome").max_length

        self.assertEqual(max_length, 225)

    def test_category_can_have_multiple_products(self):
        products_data = {"nome": "Teste", "descricao": "teste", "preco": 10.50}

        products = [Produto.objects.create(**products_data) for _ in range(5)]

        for product in products:
            self.category.produtos.add(product)

        self.assertEqual(len(products), self.category.produtos.count())
