from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Домашня сторінка
    path('tags/', views.tag_list, name='tag_list'),  # Сторінка списку тегів
]
