from django.contrib import admin
from .models import *
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display= ('id','name')

class PomodoroAdmin(admin.ModelAdmin):
    list_display= ('id','idUser','idTask')

admin.site.register(PomodoroTime,PomodoroAdmin)
admin.site.register(Task,TaskAdmin)