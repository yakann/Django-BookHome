from django.urls import path, include
from .views import KitapDetay, KitapListesi, GenericBooksList

app_name='Books'

urlpatterns = [
    path('', KitapListesi.as_view(), name='kitaplar'),
    path('kitapdetay/<int:id>/', KitapDetay.as_view(), name='kitap-detay'),
    path('generickitap/<int:id>/', GenericBooksList.as_view(), name='kitap-generic'),
] 