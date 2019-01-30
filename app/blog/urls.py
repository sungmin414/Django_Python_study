from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('post/', PostLV.as_view(), name='post_list'),
    path('post/<slug>/', PostDV.as_view(), name='post_detail'),
    path('archive/', PostAV.as_view(), name='post_archive'),
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),
    path('<int:year>/<month>/', PostMAV.as_view(), name='post_month_archive'),
    path('<int:year>/<month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),
    path('today/', PostTAV.as_view(), name='post_today_archive'),
    # 태그 클라우드를 보여주기 위한 뷰로 템플릿 처리만 하면 되므로 TemplateView를 상속받아 정의
    path('tag/', TagTV.as_view(), name='tag_cloud'),
    path('tag/<tag>/', PostTOL.as_view(), name='tagged_object_list'),
    path('search/', SearchFormView.as_view(), name='search'),
    # 콘텐츠 편집기능
    path('add/', PostCreateView.as_view(), name='add'),
    path('change/', PostChangeLV.as_view(), name='change'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/<pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
