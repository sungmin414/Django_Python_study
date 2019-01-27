from django.urls import path
from .views import *

app_name = 'photo'
urlpatterns = [
    path('', AlbumLV.as_view(), name='index'),
    path('album/', AlbumLV.as_view(), name='album_list'),
    path('album/<pk>/', AlbumDV.as_view(), name='album_detail'),
    path('photo/<pk>/', PhotoDV.as_view(), name='photo_detail'),
]