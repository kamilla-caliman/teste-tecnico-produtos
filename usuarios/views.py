from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from .models import User
from .serializers import AccountSerializer


class CreateAccountView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    queryset = User.objects.all()


class LogoutView(ObtainAuthToken):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)
