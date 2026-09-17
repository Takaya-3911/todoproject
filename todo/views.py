from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel
from .forms import TodoForm
from django.urls import reverse_lazy

class TodoList(ListView):
    # どのhtmlファイルか
    template_name = 'list.html'
    # どのデータベースか
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # Createビューではフィールド指定が必須
    form_class = TodoForm
    # データ作成終了時に戻す先のURL設定が必要
    # reverse_lazyはクラス内で宣言する。reverseは関数内で宣言する
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
