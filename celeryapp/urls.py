from django.urls import path
from . import views

urlpatterns = [
    path('task_1', views.task_1, name='task_1'),
    path('task_2', views.task_2, name='task_2'),
]
