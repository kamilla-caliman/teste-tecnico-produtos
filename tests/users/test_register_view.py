# from rest_framework.test import APITestCase
# from rest_framework.views import status
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser


# User: AbstractUser = get_user_model()


# class UserRegistrationViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls) -> None:
#         cls.BASE_URL = "/api/users/"

#         cls.maxDiff = None

#     def test_create_user_without_required_fields(self):
#         response = self.client.post(self.BASE_URL, data={}, format="json")

#         # STATUS CODE
#         with self.subTest():
#             expected_status_code = status.HTTP_400_BAD_REQUEST
#             resulted_status_code = response.status_code
#             msg = (
#                 "Verifique se o status code retornado do POST sem todos os campos obrigatórios"
#                 + f" em {self.BASE_URL} é {expected_status_code}"
#             )
#             self.assertEqual(expected_status_code, resulted_status_code, msg)

#         # RETORNO JSON
#         resulted_data: dict = response.json()
#         expected_fields = {"nome", "username", "email", "password", "empresa"}
#         returned_fields = set(resulted_data.keys())
#         msg = "Verifique se todas as chaves obrigatórias são retornadas ao tentar criar um usuário sem dados"
#         self.assertSetEqual(expected_fields, returned_fields, msg)
