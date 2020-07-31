from django.contrib import admin

from .models import Authors, Books, Genres, Publishers
#Register your models here.
admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Genres)
admin.site.register(Publishers)