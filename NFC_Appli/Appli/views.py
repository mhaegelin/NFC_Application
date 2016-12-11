from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.template import loader
from Appli.models import *


class LoginForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=100)
    Password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

class AddUser(forms.Form):
    Username = forms.CharField(label='Username', max_length=100)
    Password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    Mail = forms.CharField(label='Mail', max_length=100, widget=forms.EmailInput)
    CHOICES = (('1', 'SuperUtilisateur',), ('2', 'Utilisateur standard',))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

def hello(request):
    return HttpResponse("Hello, world. You're at the Appli index.")

def accueil(request):
    #Verifier que l'utilisateur existe
    username = request.POST.get('Username', '')
    password = request.POST.get('Password', '')
    user = authenticate(username = username, password = password)
    if user is not None:
	if user.is_superuser == 1: #Administrateur
	        login(request, user)
		util = AddUser()
	        return render(request, 'accueil.html', {'formulaire' : util})
	else: #Non-administrateur
		return redirect('fiche')
    else:
        return HttpResponse("Login ou mot de passe incorrect <a href=\"/Appli/\">Reessayer</a>")

def EcranLogin(request):
    form = LoginForm()
    return render(request, 'login.html', {'formulaire' : form })

def log_out(request):
	logout(request)
	return redirect('login')

def fiche(request):
	user = Utilisateur.objects.get(pk=2) #Il correspondra a l'utilisateur authentifie.
	cours = Cours.objects.get(pk=1) #Il correspondra au cours donne par l'utilisateur

	mGroupe = Etudiant.objects.filter(idgroupe__enseigne__idutil=user.idutil, idgroupe__enseigne__idcours=cours.idcours)
	#liste_etu = Etudiant.objects.filter(idgroupe = mGroupe.idgroupe)
	#nbEtudiant = liste_etu.count()
	context = {'list_etu' : mGroupe, 'user' : user, 'cours' : cours}
	return render(request, "fiche.html", context)
