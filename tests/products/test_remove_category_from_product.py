from rest_framework.test import APITestCase
from rest_framework.views import status
from tests.factories.products_factories import create_product
from tests.factories.categories_factories import create_category
from tests.factories.user_factories import create_user_with_token
from products.models import Product


class RemoveCategoryFromProductTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user, token = create_user_with_token()
        cls.access_token = token
        cls.product_test = create_product()
        cls.product_id = cls.product_test.id
        cls.category_test = create_category()
        cls.category_id = cls.category_test.id

        cls.product_test.categories.add(cls.category_test)

        cls.BASE_URL = f"/api/products/{cls.product_id}/category/{cls.category_id}/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_remove_category_from_products_without_token(self):
        response = self.client.patch(self.BASE_URL, format="json")

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_401_UNAUTHORIZED
            resulted_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do PATCH"
                + f" é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON
        expected_data = {"detail": "Authentication credentials were not provided."}
        resulted_data = response.json()
        msg = (
            "Verifique se os dados retornados do PATCH sem token"
            + f" em {self.BASE_URL} é {expected_data}"
        )
        self.assertDictEqual(expected_data, resulted_data, msg)

    def test_remove_category_from_product_with_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.access_token))
        response = self.client.patch(self.BASE_URL, format="json")
        categories = response.json()["categories"]

        # STATUS CODE
        with self.subTest():
            expected_status_code = status.HTTP_200_OK
            resulted_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do PATCH"
                + f" é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON

        expected_data = next(
            (item for item in categories if item["id"] == self.category_id), None
        )
        msg = (
            "Verifique se os dados retornados do PATCH"
            + f" em {self.BASE_URL} é {expected_data}"
        )

        self.assertEqual(expected_data, None, msg)
