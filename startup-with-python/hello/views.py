from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

def helloWorldView(request):
    return HttpResponse('Hello, World!')

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
            {'all_items':all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    all_todo_items = TodoItem.objects.all()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')