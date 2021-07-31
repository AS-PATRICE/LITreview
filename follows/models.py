from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class UserFollows(models.Model):
    """"""
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                      on_delete=models.CASCADE,
                      related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='followed_by')
    
    
    def profiles_posts(self):
        return self.post_set.all()
    
    # class Meta:
    #     # ensures we don't get multiple UserFollows instances
    #     # for unique user-user_followed pairs
    #     unique_together = ('user', 'followed_user',)
        
    
    def __str__(self):
        return str(self.user.username)