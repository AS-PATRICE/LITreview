from django.shortcuts import render
from itertools import chain
from django.db.models import CharField, Value
from django.http.response import HttpResponse
from review.models import Review
from ticket.models import Ticket
from follows.models import UserFollows
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def list_flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    context = {'ticket': tickets,
               'review': reviews}
    return render(request, 'flux/index.html', locals())

@login_required(login_url='login')
def review_of_followed_user(request, pk):
    profile = UserFollows.objects.get(id=pk)
    users = [user for user in profile.followed_user.all()]
    reviews = []
    qs = None
    
    for u in users:
        p = UserFollows.objects.get(user=u)
        p_review = p.post_set.all()
        reviews.append(p_review)
    my_review = UserFollows.profiles_posts()
    reviews.append(my_review)
    
    if len(reviews)>0:
        qs = sorted(chain(*reviews), reverse=True, key=lambda obj: obj.time_created)
    return render(request, 'flux/index.html', {'profile':profile, 'reviews':qs})


@login_required(login_url='login')
def ticket_of_followed_user(request, pk):
    profile = UserFollows.objects.get(id=pk)
    users = [user for user in profile.followed_user.all()]
    tickets = []
    ts = None
    
    for u in users:
        t = UserFollows.objects.get(user=u)
        p_ticket = t.post_set.all()
        tickets.append(p_ticket)
    my_ticket = UserFollows.profiles_posts()
    tickets.append(my_ticket)
    
    if len(tickets)>0:
        ts = sorted(chain(*tickets), reverse=True, key=lambda obj: obj.Time_created)
    return render(request, 'flux/index.html', {'tickets':ts, 'profile':profile})

