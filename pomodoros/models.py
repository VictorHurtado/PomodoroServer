from pydoc import describe
from tabnanny import verbose
from django.db import models
from backend_api.models import Users

from base.models import BaseModel
# Create your models here.
#Task
class Task(BaseModel):
    name= models.CharField(max_length=255) 
    description =models.CharField(max_length=255, blank=True, null=True)
    qtPomodoros = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name="Tareas"
        verbose_name_plural="Tareas"

    def __str__(self):
        return   "%s %s (%s)" % (
            self.id,
            self.name,
            self.qtPomodoros
        )

# POMODOROS
class PomodoroTime(BaseModel):
    completed = models.BooleanField() 
    time = models.TimeField()
    typeOf = models.IntegerField()
    startTime = models.TimeField()
    finishTime = models.TimeField()

    idUser = models.ForeignKey(Users, on_delete=models.CASCADE )
    idTask = models.ForeignKey(Task, on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        verbose_name="Pomodoro"
        verbose_name_plural="Pomodoros"

    def __str__(self):
        return   "%s |%s| (%s)" % (
            self.id,
            self.idUser.username,
            self.idTask
        )

