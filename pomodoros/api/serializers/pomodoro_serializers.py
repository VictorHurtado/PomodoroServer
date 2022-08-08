from rest_framework import serializers
from pomodoros.models import PomodoroTime


class PomodorosWithUsersSerializer(serializers.ModelSerializer):
    # idUser= UsersSerializer()
    class Meta:
        model = PomodoroTime
        fields = '__all__'
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'time': instance.time,
            'typeOf': instance.typeOf,
            'startTime': instance.startTime,
            'finishTime': instance.finishTime,
            'user': instance.idUser.username,
            'task': {
                'name':instance.idTask.name,
                'description': instance.idTask.description if instance.idTask.description != None else ''
            }if instance.idTask != None else ''
        }

       


class PomodoroTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroTime
        fields = '__all__'

