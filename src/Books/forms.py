from django import forms
from .models import Authors, Books, Genres, Publishers

class BooksForm(forms.ModelForm):
    Tip = forms.ModelChoiceField(queryset=Books.objects.all(),
    empty_label=None,
    widget=forms.Select(attrs={
          'class': 'custom-select'
          }))
          
    class Meta:
        model = Books
        fields = ['Kod','Aciklama1','Aciklama2','GrupKod','SayKod','Tip']
        widgets = {
            # 'tarih1': DatePickerInput(format='%d/%m/%Y'),
            # 'tarih2': DatePickerInput(format='%d/%m/%Y'),
            'Kod': forms.TextInput(attrs={'placeholder': '','class':'form-control'}),
            'Aciklama1': forms.TextInput(attrs={'placeholder': '','class':'form-control'}),
            'Aciklama2': forms.TextInput(attrs={'placeholder': '','class':'form-control'}),
            'GrupKod': forms.TextInput(attrs={'placeholder': '','class':'form-control'}),
            'SayKod': forms.NumberInput(attrs={'placeholder': '','class':'form-control'}),
        }