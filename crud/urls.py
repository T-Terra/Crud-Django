from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('users/add/', views.users, name='add_user'),
    path('users/', views.listUsers, name='list_users'),
    path('users/deleteForm/', views.deleteForm, name='deleteForm'),
    path('users/delete/', views.delete, name='delete'),
]
