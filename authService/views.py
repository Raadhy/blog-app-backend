from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from typeguard import typechecked
from . import serializers


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistration(APIView):
    def post(self, request):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "Registration Successful..."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@typechecked
class UserLogin(APIView):
    def post(self, request):
        try:
            email : str = request.data['email']
            password : str = request.data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user=user)
                return Response({"msg": "Login Successful...", "user": {
                    "email": email,
                    "id": user.id
                }, "token": token}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = request.user
            serializer = serializers.UserProfileSerializer(user)
            return Response({"msg": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        try:
            serializer =serializers.UserChangePassword(data=request.data, context={'user': request.user})
            if serializer.is_valid(raise_exception=True):
                return Response({'msg': 'Password Change Successfully...'}, status=status.HTTP_200_OK)
            return Response({"error": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)