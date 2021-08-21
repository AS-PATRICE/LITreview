from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from follows.models import UserFollows
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def page_abonnement(request):
    followers = UserFollows.objects.all() #.exclude(request.user)
    context = {'followers': followers}
    return render(request, 'follows/subscription.html', locals())


@login_required(login_url='login')
def follow_user(request, pk):
    if request.method=="POST":# Condition si validation du formulaire
        my_profile = UserFollows.objects.get(user=request.user)# Je fais appel à mon profile
        pk = request.POST.get('profile_pk') # recherche de l'identifiant de l'utilisateur à 
        follow = UserFollows.objects.get(pk=pk)# obtension de la clée primaire de l'utilisateur
        
        if follow.user in my_profile.followed_user.all():# Voire si je suis l'utilisateur
            my_profile.followed_user.add(follow.user)# 
        else:
            my_profile.followed_user.remove(follow.user) # Si oui, je le supprime
            return redirect('page_abonnement')
        
        
    

# @login_required(login_url='login')
# def unfollow_user(request, pk):
#     if request.method =="POST":
#         my_profile = UserFollows.objects.get(user=request.user)# Mon profile
#         pk = request.POST.get('profile_pk') # recherche de l'identifiant de l'utilisateur à 
#         follow = UserFollows.objects.get(pk=pk) 
        
#         if follow.user in my_profile.followed_user.all():# Voire si je suis l'utilisateur
#             my_profile.followed_user.remove(follow.user) # Si oui, je le supprime
#             return redirect('page_abonnement')




        
        

