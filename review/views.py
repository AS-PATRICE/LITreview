import review
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .models import Review
from ticket.models import Ticket
from .forms import ReviewForm
from ticket.forms import TicketForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def list_review(request):
    posts = Review.objects.all()
    tickets = Ticket.objects.all()
    context = {'tickets': tickets,
               'posts':posts}
    return render(request, 'review/posts.html', locals())


@login_required(login_url='login')
def created_post(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'review/creat_post.html', locals())


@login_required(login_url='login')
def answer_ticket(request, pk):
    ticket = Ticket.objects.get(id = pk)
    form = ReviewForm(instance=ticket)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'review/answer_ticket.html', locals())



@login_required(login_url='login')
def updated_post(request, pk):
    posts = Review.objects.get(id = pk)
    form = ReviewForm(instance=posts)
    if posts.user == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=posts)
            if form.is_valid():
                form.save()
                return redirect('list_review')
    context = {'form':form}
    return render(request, 'review/update_post.html', locals())


@login_required(login_url='login')
def deleted_post(request, pk):
    post = Review.objects.get(id=pk)
    
    if post.user == request.user:
        # if request.method=='POST':
        #     ticket.delete()
        post.delete()        
    return redirect('/')
    
    # context = {'item':post}
    # return render(request, 'review/delete_post.html', locals())


