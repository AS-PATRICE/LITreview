from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Ticket
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def list_ticket(request):
    ticket = Ticket.objects.all()
    context = {'ticket':ticket}
    return render(request, 'ticket/list_ticket.html')