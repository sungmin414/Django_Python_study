from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# from config.views import LoginRequiredMixin
from .forms import PhotoInlineFormSet
from .models import Album, Photo


class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)


class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')


class AlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')


# LoginRequiredMixin, CreateView 상속받아 AlbumPhotoCV 뷰를 작성
# LoginRequireMixin은 @login_required 데코레이터 기능을 함, CreateView 클래스를 상속 받는 클래스는 중요한 몇 가지 클래스 속성만 정의해주면
# 적절한 폼을 보여주고 폼에 입력된 내용에서 에러 여부를 체크하고 에러가 없으면 입력된 내용으로 테이블에 레코드를 생성
class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['name', 'description']
    template_name = 'photo/album_form.html'

# 장고에서 제공하는 디폴트 컨텍스트 변수 이외에 추가적인 컨텍스트 변수를정의하기 위해 get_context_data() 메소드를 오버라이딩 정의
    def get_context_data(self, **kwargs):
        # AlbumPhotoCV 부모 클래스의 get_context_data() 호출해 기본 컨텍스트 변수를 설정,
        # 기본 컨텍스트 변수 이외에도 메인 폼도 컨텍스트 변수에 추가
        context = super(AlbumPhotoCV, self).get_context_data(**kwargs)
        # POST 요청인 경우, formset 컨텍스트 변수를 request.POST 와 request.FILES 파라미터를 사용해 지정함
        # request.FILES 파라미터를 추가한 이유는 파일 업로드가 이뤄지기 떄문
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            # GET 요청인 경우, formset 컨텍스트 변수에 빈 폼셋을 지정
            context['formset'] = PhotoInlineFormSet()
        return context

    # 유효성 검사를 수행해 에러가 없는 경우, form_valid() 메소드를 호출
    def form_valid(self, form):
        # 폼의 owner 필드에는 현재 로그인된 사용자의 User 객체를 할당, 즉 앨범 폼의 owner 필드를 자동으로 지정
        form.instance.owner = self.request.user
        # get_context_date() 메소드를 호출해, context 컨텍스트 사전을 지정
        context = self.get_context_data()
        formset = context['formset']
        # 폼셋에 들어 있는 각 폼의 owner 필드에 현재 로그인된 사용자의 User 객체를 할당, 폼셋에 들어 있는 각 사진 폼의 owner 필드를 자동으로 지정
        for photoform in formset:
            photoform.instance.owner = self.request.user
        # 폼셋에 들어 있는 각 사진 폼의 데이터가 모두 휴효한지 확인
        if formset.is_valid():
            # form.save() 를 호출해 폼의 데이터를 테이블에 지정, 앨범 레코드를 하나 생성한 것
            self.object = form.save()
            # 폼셋의 메인 객체를 방금 테이블에 저장한 객체로 지정
            formset.instance = self.object
            # formset.save() 를 호출해 폼셋의 데이터를 테이블에 저장, form.save()로 인해 생성한 앨범 레코드에 1:N 관계로 연결된 여러 개의
            # 사진 레코드를 테이블에 저장
            formset.save()
            # 마지막으로 앨범 객체의 get_absolute_url() 메소드를 호출해 페이지를 이동, 앨범 상세 페이지로 리다이렉트
            return redirect(self.object.get_absolute_url())
        else:
            # 폼셋의 데이터가 유효하지 않으면, 다시 메인 폼 및 인라인 폼셋을 출력
            # 폼과 폼셋에는 직전에 사용자가 입력한 데이터를 다시 보여줌
            return self.render_to_response(self.get_context_data(form=form))


class AlbumPhotoUV(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['name', 'description']
    template_name = 'photo/album_form.html'

    def get_context_data(self, **kwargs):
        # 부모 클래스의 get_context_date() 호출해 기본 컨텍스트 변수를 설정
        context = super(AlbumPhotoUV, self).get_context_data(**kwargs)
        # POST 요청인 경우, formset 컨텍스트 변수를 request.POST 와 request.FILES 파라미터를 사용해 지정
        # instance 파라미터에 현재의 앨범 객체를 지정
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            # GET 요청인 경우, formset 컨텍스트 변수에 현재의 앨범 객체와 연결된 폼셋을 지정
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
