from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from follows.models import UserFollows
from follows.forms import FollowForm
from review.models import Review
from ticket.models import Ticket
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def page_abonnement(request):
    followers = UserFollows.objects.filter(user=request.user) # Les utilisateurs qui followent l'utilisateur connecté
    followings = UserFollows.objects.filter(followed_user=request.user) # Les utilisateurs qui sont follow par l'utilisateur connecté
    context = {'followers': followers,
               'followings': followings}
    return render(request, 'follows/subscription.html', locals())


@login_required(login_url='login')
def find_user(request):
    if request.method == "POST":
        query = request.POST.get("user_id")
        
        try:
           following_user = User.objects.get(pk=query)
           UserFollows.objects.create(user=request.user, followed_user=following_user)
        except Exception as e:
            pass
            
        return redirect('page_abonnement')
        

@login_required(login_url='login')
def follow_user(request, user):
    selected_user = User.objects.get(username=user)
    new_following = UserFollows(user=selected_user, followed_user=request.user)
    new_following.save()
    return redirect('page_abonnement')
        

@login_required(login_url='login')
def unfollow_user(request, follow_id):
    following = UserFollows.objects.filter(followed_user=follow_id, user=request.user)
    following.delete()
    return redirect('page_abonnement')



