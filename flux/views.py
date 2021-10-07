from django.shortcuts import render, redirect
from itertools import chain
from django.db.models import CharField, Value, Q
from django.http.response import HttpResponse
from review.models import Review
from review.forms import ReviewForm
from ticket.models import Ticket
from ticket.forms import TicketForm
from follows.models import UserFollows
from django.contrib.auth.decorators import login_required

# Create your views here.
    
@login_required(login_url='login')
def list_flux(request):
    
    users = []
    user_follows = UserFollows.objects.filter(user=request.user)
    for user_follow in user_follows:
        users.append(user_follow.followed_user)
    users.append(request.user)
    
    
    # Complex lookups with Q objects
    reviews = Review.objects.filter(Q(user__in=users))
    reviews = reviews.annotate(content_type=('REVIEW', CharField()))
    
    
    ticket_with_review = []
    for review in reviews:
        ticket_with_review.append(review.ticket)
        
    tickets = Ticket.objects.filter(Q(user__in=users))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
        
    posts = sorted(chain(tickets, reviews), key=lambda post: post.time_created, reverse=True)   
    
    context = {'posts': posts}
    
    return render(request, 'flux/index.html', context)
 

@login_required(login_url='login')
def create_review(request):
    """create review"""
    form_ticket = TicketForm()
    form_review = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            set_ticket = ticket_form.save(commit=False)
            set_ticket.user = request.user
            
            set_review = review_form.save(commit=False)
            set_review.ticket = set_ticket
            set_review.user = request.user
            
            set_ticket.save()
            set_review.save()
            return redirect('list_flux')
    context = {'ticket_form': form_ticket,
                'review_form': form_review}
    return render(request, "review/create_review.html", context)

@login_required(login_url='login')
def create_ticket(request):
    """create ticket"""   
    if request.method == 'POST':
        form_ticket = TicketForm(request.POST, request.FILES)
        if form_ticket.is_valid():
            ticket = form_ticket.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('list_flux')
        else:
            print(form_ticket.errors.as_data())
    else:
        form_ticket = TicketForm()
        context = {'form_ticket':form_ticket}
    return render(request, 'ticket/create_ticket.html', locals())

        


@login_required(login_url='login')
def answer_ticket(request, ticket_pk_answer):
    """ answer ticket"""
    ticket = Ticket.objects.get(id=ticket_pk_answer)
    if request.method =='POST':
        form_review = ReviewForm(request.POST)
        if form_review.is_valid():
            set_review = form_review.save(commit=False)
            set_review.ticket = ticket[0]
            set_review.user = request.user
            set_review.save()
            return redirect('/')
        else:
            form_review = ReviewForm()
    context = {'form_review':form_review}
    return render(request, "review/answer_ticket.html", context)