from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark
"""
# 기능 추가 : view 생성 -> url 지정 -> url에 맞는 템플릿 제작(이때 urls.py 에서 탬플릿에 넘겨줄 데이터 설정)
class ~View(CreateView or UpdateView or DetailView or DeleteView):
    model = Model 이름
    field = 입력받을 모델의 필드 작성
    success_url = reverse_lazy('url') # 동작 성공시 리디랙션할 url 
    template_name = 해당 뷰에서 사용할 템플릿 경로
    template_name_suffix = '_create' # 템플릿 접미사 변경값 -> template_create.html 
"""


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']       # 어떤 필드를 입력 받을지
    success_url = reverse_lazy('list')  # 글쓰기를 성공 하고 이동할 url
    template_name_suffix = '_create'    # 템플릿 접미사 변경 설정값(= bookmark_create)


class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name_suffix = '_detail'


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')