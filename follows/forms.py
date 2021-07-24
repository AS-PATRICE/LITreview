from django.forms import ModelForm, fields
from .models import UserFollows

class ReviewForm(ModelForm):
    class Meta:
        model = UserFollows
        fields = '__all__'