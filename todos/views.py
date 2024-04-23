from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'add_todo.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/delete_todo.html', {'todo': todo})

def edit_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form})
