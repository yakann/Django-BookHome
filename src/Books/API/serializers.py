from rest_framework import serializers

from . import models

class BookSerializers(serializers.Serializer):

    title = serializers.CharField(
        max_length=100,
        style={'placeholder': 'text', 'autofocus': True}
    )
    total_pages = serializers.CharField(
        max_length=100,
        style={'input_type': 'number', 'placeholder': 'Password'}
    )
    rating = serializers.CharField(
        max_length=5,
        style={'input_type': 'number'}
    )
    isbn = serializers.CharField(
        max_length=13,
        style={'input_type': 'text'}
    )
    published_date = serializers.CharField(
        style={'input_type': 'date'}
    )

class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Publishers
        fields = '__all__'

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Authors
        fields = '__all__'

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Genres
        fields = '__all__'