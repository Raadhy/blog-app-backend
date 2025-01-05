from rest_framework import serializers
from . import models

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']