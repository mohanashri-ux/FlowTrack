from django.shortcuts import render, redirect
from .models import Task, Workflow
from .forms import TaskForm, WorkflowForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home_view(request):
    return render(request, 'workflows/home.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'workflows/task_list.html', {'tasks': tasks})


def workflow_list(request):
    workflows = Workflow.objects.all()
    workflow_data = []

    for wf in workflows:
        tasks = wf.tasks.all()
        total = tasks.count()
        done = tasks.filter(status='done').count()
        progress = int((done / total) * 100) if total > 0 else 0

        workflow_data.append({
            'workflow': wf,
            'progress': progress
        })

    return render(request, 'workflows/workflow_list.html', {'workflow_data': workflow_data})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # ✅ assign logged-in user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'workflows/create_task.html', {'form': form})

@login_required
def create_workflow(request):
    if request.method == 'POST':
        form = WorkflowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workflow_list')
    else:
        form = WorkflowForm()
    return render(request, 'workflows/create_workflow.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'workflows/register.html', {'form': form})
