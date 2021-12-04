from rest_framework import serializers
from .models import *

class UserAPI(serializers.ModelSerializer):
    class Meta :
        model= OwnerProfile
        exclude = [
            "password",
            "groups",
            "is_staff",
        ]
class LoginAPI(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
