from django.contrib import admin
from django.urls import path
from .views import TaskCreateSerializer, TaskRetriveUpdateSerialzer, TaskListView, create_task


urlpatterns = [
    path('task/', TaskListView.as_view(), name='task-list'),
    path('createtasks/', TaskCreateSerializer.as_view(), name='create-task'),
    path('updatetasks/<int:pk>/', TaskRetriveUpdateSerialzer.as_view(), name='update-task'),
    path('tasks/create/', create_task , name='create-task'),
]