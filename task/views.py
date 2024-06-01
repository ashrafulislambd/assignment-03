from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import TaskModel
from .forms import TaskForm

def index(request):
    tasks = TaskModel.objects.all()
    return render(request, "task/index.html", {
        "tasks": tasks
    })

def edit(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            return redirect("task:index")

    else:
        form = TaskForm(instance=task)
    return render(request, "task/edit.html", {
        "form": form,
        "task": task
    })

def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task:index")
    else:
        form = TaskForm()
    return render(request, "task/add.html", {"form": form}) 

def delete(request):
    if request.method == "POST":
        try:
            task_id = request.POST["task_id"]
            task = get_object_or_404(TaskModel, pk=task_id)
            task.delete()
            return redirect("task:index")
        except (KeyError, TaskModel.DoesNotExist):
            raise Http404("Task doesn't exist")