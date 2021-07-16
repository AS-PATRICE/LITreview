from django.shortcuts import render
from django.shortcuts import HttpResponse
from review.models import Review
from ticket.models import Ticket

# Create your views here.

def list_flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    context = {'ticket': tickets,
               'review': reviews}
    return render(request, 'flux/index.html', context)