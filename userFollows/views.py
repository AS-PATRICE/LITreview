from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def list_userFollows(request):
    return render(request, 'userFollows/list_userFollows.html')