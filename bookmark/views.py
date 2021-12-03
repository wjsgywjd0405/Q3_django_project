from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView) :
    model = Bookmark # 어떤 모델의 입력을 받을지 설정
    fields = ['site_name', 'url'] # 어떤 필드들을 입력받을지 설정
    success_url = reverse_lazy('bookmark:list') # 북마크 추가를 완료하고 목록 페이지로 이동
    template_name_suffix = '_create' # 사용할 템플릿의 접미사만 변경하는 설정값

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')