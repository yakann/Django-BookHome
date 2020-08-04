from rest_framework import serializers

from . import models

class BookSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=255)
    total_pages = serializers.IntegerField(required=True, max_value=5000)
    rating = serializers.DecimalField(required=False, decimal_places=2, max_digits=5)
    isbn = serializers.CharField(required=True, max_length=13)
    published_date = serializers.DateField(style={'base_template': 'input.html', 'input_type':'date'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.total_pages = validated_data.get('total_pages', instance.total_pages)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
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