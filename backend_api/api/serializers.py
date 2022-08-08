

from rest_framework import serializers
from backend_api.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
    def create(self, validated_data):
        user = Users(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        update_user= super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
    def to_representation(self, instance):
        return {
            'idUser': instance['idUser'],
            'username': instance['username']
        }


        
