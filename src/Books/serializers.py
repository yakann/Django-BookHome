from rest_framework import serializers

from . import models

class BookSerializers(serializers.Serializer):

    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

    # title = serializers.CharField(
    #     max_length=100,
    #     style={'placeholder': 'text', 'autofocus': True}
    # )
    # total_pages = serializers.CharField(
    #     max_length=100,
    #     style={'input_type': 'number', 'placeholder': 'Password'}
    # )
    # rating = serializers.CharField(
    #     max_length=5,
    #     style={'input_type': 'number'}
    # )
    # isbn = serializers.CharField(
    #     max_length=13,
    #     style={'input_type': 'text'}
    # )
    # published_date = serializers.CharField(
    #     style={'input_type': 'date'}
    # )

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