
from django.contrib import admin
from django.urls import path
from firsttodo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", todo_list, name="todo"),
    path("create", create_todo, name="create_todo"),
]
