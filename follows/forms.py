

from django.forms import ModelForm, fields
from .models import UserFollows


class FollowForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ["followed_user"]
        labels = {"followed_user": "Nom d'utilisateurs",}
