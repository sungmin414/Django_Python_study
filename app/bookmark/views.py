from django.shortcuts import render
# 클래스형 제네릭 뷰를 사용하기 위해 ListView, DetailView 클래스를 임포트
from django.views.generic import ListView, DetailView

from .models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark