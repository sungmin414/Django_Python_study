from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# 클래스형 제네릭 뷰를 사용하기 위해 ListView, DetailView 클래스를 임포트
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark


# LoginRequiredMixin 클래스를 상속받는 클래스는 로그인된 경우만 접근 가능
# 로그인이 되지 않는 상태에서 BookmarkCreateView 뷰를 호출하면 로그인 페이지로 이동
# 폼에 입력된 내용에서 에러 여부를 체크한후 에러가 없으면 입력된 내용으로 테이블에 레코드를 생성
class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    # 폼에 입력된 내용에 대해 유효성 검사
    def form_valid(self, form):
        # 현재 로그인된 사용자의 User 객체를 할당
        form.instance.owner = self.request.user
        # 부모 클래스 즉 CreateView 클래스의 form_valid()메소드를 호출
        return super(BookmarkCreateView, self).form_valid(form)


# 로그인이 되면 ListView 보여주기
class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    # get_queryset() 메소드는 화면에 출력할 레코드 리스트를 반환
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')