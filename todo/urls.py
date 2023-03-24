from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update/<int:pk>/', views.UpdateData, name='update'),
    path('delete/<int:pk>/', views.DeleteData, name='delete'),
] 
