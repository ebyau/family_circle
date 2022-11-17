from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name='register'),

    #path('customer/<str:pk>/', views.customer, name='customer'),
    path('upload/', views.upload, name='upload'),
    path('update/<str:pk>/', views.update_message, name='update_message'),

    path('audio/<str:pk>/', views.play_audio, name='play_audio'),

]
