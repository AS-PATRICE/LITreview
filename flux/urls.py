from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_flux, name='list_flux'),
    path('review_of_followed_user/', views.review_of_followed_user, name='review_of_followed_user'), 
    path('ticket_of_followed_user/', views.ticket_of_followed_user, name='ticket_of_followed_user'),  
]
