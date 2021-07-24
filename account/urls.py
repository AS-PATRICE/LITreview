from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.page_login,name='login'),
    path('quitter', views.deconnexion,name='quitter'),
    path('inscription', views.page_inscription,name='inscription'),
    
]