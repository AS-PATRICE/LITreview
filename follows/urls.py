from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_abonnement, name='page_abonnement'),
    path('find_user/', views.find_user, name='find_user'), 
    path('follow_user/<user>', views.follow_user, name='follow_user'), 
    path('unfollow_user/<str:follow_id>', views.unfollow_user, name='unfollow_user'),      
]
