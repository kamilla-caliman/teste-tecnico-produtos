from rest_framework.test import APITestCase
from rest_framework.views import status
from tests.factories.products_factories import create_product
from tests.factories.user_factories import create_user_with_token
from products.models import Product


class ProductDetailViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user, token = create_user_with_token()
        cls.access_token = token
        cls.product_test = create_product()
        cls.product_id = cls.product_test.id

        cls.BASE_URL = f"/api/products/{cls.product_id}/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_retrieve_product_without_token(self):
        response = self.client.get(self.BASE_URL, format="json")

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_401_UNAUTHORIZED
            resulted_status_code = response.status_code
            msg = "Verifique se o status code retornado do GET"
            self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON
        expected_data = {"detail": "Authentication credentials were not provided."}
        resulted_data = response.json()
        msg = (
            "Verifique se os dados retornados do GET sem token"
            + f" em {self.BASE_URL} é {expected_data}"
        )
        self.assertDictEqual(expected_data, resulted_data, msg)

    def test_retrieve_product_with_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.access_token))
        response = self.client.get(self.BASE_URL, format="json")

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_200_OK
            resulted_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado ao fazer o GET com o token válido "
                + f"em {self.BASE_URL} é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON
        expected_keys = {
            "id",
            "name",
            "description",
            "price",
            "categories",
            "created_at",
            "updated_at",
        }
        resulted_data = response.json()
        resulted_keys = set(resulted_data.keys())
        msg = (
            "Verifique se as informações retornadas no POST "
            + f"em `{self.BASE_URL}` estão corretas."
        )
        self.assertSetEqual(expected_keys, resulted_keys, msg)

    def test_update_product_without_token(self):
        patch_data = {"name": "Product PATCHED"}
        response = self.client.get(self.BASE_URL, data=patch_data, format="json")

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_401_UNAUTHORIZED
            resulted_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado ao fazer o PATCH sem token "
                + f"em {self.BASE_URL} é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON
        expected_data = {"detail": "Authentication credentials were not provided."}
        resulted_data = response.json()
        msg = (
            "Verifique se os dados retornados ao fazer um PATCH sem token "
            + f"em {self.BASE_URL} é {expected_data}"
        )
        self.assertDictEqual(expected_data, resulted_data, msg)

    def test_update_product_with_token(self):
        patch_data = {"name": "Product PATCHED"}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.access_token))
        response = self.client.patch(self.BASE_URL, data=patch_data, format="json")

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_200_OK
            resulted_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado ao fazer o PATCH com token válido "
                + f"em {self.BASE_URL} é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON
        expected_data = patch_data["name"]
        resulted_data = response.json()["name"]

        msg = (
            "Verifique se os dados retornados ao fazer um PATCH com token válido "
            + f"em {self.BASE_URL} é {expected_data}"
        )
        self.assertEqual(expected_data, resulted_data, msg)

    def test_delete_product_without_token(self):
        response = self.client.delete(self.BASE_URL, format="json")

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_401_UNAUTHORIZED
            resulted_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado ao fazer um DELETE sem token "
                + f"em {self.BASE_URL} é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON
        expected_data = {"detail": "Authentication credentials were not provided."}
        resulted_data = response.json()
        msg = (
            "Verifique se os dados retornados ao fazer um DELETE sem token "
            + f"em {self.BASE_URL} é {expected_data}"
        )
        self.assertDictEqual(expected_data, resulted_data, msg)

    def test_delete_product_with_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.access_token))
        response = self.client.delete(self.BASE_URL, format="json")

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_204_NO_CONTENT
            resulted_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado ao fazer um DELETE com token de admin"
                + f" em {self.BASE_URL} é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, resulted_status_code, msg)
