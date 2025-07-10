
from django.contrib import admin
from django.urls import path
from firsttodo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="dashboard"),
    path("todo/", todo_list, name="todo"),
    path("create/", create_todo, name="create_todo"),
    path("completed/<int:todo_id>/", complete_todo, name="completed_todo"),
    path("delete/<int:todo_id>/", delete_todo, name="delete"),
    path("register/", register_view, name="registerpage"),
    path("login/", auth_login, name="loginpage"),
]
