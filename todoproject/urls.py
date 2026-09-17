from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 第一引数を空欄にすると自動的にここに入るようになる
    path('', include('todo.urls'))
]
