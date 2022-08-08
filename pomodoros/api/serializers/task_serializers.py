from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from pomodoros.models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model= Task
        fields='__all__'
