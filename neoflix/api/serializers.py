from rest_framework import serializers
from .models import MovieStore


class MovieSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MovieStore
        fields = ('id', 'name', 'date_created',
                  'category', 'rating', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
