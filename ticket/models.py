from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Ticket(models.Model):
    """"""
    
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048,
                                blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(null=True,
                              blank=True)
    Time_created = models.DateField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.title
