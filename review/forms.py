from django.forms import ModelForm, fields
from django import forms
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('ticket', 'headline', 'rating', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
        
        
        # model = Review
        # fields = ('ticket', 'headline', 'rating', 'body')
        
        # widgets = {
        #     'ticket': forms.TextInput(attrs={'class': 'form-control'}),
        #     'headline': forms.TextInput(attrs={'class': 'form-control'}),
        #     'rating': forms.Select(attrs={'class': 'form-check-input'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        # }