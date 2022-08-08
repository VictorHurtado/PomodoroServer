
from  rest_framework import status,viewsets
from rest_framework.response import Response
from pomodoros.api.serializers.task_serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class= TaskSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(state=True).first()
    
    def create(self, request):
        task_serializer = self.serializer_class(data=request.data)
        #validation
        if task_serializer.is_valid():
            task_serializer.save()
            return Response({"message": "Tarea creada correctamente"}, status=status.HTTP_200_OK)
        return Response(task_serializer.errors) 

    def update(self, request,pk=None):
        if self.get_queryset(pk):
            task_serializer = self.serializer_class(self.get_serializer(pk),data=request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response({"message": "Pomodoro actualizado correctamente", "data":task_serializer.data}, status=status.HTTP_200_OK)
            return Response({'message':'Pomodoro no fue actualizado', 'data':task_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    def destroy(self, request,pk=None):
        task=self.get_serializer().Meta.model.objects.filter(id=pk).first()
        if task:
            task.state=False
            task.save()
            return Response({'message':'Tarea eliminada'}, status=status.HTTP_200_OK)
        return Response({'message':'La tarea no fue eliminada'},status=status.HTTP_400_BAD_REQUEST) 
       
        