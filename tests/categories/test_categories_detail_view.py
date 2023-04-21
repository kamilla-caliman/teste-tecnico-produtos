from rest_framework.test import APITestCase
from rest_framework.views import status
from tests.factories.categories_factories import create_category
from tests.factories.user_factories import create_user_with_token


class CategoryDetailViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user, token = create_user_with_token()
        cls.access_token = token
        cls.category_test = create_category()
        cls.category_id = cls.category_test.id

        cls.BASE_URL = f"/api/categories/{cls.category_id}/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_retrieve_category_without_token(self):
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

    def test_retrieve_category_with_token(self):
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
        expected_data = {
            "id": self.category_id,
            "name": self.category_test.name,
            "products": [],
        }
        resulted_data = response.json()
        msg = (
            "Verifique se as informações retornadas no POST "
            + f"em `{self.BASE_URL}` estão corretas."
        )
        self.assertDictEqual(expected_data, resulted_data, msg)

    def test_update_category_without_token(self):
        patch_data = {"name": "Category PATCHED"}
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

    def test_update_category_with_token(self):
        patch_data = {"name": "Category PATCHED"}
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
        expected_data = {
            "id": self.category_id,
            "name": patch_data["name"],
            "products": [],
        }
        resulted_data = response.json()

        msg = (
            "Verifique se os dados retornados ao fazer um PATCH com token válido "
            + f"em {self.BASE_URL} é {expected_data}"
        )
        self.assertDictEqual(expected_data, resulted_data, msg)

    def test_delete_category_without_token(self):
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

    def test_delete_category_with_token(self):
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
