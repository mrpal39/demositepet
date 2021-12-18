from django.db import models
from rest_framework import serializers
from .models import Contact, Kennel

class KennelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kennel
        fields='__all__'

