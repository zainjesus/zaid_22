from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserValidateSerializer, UserCreateSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(data={'message': 'User be created!'},
                        status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(data={'error': 'Incorrect login or password!'},
                        status=status.HTTP_401_UNAUTHORIZED)


