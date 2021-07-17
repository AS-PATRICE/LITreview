from django.shortcuts import render
from django.http.response import HttpResponse
from follows.models import UserFollows
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def page_abonnement(request):
    followers = UserFollows.objects.all()
    context = {'follower': followers}
    return render(request, 'follows/abonnement.html', context)

