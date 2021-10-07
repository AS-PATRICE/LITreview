import ticket
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url='login')
# def ticket(request, ticket_id_edit=False, ticket_id_del=False):
#     if ticket_id_edit:
#         ticket = Ticket.objects.get(id=ticket_id_edit)
#         form_ticket=TicketForm(instance=ticket)
#         if request.method == 'POST':
#             form_ticket = TicketForm(request.POST, request.FILES, instance=ticket)
#             if form_ticket.is_valid():
#                 form_ticket.save()
#                 return redirect('/')
#         context = {'form_ticket' : form_ticket}
#         return render (request, 'ticket/ticket.html', context)
    
#     if ticket_id_del:
#         ticket = Ticket.objects.get(id=ticket_id_del)
#         ticket.delate()
#         return redirect('/')
    
#     if not ticket_id_edit and not ticket_id_del:
#         form_ticket = TicketForm()
#         if request.method == 'POST':
#             form_ticket = TicketForm(request.POST, request.FILES)
#             if form_ticket.is_valid():
#                 set_ticket = form_ticket.save(commit=False)
#                 set_ticket.user = request.user
#                 set_ticket.save()
#                 return redirect('/')
#         context = {'form_ticket' : form_ticket}
#         return render (request, 'ticket/ticket.html', context)


# @login_required(login_url='login')
# def updated_ticket(request, pk):
#     ticket= Ticket.objects.get(id=pk)
#     form_update = TicketForm(request.POST or None,request.FILES or None, instance=ticket)
#     if form_update.is_valid():
#         form_update.save()
#         return redirect("list_posts")
#     return render(request, "ticket/update_ticket.html",{"form_update": form_update })
    



