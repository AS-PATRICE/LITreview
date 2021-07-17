from django.shortcuts import render
from django.shortcuts import HttpResponse
from review.models import Review
from ticket.models import Ticket
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def list_flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    context = {'ticket': tickets,
               'review': reviews}
    return render(request, 'flux/index.html', locals())