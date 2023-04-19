from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "nome", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [UniqueValidator(queryset=User.objects.all())],
                "required": True,
            },
        }

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
            nome=validated_data["nome"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
