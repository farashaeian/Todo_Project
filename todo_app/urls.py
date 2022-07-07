from . import views
from django.urls import path

urlpatterns = [
    path('create_task/', views.CreateTask.as_view(), name='create_task'),
    path('list_task/', views.ListTask.as_view(), name='list_task'),
    path('change_task/<pk>/', views.ChangeTask.as_view(), name='change_task'),
]
