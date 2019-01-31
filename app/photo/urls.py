from django.urls import path
from .views import *

app_name = 'photo'
urlpatterns = [
    path('', AlbumLV.as_view(), name='index'),
    path('album/', AlbumLV.as_view(), name='album_list'),
    path('album/<pk>/', AlbumDV.as_view(), name='album_detail'),
    path('photo/<pk>/', PhotoDV.as_view(), name='photo_detail'),
    path('album/add/', ALbumPhotoCV.as_view(), name='album_add'),
    path('album/change/', AlbumPhotoLV.as_View(), name='album_change'),
    path('album/<pk>/update/', AlbumPhotoUV.as_view(), name='album_update'),
    path('album/<pk>/delete/', AlbumphotoDV.as_view(), name='album_delete'),
    path('photo/add', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/change/', PhotoChangeLV.as_view(), name='photo_change'),
    path('photo/<pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]