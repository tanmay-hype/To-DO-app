from rest_framework import serializers
from .models import User    
from django.contrib.auth import authenticate
#serializer is imported for converting complex 
# data types, such as querysets and model instances, 
# into native Python datatypes that can then be easily
#  rendered into JSON, XML or other content types.
#user is imported for creating new user 
# and authenticate is imported for validating
#  user credentials during login

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
# the create method is overridden to create a new user
#  using the create_user method provided by Django's 
# User model manager.

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
# the validate method is overridden to authenticate 
# the user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
#  If the authentication fails, a validation error 
# is raised.
# The LoginSerializer is a simple serializer that takes
#  in a username and password, and validates them against

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')