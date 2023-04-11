from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    rating = serializers.DecimalField(max_digits=5, decimal_places=2)
    active = serializers.BooleanField()
    