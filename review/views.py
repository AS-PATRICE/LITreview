from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def list_review(request):
    return render(request, 'review/list_review.html')


