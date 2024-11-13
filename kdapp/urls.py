from django.urls import path
from . import views
from .views import  KullaniciDetay,todoekle,kullaniciekle






urlpatterns = [
    path("",views.kullanici,name='kullanici'),
    path("kullanici",views.kullanici,name='kullanici'),
    path("kullaniciliste",views.kullaniciliste,name='kullaniciliste'),
    path('user/<int:user_id>/details/', views.KullaniciDetay, name='kullanicidetay'),
    path('kullanicitodoekle/', views.todoekle, name='kullanicitodoekle'),
    path('kullanici-ekle/', views.kullaniciekle, name='kullanici_ekle'),
    path('kullanicisil/', views.kullanicisil, name='kullanicisil'),

]
