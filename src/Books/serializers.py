from rest_framework import serializers

from . import models


class BookSerializers(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=255, default=None)
    total_pages = serializers.IntegerField(default=None, max_value=5000)
    rating = serializers.DecimalField(default=None, decimal_places=2, max_digits=5)
    isbn = serializers.CharField(default=None, max_length=13)
    published_date = serializers.DateField(default=None,style={'base_template': 'input.html', 'input_type':'date'})
    publisher_id = serializers.ChoiceField(choices=models.Publishers.objects.all().values_list('name', flat=True), default=None)
    author_id = serializers.ChoiceField(choices=models.Authors.objects.all().values_list('first_name', flat=True), default=None)
    genre_id = serializers.ChoiceField(choices=models.Genres.objects.all().values_list('genre', flat=True), default=None)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        
        return models.Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.total_pages = validated_data.get('total_pages', instance.total_pages)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        publisher_id = validated_data.get('publisher_id', instance.publisher_id)
        author_id = validated_data.get('author_id', instance.author_id)
        genre_id = validated_data.get('genre_id', instance.genre_id)
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