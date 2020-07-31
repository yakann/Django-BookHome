from django.db import models

# Create your models here.

class Publishers(models.Model):
    
    class Meta:
        db_table = 'Publishers'
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, blank=False, null=False)

class Authors(models.Model):
    
    class Meta:
        db_table = 'Authors'
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)

class Genres(models.Model):
    
    class Meta:
        db_table = 'Genres'
    id = models.AutoField(primary_key=True, unique=True)
    genre = models.CharField(max_length=255, blank=False, null=False)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

class Books(models.Model):

    class Meta:
        db_table = 'Books'
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    total_pages = models.IntegerField(blank=False, null=True)
    rating = models.DecimalField(blank=False, null=True, decimal_places=2, max_digits=5)
    isbn = models.CharField(max_length=13, blank=False, null=True)
    published_date = models.DateField(blank=False, null=True)
    publisher_id = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)

# class Book_Authors(models.Model):
    
#     class Meta:
#         db_table = 'Book_Authors'
#     book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
#     author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)

# class Book_Genres(models.Model):
    
#     class Meta:
#         db_table = 'Book_Genres'
    
#     book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
#     genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)

#MİGRATE SORUNU İÇİN: https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html