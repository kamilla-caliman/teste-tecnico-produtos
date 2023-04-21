from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

User: AbstractUser = get_user_model()


def create_user_with_token(user_data=None):
    if not user_data:
        user_data = {
            "name": "User Test",
            "username": "user_test",
            "email": "user_test@mail.com",
            "password": "1234",
        }

    user = User.objects.create_user(**user_data)
    user_token = Token.objects.create(user=user)

    return user, user_token
