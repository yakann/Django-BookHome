from django.urls import path, include
from .views import KitapDetay, KitapListesi

urlpatterns = [
    path('', KitapListesi.as_view()),
    path('kitapdetay/<int:id>/', KitapDetay.as_view()),
] 