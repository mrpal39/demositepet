from accounts.models import OwnerProfile
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerProfile
        fields = ('id', 'username', 'email',
                  'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = OwnerProfile.objects.create_user(validated_data['username'],
                                                email=validated_data['email'],
                                                password=validated_data['password'],
                                                first_name=validated_data['first_name'],
                                                last_name=validated_data['last_name']
                                                )
        return user
# User serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerProfile
        fields = '__all__'
