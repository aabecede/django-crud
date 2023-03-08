from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    # return HttpResponse("hweee")
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks
    }

    return render(request, 'todo/index.html', context)

def show(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task' : task
        }
    except Task.DoesNotExist: #not found
        raise Http404("Data TIdak Ditemukan")
    return render(request, 'todo/detail.html', context)

def createView(request):
    # print(request.method, "method")
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = TaskForm(request.POST)
            new_task.save()
            messages.success(request, 'Sukses Tambah Data')
            return redirect('todo:index')
        print(form, "formnya")
    else:
        form = TaskForm()
    # print(form)
    return render(request, 'todo/form.html', {'form':form})
    
def updateView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/form.html', {'form': form})

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:index')
    return render(request, 'todo/delete-confirm.html', {'task': task})