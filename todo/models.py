from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Task(models.Model):
    #enum
    class TaskStatus(models.TextChoices):
        TODO = 'todo',_('Todo')
        IN_PROGRESS = 'in_progress',_('In Progress')
        CLOSED = 'closed',_('Closed')
    
    #columns
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length= 20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    assign = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #table
        db_table = 'tasks'