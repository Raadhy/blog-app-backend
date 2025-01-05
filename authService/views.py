from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class UserRegistration(APIView):
    def post(self, request, format=None):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # token = get_tokens_for_user(user=user)
            return Response({"msg": "Registration Successful..."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)