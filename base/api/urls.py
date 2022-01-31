from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('users/', views.getUsers),
    path('users/<str:pk>/', views.getUser),
    path('friends/', views.getFriends),
    path('friends/<str:pk>/', views.getFriends),
]