from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Review
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def list_review(request):
    posts = Review.objects.all()
    context = {'posts':posts}
    return render(request, 'review/list_review.html', context)


