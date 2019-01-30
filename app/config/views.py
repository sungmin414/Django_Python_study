from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


class HomeView(TemplateView):
    template_name = 'home.html'


# /accounts/register/ URL을 처리하는 뷰, 폼에 입력된 내용에서 에러 여부를 체크한 후 에러가 없으면 입력된 내용으로 테이블에 레코드를 생성
class UserCreateView(CreateView):
    template_name = 'register/register.html'
    form_class = UserCreationForm
    # 폼에 입력된 내용이 에러가 없고 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정함
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'register/register_done.html'


# login_required() 함수는 함수에만 적용할수 있으므로 클래스형 뷰에서는 LoginRequireMixin 클래스를 상속받아
# 사용하면 login_required() 데코레이터 기능을 제공할 수 있음
class LoginRequiredMixin(object):
    # as_view() 메소드를 인스턴스 메소드가 아니라 클래스 메소드로 정의, as_view() 메소드는 항상 클래스 메소드로 정의
    @classmethod
    def as_view(cls, **initkwargs):
        # super() 메소드에 의해 LoginRequiredMixin의 상위 클래스에 있는 as_view() 메소드가
        # view 변수에 할당
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        # view 변수, 즉 LoginRequiredMixin의 상위 클래스에 있는 as_view() 메소드에 Login_required()
        # 기능을 적용하고 그 결과를 반환
        return login_required(view)