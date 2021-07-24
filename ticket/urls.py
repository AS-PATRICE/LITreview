from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.created_ticket, name='created_ticket'),
    path('updated_ticket/<str:pk>', views.updated_ticket, name='updated_ticket'),
    path('deleted_ticket/<str:pk>', views.deleted_ticket, name='deleted_ticket'),
    
]
