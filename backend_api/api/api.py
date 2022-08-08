
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from backend_api.api.serializers import UsersSerializer, UserListSerializer
from backend_api.models import Users




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_api_view(request):
    
    # list
    if request.method == 'GET':
        users = Users.objects.all().values('idUser', 'username')
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    # create
    elif request.method == 'POST':
        users_serializer = UsersSerializer(data=request.data)
        # validation
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"message": "Usuario creado correctamente"}, status=status.HTTP_200_OK)
        return Response(users_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk):
    # QuerySet
    user = Users.objects.filter(idUser=pk).first()
    # validation
    if user:
        # retrieve
        if request.method == 'GET':
            user_serializer = UsersSerializer(user)
            return Response({"message": "Resuelto!", "data": user_serializer.data}, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            user_serializer = UsersSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"message": "Resuelto!", "data": user_serializer.data}, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({"message": "Usuario eliminado correctamente!"}, status=status.HTTP_200_OK)
    return Response({"message": "No se ha encontrado ningun usuario"}, status=status.HTTP_400_BAD_REQUEST)


