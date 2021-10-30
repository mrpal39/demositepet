from django.db import models
from django.db.models import fields
from rest_framework import serializers

from pet.models import Pet

class PetSer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    state = serializers.ReadOnlyField(source='State.name')
    category = serializers.ReadOnlyField(source='category.name')
    breeds = serializers.ReadOnlyField(source='breeds.name')
    
    class Meta:
        model=Pet
        fields="__all__"
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Pet.objects.create(**validated_data)
