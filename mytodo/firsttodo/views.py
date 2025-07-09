from django.shortcuts import render, redirect
from .forms import *
from .models import *
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

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
    return redirect('todo')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect('todo')
    

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed  = True
    todo.save()
    return redirect('todo')