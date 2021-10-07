from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('update_review/<int:update_pk_review>', views.update_review, name='update_review'),
    path('delete_review/<int:delete_pk_review>', views.delete_review, name='delete_review'),
    path('update_ticket/<int:update_pk_ticket>', views.update_ticket, name='update_ticket'),
    path('delete_ticket/<int:delete_pk_ticket>', views.delete_ticket, name='delete_ticket'),
]
