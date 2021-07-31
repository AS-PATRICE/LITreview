from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_flux, name='list_flux'),
    path('review_of_followed_user/<str:pk>', views.review_of_followed_user, name='review_of_followed_user'), 
    path('ticket_of_followed_user/<str:pk>', views.ticket_of_followed_user, name='ticket_of_followed_user'),  
]
