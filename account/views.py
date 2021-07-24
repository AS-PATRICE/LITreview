from django import forms
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUser


# Create your views here.

def page_inscription(request):
    
    form = CreateUser()
    
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Compte créer avec succès pour ' + user)
            return redirect('list_flux')
    context = {'form': form}
    
    return render(request, 'account/inscription.html', context)



def page_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_flux')
        else:
            messages.info(request,"Utilisateur et/ou mot de passe non conforme.")
    return render(request, 'account/login.html', context)


def deconnexion(request):
    logout(request)
    return redirect('login')

