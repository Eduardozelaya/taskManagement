from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Rota para listar todas as tarefas
    path('create/', views.task_create, name='task_create'),  # Rota para criar uma nova tarefa
    path('update/<int:pk>/', views.task_update, name='task_update'),  # Rota para editar uma tarefa existente
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),  # Rota para excluir uma tarefa
]
