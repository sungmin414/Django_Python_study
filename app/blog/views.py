from django.shortcuts import render

# ListView
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView

from .models import Post


class PostLV(ListView):
    model = Post
    # template_name을 설정하지 않으면 'blog/post_list.html'이 된다.
    template_name = 'blog/post_all.html'
    # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 지정하
    context_object_name = 'posts'
    # 한페이지에 보여주는 객체 리스트의 숫자 2
    # paginate_by속성을 정의하는 것만으로도 장고가 제공하는 페이징 기능을 사용할수있음.
    # 페이징 기능이 활성화 되면 객체 리스트 하단에 페이지를 이동할수 있는 버튼을 만들 수 있다.
    paginate_by = 2


# DetailView
class PostDV(DetailView):
    model = Post


# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    # 기준이되는 날짜 필드는 modify_date 사용,
    # 변경날짜가 최근인 포스트를 먼저 출력
    date_field = 'modify_date'


# 테이블로부터 날짜 필드의 연도를 기준으로 객체 리스트를 가져와, 그 객체들이 속한
# 월을 리스트로 출력
class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    # 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨줌
    make_object_list = True


# 테이블로부터 날짜 필드의 연월을 기준으로 객체 리스트를 가져와,
# 그 리스트를 출력, 날짜 필드의 연도 및 월 파라미터는 URLconf에서 추출해 뷰로 넘겨줌
class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


# 테이블로부터 날짜 필드의 연월일을 기준으로 객체 리스트를 가져와 그 리스트를 출력
# 날짜 필드의 연도, 월, 일 파라미터는 URLconf에서 추출해 뷰로 넘겨줌
class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


# 테이블로부터 날짜 필드가 오늘인  객체 리스트를 가져와, 그리스트를 출력
# 오늘 날짜를 기준 연월일로 지정한다는 점 이외에는 DayArchiveView와 동일
class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'
