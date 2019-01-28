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
