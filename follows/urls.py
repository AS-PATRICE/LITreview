from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_abonnement, name='page_abonnement'),
    path('follow_user/<str=pk>', views.follow_user, name='follow_user'), 
    # path('unfollow_user/', views.unfollow_user, name='unfollow_user'),
      
]
