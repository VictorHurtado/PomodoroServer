from django.urls import path
from backend_api.api.api import user_api_view,user_detail_api_view, user_detail_username_api_view
urlpatterns=[
    path('list/', user_api_view,name='user_api'),
    path('<int:pk>/', user_detail_api_view,name='user_api'),
    path('userdetail/', user_detail_username_api_view,name='user_api'),

]