from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from follows.models import UserFollows
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def page_abonnement(request):
    followers = UserFollows.objects.all() #.exclude(request.user)
    context = {'follower': followers}
    return render(request, 'follows/subscription.html', locals())

@login_required(login_url='login')
def unfollow_user(request, pk):
    if request.method =="POST":
        my_profile = UserFollows.objects.get(user=request.user)
        follow = UserFollows.POST.get(id=pk)
        
        if follow.user in my_profile.followed_user.all():
            my_profile.followed_user.remove(follow.user)
    context = {'follow':follow}
    return render(request, 'follows/subscription.html', locals())

@login_required(login_url='login')
def follow_user(request, pk):
    if request.method =="POST":
        my_profile = UserFollows.objects.get(user=request.user)
        follow = UserFollows.POST.get(id=pk)
        
        if follow.user in my_profile.followed_user.all():
            my_profile.followed_user.add(follow.user)
    context = {'follow':follow}
    return render(request, 'follows/subscription.html', locals())
        
        

