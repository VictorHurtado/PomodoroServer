

from  rest_framework import status
from rest_framework import viewsets
from  rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from pomodoros.api.serializers.pomodoro_serializers import PomodoroTimeSerializer


class PomodorosViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=PomodoroTimeSerializer


    def get_queryset(self,pk= None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(state=True).first()
    
    def create(self,request):
    
        pomodoro_serializer= self.serializer_class(data=request.data)
        # validation
        if pomodoro_serializer.is_valid():
            pomodoro_serializer.save()
            return Response({"message": "Pomodoro creado correctamente"}, status=status.HTTP_200_OK)
        return Response(pomodoro_serializer.errors) 
    
    def update(self,request, pk=None):
        if self.get_queryset(pk):
            pomodoro_serializer = self.serializer_class(self.get_serializer(pk),data=request.data)
            if pomodoro_serializer.is_valid():
                pomodoro_serializer.save()
                return Response({"message": "Pomodoro actualizado correctamente", "data":pomodoro_serializer.data}, status=status.HTTP_200_OK)
            return Response({'message':'Pomodoro no fue actualizado', 'data':pomodoro_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    

    def destroy(self,request,pk=None):
        pomodoro=self.get_serializer().Meta.model.objects.filter(id=pk).first()
        if pomodoro:
            pomodoro.state=False
            pomodoro.save()
            return Response({'message':'Pomodoro eliminado'}, status=status.HTTP_200_OK)
        return Response({'message':'Pomodoro no fue eliminado'},status=status.HTTP_400_BAD_REQUEST) 
    

# class PomodorosListAPIView(GeneralListAPIView):
#     serializer_class=PomodoroTimeSerializer

# class PomodorosRetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class=PomodoroTimeSerializer
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)

# class PomodorosCreateAPIView(generics.CreateAPIView):
#     serializer_class= PomodoroTimeSerializer
#     def post(self,request):
#         pomodoro_serializer = self.get_serializer()
#         pomodoro_serializer= pomodoro_serializer(data=request.data)
#         # validation
#         if pomodoro_serializer.is_valid():
#             pomodoro_serializer.save()
#             return Response({"message": "Pomodoro creado correctamente"}, status=status.HTTP_200_OK)
#         return Response(pomodoro_serializer.errors) 

# class PomodorosListByUserAPIView(generics.ListAPIView):
#     serializer_class= PomodoroTimeSerializer
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True,idUser=self.kwargs['pk'])

# class PomodorosDestroyAPIView(generics.DestroyAPIView):
#     serializer_class= PomodoroTimeSerializer
#     def delete(self,request,pk=None):
#         pomodoro=self.get_serializer().Meta.model.objects.filter(id=pk).first()
#         if pomodoro:
#             pomodoro.state=False
#             pomodoro.save()
#             return Response({'message':'Pomodoro eliminado'}, status=status.HTTP_200_OK)
#         return Response({'message':'Pomodoro no fue eliminado'},status=status.HTTP_400_BAD_REQUEST) 
    
# class PomodorosUpdateAPIView(generics.UpdateAPIView):
#     serializer_class= PomodoroTimeSerializer
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)

#     def patch(self, request,pk=None):
#         pomodoro =self.get_queryset().filter(id=pk).first()
#         print(pomodoro)
#         if pomodoro:
#             pomodoro_serializer=self.serializer_class(pomodoro)
#             return Response(pomodoro_serializer.data,status=status.HTTP_200_OK)
#         return Response({'message':'Error no se encontro el pomodoro'},status=status.HTTP_400_BAD_REQUEST)

#     def put(self,request, pk=None):
#         pomodoro = self.get_queryset().filter(id=pk).first()
#         if pomodoro:
#             pomodoro_serializer=self.serializer_class(pomodoro)
#             return Response(pomodoro_serializer.data,status=status.HTTP_200_OK)
#         return Response({'message':'Error no se encontro el pomodoro'},status=status.HTTP_400_BAD_REQUEST)

  
# @api_view(['GET'])
# def user_detail_pomodoros_api_view(request, pk):
#     # QuerySet
#     pomodoros = PomodoroTime.objects.filter(idUser=pk).all()
#     # validation
#     if pomodoros:
#         # retrieve
#         if request.method == 'GET':
#             pomodoros_serializer = PomodorosWithUsersSerializer(pomodoros, many=True)

#             return Response({"message": "Resuelto!", "data": pomodoros_serializer.data}, status=status.HTTP_200_OK)
#         # update
        
#     return Response({"message": "No se ha encontrado ningun usuario"}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def pomodoro_time_api_view(request):
#     # list
#     if request.method == 'GET':
#         pomodoros = PomodoroTime.objects.all()
#         pomodoros_serializer = PomodoroTimeSerializer(pomodoros, many=True)
#         return Response({"message": "Resuelto! Pomodoros encontrados", "data": pomodoros_serializer.data}, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         pomodoro_serializer = PomodoroTimeSerializer(data=request.data)
#         # validation
#         if pomodoro_serializer.is_valid():
#             pomodoro_serializer.save()
#             return Response({"message": "Pomodoro creado correctamente"}, status=status.HTTP_200_OK)
#         return Response(pomodoro_serializer.errors)


# @api_view(['GET'])
# def pomodoro_detail_api_view(request, pk):
#     # pomodoro = PomodoroTime.objects.filter(idPomodoro=pk).first()
#     pomodoro = PomodoroTime.objects.filter(id=pk).first()

#     if pomodoro:
#         # retrieve
#         if request.method=='GET':
#                 pomodoro_serializer= PomodoroTimeSerializer(pomodoro)
                
#                 return Response({"message": "Resuelto!" ,"data":pomodoro_serializer.data}, status= status.HTTP_200_OK)