from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )

from django.urls import reverse_lazy

from .models import Todo


class TodoList(ListView):
    model = Todo
    # q: context_object_nameは何をしているのか？
    # a: HTMLテンプレートで使う変数名を指定する
    context_object_name = "tasks"


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"


class TodoCreate(CreateView):
    model = Todo
    # __all__は全てのカラムを指定する、今回はtitle, description, deadline
    fields = ("__all__")

    # reverse_lazyはリダイレクト的なもの、urlpatternsのnameを指定する
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    model = Todo
    fields = ("__all__")
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")
