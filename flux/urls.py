from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_flux, name='list_flux'),
    path('create_review/', views.create_review, name='create_review'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('answer_ticket/<int:ticket_pk_answer>', views.answer_ticket, name='answer_ticket'),
    
]
