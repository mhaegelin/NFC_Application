from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django.template import loader
from Appli.models import *
from django.core.exceptions import ObjectDoesNotExist

class AddUser(forms.Form):
    Username = forms.CharField(label='Username', max_length=100)
    Password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    Name = forms.CharField(label='Name', max_length=100)
    LastName = forms.CharField(label='LastName', max_length=100)
    Mail = forms.CharField(label='Mail', max_length=100, widget=forms.EmailInput)
    CHOICES = (('0', 'Utilisateur standard'), ('1', 'SuperUtilisateur'))
    choice_field = forms.ChoiceField(label='ChoiceField', widget=forms.RadioSelect, choices=CHOICES)

def hello(request):
    return HttpResponse("Hello, world. You're at the Appli index.")

def accueil(request):
    import hashlib
    #Verifier que l'utilisateur existe
    uname = request.POST.get('name', '')
    upass = request.POST.get('passwd', '')
    hash_object = hashlib.sha1(upass)
    hex_dig = hash_object.hexdigest()
    try:
        user = Utilisateur.objects.get(username=uname, password=hex_dig)
    except ObjectDoesNotExist:
        user = None
    if user is not None: #Utilisateur reconnu
	if user.issuperuser == 1: #Administrateur
		return render(request, 'accueil.html', {'user' : user})
	else: #Non-administrateur
		return redirect('fiche')
        
    else:
        return HttpResponse("Login ou mot de passe incorrect <a href=\"/Appli/\">Reessayer</a>")

"""def addutil(request):
    username = request.POST.get('Username', '')
    password = request.POST.get('Password', '')
    email = request.POST.get('Mail', '')
    choice = request.POST.get('choice_field', '')
    name = request.POST.get('Name', '')
    lastname = request.POST.get('LastName', '')
    util = AddUser()
    utilisateur = User.objects.create_user(username, email, password)
    utilisateur.is_superuser = choice
    utilisateur.first_name = name
    utilisateur.last_name = lastname
    utilisateur.save()
    return render(request, 'accueil.html', {'formulaire' : util})
"""
def EcranLogin(request):
    return render(request, "login.html")

def log_out(request):
	return redirect('login')
"""
def fiche(request):
	#Il correspondra a l'utilisateur authentifie.
	user = request.user
	print user.id	
	cours = Cours.objects.get(pk=1) #Il correspondra au cours donne par l'utilisateur

	liste_etu = Etudiant.objects.filter(idgroupe__enseigne__idutil=user.id, idgroupe__enseigne__idcours=cours.idcours)
	nbEtudiant = liste_etu.count()
	context = {'list_etu' : liste_etu, 'nbEtudiant' : nbEtudiant, 'user' : user, 'cours' : cours}
	return render(request, "fiche.html", context)

def validated(request): #Cette vue recupere la liste des etudiants coches, et met a jour la fiche presompt 
	if request.user.is_authenticated:
		num = request.POST.get('17', '')
		print num
		return render(request, 'validated.html', {'num' : num })
	else:
		return HttpResponse("User inconnu")
"""	
def test(request):
	return render(request, "test.html")

