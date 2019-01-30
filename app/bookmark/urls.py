from django.urls import path
from .views import *

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
    # 콘텐츠 편집 기능
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('change/', BookmarkChangeLV.as_view(), name='change'),
    path('<pk>/update/', BookmarkUpdateView.as_view(), name='update'),
    path('<pk>/delete/', BookmarkDeleteView.as_view(), name='delete'),
]