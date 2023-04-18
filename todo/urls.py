from django.urls import path
# from . import views
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete

urlpatterns = [
    # 関数ベースビューの場合
    # path(URL, views.関数名, name=URL名称)
    # クラスベースビューの場合
    # path(URL, views.クラス名.as_view(), name=URL名称)

    # q: nameは何をしているのか？
    # a: HTMLのhrefでURLを参照するときに使う
    path("", TodoList.as_view(), name="list"),

    # pkは各タスクに振られているprimary keyの略
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    path("create/", TodoCreate.as_view(), name="create"),
    path("update/<int:pk>", TodoUpdate.as_view(), name="update"),
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"),
]
