from django.urls import path

app_name = "task" 

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("edit/<int:task_id>", views.edit, name="edit"),
    path("delete", views.delete, name = "delete"),
    path("add", views.add, name = "add"),
]
