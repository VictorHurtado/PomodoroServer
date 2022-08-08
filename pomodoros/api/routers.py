from email.mime import base
from rest_framework.routers import DefaultRouter
from pomodoros.api.views.pomodoros_viewsets import PomodorosViewSet
from pomodoros.api.views.task_viewsets import TaskViewSet


router= DefaultRouter()

router.register('pomodoros',PomodorosViewSet, basename='pomodoro')
router.register('tareas',TaskViewSet, basename='tarea')
urlpatterns= router.urls