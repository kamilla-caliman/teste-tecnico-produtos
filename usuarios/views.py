from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics
from .models import User
from .serializers import AccountSerializer


class CreateAccountView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    queryset = User.objects.all()


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)
