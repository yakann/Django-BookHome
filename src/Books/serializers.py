from rest_framework import serializers

from . import models

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'

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