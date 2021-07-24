from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from follows.models import UserFollows
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def page_abonnement(request):
    followers = UserFollows.objects.all()
    context = {'follower': followers}
    return render(request, 'follows/abonnement.html', locals())

# def FollowForm(request):
#     form = UserFollows()
#     if request.method == 'POST':
#         form = UserFollows(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form':form}
#     return render(request, 'follows/abonnement.html', locals())

