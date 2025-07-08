from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.
def todo_list(request):
    data = {}
    form = Todoform(request.POST or None)
    todos = Todo.objects.all()
    if form.is_valid():
        form.save()
    data['form'] = form
    data[todos] = todos
    return render(request, 'todo/index.html', data)

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
    return redirect('todo')