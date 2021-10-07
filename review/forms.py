from django.forms import ModelForm, fields
from django import forms
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'headline', 'rating', 'body']