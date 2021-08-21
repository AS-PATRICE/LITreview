from django.shortcuts import render
from itertools import chain
from django.db.models import CharField, Value
from django.http.response import HttpResponse
from review.models import Review
from ticket.models import Ticket
from follows.models import UserFollows
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def list_flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    context = {'ticket': tickets,
               'review': reviews}
    return render(request, 'flux/index.html', locals())

@login_required(login_url='login')
def review_of_followed_user(request):
    profile = UserFollows.objects.filter(user=request.user)# ici j'ai remplacé get() par filter. 
    reviews = []
    qs = None
    for u in profile:
        p = UserFollows.objects.get(user=u)
        p_review = p.post_set.all()
        reviews.append(p_review)
    my_review = UserFollows.profiles_posts()
    reviews.append(my_review)
    
    if len(reviews)>0:
        qs = sorted(chain(*reviews), reverse=True, key=lambda obj: obj.time_created)
    return render(request, 'flux/index.html', {'profile':profile, 'reviews':qs})




@login_required(login_url='login')
def ticket_of_followed_user(request):
    # se connecter à mon profil d'utilisateur
    profile = UserFollows.objects.filter(user=request.user)
    # Vérifier qui nous suivons
    users = [user for user in profile.followed_user.all()]
    # initialiser une variable(un tableau)
    tickets = []
    ts = None
    # Recevoir les posts des personnes que nous suivons
    for u in users:# Pour chaque utilisateur parmis les utilisateurs
        t = UserFollows.objects.get(user=u)# définition d'une variable t pour cet utilisateur particulier
        p_ticket = t.post_set.all()# Envoyer un ticket à l'utilisateur
        tickets.append(p_ticket)#J'ajoute ce ticket à la variable ticket[] déclarées plus haut
    # Mes propores tickets
    my_ticket = UserFollows.profiles_posts()
    tickets.append(my_ticket)
    # trier et chaîner les ensembles de requêtes et décompresser la liste des publications
    if len(tickets)>0:
        ts = sorted(chain(*tickets), reverse=True, key=lambda obj: obj.Time_created)
    return render(request, 'flux/index.html', {'tickets':ts, 'profile':profile})

