from django.shortcuts import render, redirect
from firsttodo.forms import *
from firsttodo.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def todo_list(request):
    data = {}
    form = Todoform(request.POST or None)
    test = Todo.objects.all()
    if form.is_valid():
        form.save()
    data['form'] = form
    data['tests'] = test
    return render(request, 'todo/index.html', data)

@login_required
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
    return redirect('todo')

def home(request):
    data = {}
    test = Todo.objects.all()
    data['tests'] = test
    return render(request, 'todo/dashboard.html',data)

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect('todo')
    

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed  = True
    todo.save()
    return redirect('todo')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('loginpage')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html',{'form':form})

def auth_login(r):
    form = AuthenticationForm(r.POST or None)
    if r.method == "POST":
        username = r.POST.get('username')
        password = r.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(r, user)
            return redirect('todo')
    data = {}
    data['form'] = form
    return render(r, 'auth/login.html', data)

def logout_view(request):
    logout(request)
    return redirect("loginpage")