from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CategoryForm

def index(request):
    return render(request, "base.html")

def add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task:index")

    else:
        form = CategoryForm()
    return render(request, "category/add.html", {"form": form})