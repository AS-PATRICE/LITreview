from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_review, name='list_review'),
    path('answer_ticket/', views.answer_ticket, name='answer_ticket'),
    path('created_post/', views.created_post, name='created_post'),
    path('updated_post/<str:pk>', views.updated_post, name='created_post'),
    path('deleted_post/<str:pk>', views.deleted_post, name='deleted_post'),
    
]
