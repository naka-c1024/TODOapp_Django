from django.contrib import admin
# q: なぜmodelsの前に.がついているのか？
# a: このファイルと同じディレクトリにあるmodels.pyをインポートするため
# q: .をつけないとどうなるのか？
# a: ModuleNotFoundError: No module named 'models'になる
from .models import Todo

# Register your models here.
admin.site.register(Todo)
