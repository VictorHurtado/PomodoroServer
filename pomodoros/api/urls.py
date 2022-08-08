from django.urls import path
# from pomodoros.api.api import pomodoro_time_api_view,pomodoro_detail_api_view,user_detail_pomodoros_api_view
from pomodoros.api.views.pomodoros_viewsets import PomodorosDestroyAPIView, PomodorosListAPIView,PomodorosCreateAPIView, PomodorosListByUserAPIView, PomodorosRetrieveAPIView, PomodorosUpdateAPIView
urlpatterns=[
    # path('list/',PomodorosListAPIView.as_view(), name='pomodoro_api' ),
    # path('<int:pk>/',PomodorosRetrieveAPIView.as_view(), name='pomodoro_api' ),
    # path('create/',PomodorosCreateAPIView.as_view(), name='pomodoro_api' ),
    # path('<int:pk>/list',PomodorosListByUserAPIView.as_view(), name='pomodoro_api' ),
    # path('destroy/<int:pk>/',PomodorosDestroyAPIView.as_view(), name='pomodoro_api' ),
    # path('update/<int:pk>/',PomodorosUpdateAPIView.as_view(), name='pomodoro_api' ),
    # path('<int:pk>/pomodoros-list',PomodorosWithUsersSerializer.as_view(), name='pomodoro_api' )
]