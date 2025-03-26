from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task

class Assignee(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='assignees')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} assigned to {self.task.title}"

    class Meta:
        unique_together = ('task', 'user')
