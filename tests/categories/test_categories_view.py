from rest_framework.test import APITestCase
from rest_framework.views import status
from tests.factories.user_factories import create_user_with_token
from tests.factories.categories_factories import create_multiple_categories
from categories.models import Category


class CategoryViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/categories/"
        cls.user, token = create_user_with_token()
        cls.access_token = str(token.key)

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_categories_listing_pagination_without_token(self):
        categories_count = 10
        create_multiple_categories(categories_count)

        response = self.client.get(self.BASE_URL)

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_401_UNAUTHORIZED
            result_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, result_status_code, msg)

        # RETORNO JSON
        expected_data = {"detail": "Authentication credentials were not provided."}
        resulted_data = response.json()
        msg = (
            "Verifique se a mensagem de retorno do POST sem token"
            + f"em `{self.BASE_URL}` está correta."
        )
        self.assertDictEqual(expected_data, resulted_data, msg)

    def test_categories_listing_pagination(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.access_token))

        categories_count = 10
        create_multiple_categories(categories_count)

        response = self.client.get(self.BASE_URL)
        resulted_data = response.json()

        resulted_pagination_keys = set(resulted_data.keys())
        expected_pagination_keys = {"count", "next", "previous", "results"}
        msg = "Verifique se a paginação está sendo feita corretamente"
        with self.subTest():
            self.assertSetEqual(expected_pagination_keys, resulted_pagination_keys)

        results_len = len(resulted_data["results"])
        expected_len = 5
        msg = "Verifique se a paginação está retornando cinco items de cada vez"
        self.assertEqual(expected_len, results_len, msg)

    def test_product_creation_without_required_fields(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.access_token))
        response = self.client.post(self.BASE_URL, data={}, format="json")

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_400_BAD_REQUEST
            resulted_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST sem todos os campos obrigatórios "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON
        resulted_data: dict = response.json()
        expected_fields = {"name"}
        returned_fields = set(resulted_data.keys())
        msg = "Verifique se todas as chaves obrigatórias são retornadas ao tentar criar uma categoria sem dados"
        self.assertSetEqual(expected_fields, returned_fields, msg)

    def test_category_creation_without_token(self):
        # STATUS CODE
        with self.subTest():
            response = self.client.post(self.BASE_URL, data={}, format="json")
            expected_status_code = status.HTTP_401_UNAUTHORIZED
            result_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, result_status_code, msg)

        # RETORNO JSON
        expected_data = {"detail": "Authentication credentials were not provided."}
        resulted_data = response.json()
        msg = (
            "Verifique se a mensagem de retorno do POST sem token"
            + f"em `{self.BASE_URL}` está correta."
        )
        self.assertDictEqual(expected_data, resulted_data, msg)

    def test_category_creation_with_valid_token(self):
        category_data = {"name": "Category Test"}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.access_token))
        response = self.client.post(self.BASE_URL, data=category_data, format="json")
        resulted_data = response.json()

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_201_CREATED
            result_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, result_status_code, msg)

        # RETORNO JSON
        added_category = Category.objects.last()
        expected_data = {
            "id": added_category.pk,
            "name": category_data["name"],
            "products": [],
        }

        resulted_data = response.json()
        msg = (
            "Verifique se os dados retornados do POST com o token"
            + f" em {self.BASE_URL} é {expected_data}"
        )
        self.assertDictEqual(expected_data, resulted_data, msg)
