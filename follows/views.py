from django.shortcuts import render
from django.http.response import HttpResponse
from follows.models import UserFollows

# Create your views here.

def page_abonnement(request):
    followers = UserFollows.objects.all()
    context = {'follower': followers}
    return render(request, 'follows/abonnement.html', context)

