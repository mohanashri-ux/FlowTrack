from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('workflows/', views.workflow_list, name='workflow_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('workflows/create/', views.create_workflow, name='create_workflow'),
    path('register/', views.register_view, name='register'),
]
