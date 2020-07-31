from django import forms
from .models import Authors, Books, Genres, Publishers

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','total_pages','rating','isbn','published_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '','class':'form-control'}),
            'total_pages': forms.NumberInput(attrs={'placeholder': '','class':'form-control'}),
            'rating': forms.NumberInput(attrs={'placeholder': '','class':'form-control'}),
            'isbn': forms.TextInput(attrs={'placeholder': '','class':'form-control'}),
            'published_date': forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'myDateClass', 'placeholder':'Select a date'}),
        }