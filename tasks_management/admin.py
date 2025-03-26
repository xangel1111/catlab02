from django.contrib import admin
from .models import Assignee

@admin.register(Assignee)
class AssigneeAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'assigned_date', 'is_active')
    list_filter = ('is_active', 'task', 'user')
