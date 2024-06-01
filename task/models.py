from django.db import models
from category.models import TaskCategory

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)
    task_assigned = models.DateField()
    categories = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle


