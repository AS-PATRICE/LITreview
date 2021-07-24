import ticket
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def created_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form_ticket = form.save(commit=False)
            form_ticket.user = request.user
            form_ticket.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'ticket/creat_ticket.html', locals())


@login_required(login_url='login')
def updated_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    if ticket.user == request.user:
        if request.method == 'POST':
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('/')
    context = {'form':form}
    return render(request, 'ticket/creat_ticket.html', locals())


@login_required(login_url='login')
def deleted_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if ticket.user == request.user:
        if request.method=='POST':
            ticket.delete()
            return redirect('/')
    context = {'item':ticket}
    return render(request, 'ticket/delete_ticket.html', locals())

