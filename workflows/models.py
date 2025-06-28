# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# User.objects.first()

class Task(models.Model):
    STATUS_CHOICES=[
        ('not_started','Not Started'),
        ('in_progress','In Progress'),
        ('done','Done'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='not_started')
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

class Workflow(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tasks = models.ManyToManyField(Task)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
