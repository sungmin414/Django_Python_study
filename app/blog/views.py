from django.db.models import Q
from django.shortcuts import render

# ListView
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView, TemplateView, FormView
from tagging.views import TaggedObjectList

from .forms import PostSearchForm
from .models import Post


# 테이블 처리가 없이 단순히 템플릿 렌더링 처리만 하는뷰
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


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


# TaggedObjectList 클래스는 ListView를 상속 받는 뷰, 모델과 태그가 주어지면 태그가 달려 있는 모델의 객체리스트를 보여줌
class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


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


# FormView 제네릭 뷰는 GET 요청인 경우 폼을 화면에 보여주고 사용자의 입력을 기다림, 사용자가 폼에 데이터를 입력한 후 제출하면 이는
# POST요청으로 접수되어 FormView 클래스는 데이터에 대한 유효성 검사를 함, 데이터가 유효하면 form_valid()함수를 실핸한 후에
# 적절한 URL로 리다이렉트시키는 기능을 갖고 있음
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

# POST 요청으로 들어온 데이터에 대한 유효성 검사를 실시해 에러가 없으면 form_valid() 메소드를 실행
    def form_valid(self, form):
        # POST 요청의 search_word 파라미터 값을 추출해, schWord 변수에 지정, search_word 파라미터는
        # PostSearchForm 클래스에서 정의한 필드 id
        schWord = self.request.POST['search_word']
        # Q 객체는 filter() 메소드의 매칭 조건을 다양하게 줄수 있도록 함
        # 3개의 조건을 OR 문장으로 연결
        # 각조건의 icontains 연산자는 대소문자를 구분하지 않고 단어가 포함되어 있는지를 검사
        # distinct() 메소드는 중복된 객체는 제외
        # Post 테이블의 모든 레코드에 대해서 title, description, content 컬럼에 schWord 가 포함된 레코드를 대소문자 구별 없이 검색해
        # 서로 다른 레코드들만 리스트로 만들어서 post_list 변수에 지정
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        # 템플릿에 넘겨줄 컨텍스트 변수 context 를 사전 형식으로 정의
        context = {}
        # form 객체, PostSearchForm 객체를 컨텍스트 변수 form에 지정
        context['form'] = form
        # 검색용 단어 schWord를 컨텍스트 변수 search_term에 지정
        context['search_term'] = schWord
        # 검색 결과 리스트인 post_list 를 컨텍스트 변수 object_list 에 지정
        context['object_list'] = post_list
        # 단축함수 render() 템플릿 파일과 컨텍스트 변수를 처리해
        # 최종적으로 HttpResponse 객체를 반환함, form_valid() 함수는 보통 리다이렉트 처리를 위해 HttpResponseRedirect 객체를 반환하는데
        # render 함수에 의해 리다이렉트 처리가 되지 않음
        return render(self.request, self.template_name, context)