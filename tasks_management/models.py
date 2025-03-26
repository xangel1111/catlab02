from django.db import models
from django.contrib.auth.models import User  # Importar el modelo User de Django
from tasks.models import Task  # Asumiendo que el modelo Task está en la app llamada 'tasks'

class Assignee(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='assignees')  # Relaciona la tarea
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')  # Relaciona el usuario
    assigned_date = models.DateTimeField(auto_now_add=True)  # Fecha en que se asignó la tarea
    is_active = models.BooleanField(default=True)  # Para saber si la asignación sigue activa

    def __str__(self):
        return f"{self.user.username} assigned to {self.task.title}"

    class Meta:
        unique_together = ('task', 'user')  # Garantiza que un usuario no sea asignado más de una vez a la misma tarea
