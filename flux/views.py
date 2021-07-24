from django.shortcuts import render
# from itertools import chain
from django.db.models import CharField, Value
from django.http.response import HttpResponse
from review.models import Review
from ticket.models import Ticket
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def list_flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    context = {'ticket': tickets,
               'review': reviews}
    return render(request, 'flux/index.html', locals())

# def feed(request):
#     reviews = get_users_viewable_reviews(request.user)  
#     # returns queryset of reviews
#     reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

#     tickets = get_users_viewable_tickets(request.user) 
#     # returns queryset of tickets
#     tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

#     # combine and sort the two types of posts
#     posts = sorted(
#         chain(reviews, tickets), 
#         key=lambda post: post.time_created, 
#         reverse=True
#     )
#     return render(request, 'feed.html', context={'posts': posts})