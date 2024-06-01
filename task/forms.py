from django import forms
from .models import TaskModel
from django.forms.widgets import DateInput

class TaskForm(forms.ModelForm):
    categories = forms.MultipleChoiceField(required=False)
    date_assigned = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TaskModel
        fields = "__all__"
