from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/add/', views.task_add, name='task_add'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/complete/', views.task_complete, name='task_complete'),

    path('tags/', views.tag_list, name='tag_list'),
    path('tag/add/', views.tag_add, name='tag_add'),
    path('tag/<int:pk>/update/', views.tag_update, name='tag_update'),
    path('tag/<int:pk>/delete/', views.tag_delete, name='tag_delete'),
    path('toggle/<int:pk>/', views.toggle_task_status, name='toggle_task_status'),
]
