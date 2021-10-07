import review
from django.shortcuts import redirect, render
from django.http.response import HttpResponse

import ticket
from .models import Review
from ticket.models import Ticket
from .forms import ReviewForm
from ticket.forms import TicketForm
from django.db.models import CharField, Value
from itertools import chain
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def list_posts(request):
    """ show list flow"""
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
    
    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
    return render(request, "review/posts.html",
                  {"posts": posts,
                  "range": range(5)})



@login_required(login_url='login')
def update_review(request, update_pk_review):
    """Update review"""
    review = Review.objects.get(id=update_pk_review)
    form_review = ReviewForm(instance=review)
    if request.method =='POST':
        form_review = ReviewForm(request.POST, instance=review)
        if form_review.is_valid():
            return redirect('/')
    context = {'form_review':form_review}
    return render(request, "review/update_review.html", locals())
    

@login_required(login_url='login')
def delete_review(request, delete_pk_review):
    """Delete review"""
    review = Review.objects.get(id=delete_pk_review)
    review.delate()
    return redirect('/')


@login_required(login_url='login')
def update_ticket(request, update_pk_ticket):
    """update ticket"""
    ticket= Ticket.objects.get(id=update_pk_ticket)
    form_update = TicketForm(request.POST or None,request.FILES or None, instance=ticket)
    if form_update.is_valid():
        form_update.save()
        return redirect("/")
    return render(request, "ticket/update_ticket.html",{"form_update": form_update })
    


@login_required(login_url='login')
def delete_ticket(request, delete_pk_ticket):
    """delate ticket"""
    ticket = Ticket.objects.get(id=delete_pk_ticket)
    ticket.delete()
    return redirect("/")






