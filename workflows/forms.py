from django import forms
from .models import Task, Workflow

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','status']

class WorkflowForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['name', 'description', 'tasks']
        widgets = {
            'tasks': forms.CheckboxSelectMultiple
        }
