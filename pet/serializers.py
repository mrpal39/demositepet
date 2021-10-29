from rest_framework import serializers

from pet.models import Pet

class PetSerializers(serializers.Serializer):
    id = serializers.AutoField()
    owner = serializers.ForeignKey()
    name = serializers.CharField()
    description = serializers.CharField()
    category = serializers.ForeignKey()
    breeds = serializers.ForeignKey()
    size = serializers.CharField()
    state = serializers.ForeignKey()
    city = serializers.CharField()
    sex = serializers.CharField()
    profile_picture = serializers.ImageField()
    slug = serializers()
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Pet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('style', instance.style)
        instance.breeds = validated_data.get('style', instance.style)
        instance.size = validated_data.get('size', instance.size)
        instance.style = validated_data.get('style', instance.style)
        instance.style = validated_data.get('style', instance.style)
        instance.style = validated_data.get('style', instance.style)
        instance.style = validated_data.get('style', instance.style)
        instance.style = validated_data.get('style', instance.style)

        instance.save()
        return instance