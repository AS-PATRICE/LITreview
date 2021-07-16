from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class UserFollows(models.Model):
    """"""
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                      on_delete=models.CASCADE,
                      related_name='following')
    follower_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='followed_by')
    
    # class Meta:
    #     # ensures we don't get multiple UserFollows instances
    #     # for unique user-user_followed pairs
    #     unique_together = ('user', 'followed_user',)
    