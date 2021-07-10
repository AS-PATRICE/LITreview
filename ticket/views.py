from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def list_ticket(request):
    return render(request, 'ticket/list_ticket.html')