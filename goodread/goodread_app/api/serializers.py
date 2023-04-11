from rest_framework import serializers
from goodread_app.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    rating = serializers.DecimalField(max_digits=5, decimal_places=2)
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    