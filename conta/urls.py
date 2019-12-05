from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edittask/<int:id>', views.editTask, name='edit-task'),
    path('deletetask/<int:id>', views.deleteTask, name='delete-task'),
    path('fatura/', views.faturaTask, name='fatura-task'),
    #path('yourname/<str:name>', views.yourName, name='your-name'),
    path('helloworld/', views.helloworld),

]
