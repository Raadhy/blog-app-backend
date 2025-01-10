from rest_framework import serializers
from typeguard import typechecked
from . import models

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_joined']
    
class UserChangePassword(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        model = models.User
        fields = ['password']

    @typechecked
    def validate(self, attrs):
        password : str = attrs.get('password')
        user = self.context.get('user')
        if len(password) < 6:
            raise serializers.ValidationError("Password must be greated than or equals to 6 digits")
        user.set_password(password)
        user.save()
        return attrs