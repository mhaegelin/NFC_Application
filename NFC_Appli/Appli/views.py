from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django.template import loader
from Appli.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def errorPage(request, errorType):#Page regroupant toutes les erreurs de l'appli
		return render(request, 'error.html', {'errorType' : errorType})

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

def signup(request):
    import hashlib
	#Ajouter l'utilisateur
    uname = request.POST.get('username', '')
    mail = request.POST.get('mail', '')
    fname = request.POST.get('first_name', '')
    lname = request.POST.get('last_name', '')
    upass = request.POST.get('passwd1','')
    hash_object = hashlib.sha1(upass)
    hex_dig = hash_object.hexdigest()
    user = Utilisateur(username=uname, email=mail, first_name=fname, last_name=lname, password=hex_dig)
    user.save()
    return render(request, "login.html")

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
		liste_utilisateurs = Utilisateur.objects.all()
		liste_etudiants = Etudiant.objects.all()
		liste_cours = Cours.objects.all()
		return render(request, 'accueil.html', {'user' : user, 'liste_etud' : liste_etudiants, 'liste_util' : liste_utilisateurs, 'liste_cours' : liste_cours})
	else: #Non-administrateur
		return redirect('fiche')
    else:
	return errorPage(request, 'unknownUser')

def ajaxetud(request):
    idetud = request.GET.get('id', None)
    etud = Etudiant.objects.get(idetud=idetud)
    name = etud.nometud
    surname = etud.prenometud
    mail = etud.mailetud
    data = {
    'name': name,
    'surname': surname,
    'mail': mail
    }
    return JsonResponse(data)

def ajaxutil(request):
    idutil = request.GET.get('id', None)
    if idutil!='#NoSelection#':
        util = Utilisateur.objects.get(idutil=idutil)
        uname = util.username
        fname = util.first_name
        lname = util.last_name
        mail = util.email
    else:
        uname=''
        fname=''
        lname=''
        mail=''
    
    data = {
    'user_name': uname,
    'first_name': fname,
    'last_name': lname,
    'mail': mail
    }
    return JsonResponse(data)

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

def fiche(request):
	user = request.GET.get('user')
	if user is None:
		return errorPage(request, 'unknownUser')

	if request.user.is_authenticated:
		#Il correspondra a l'utilisateur authentifie.
		user = request.user
		print user.id	
		cours = Cours.objects.get(pk=1) #Il correspondra au cours donne par l'utilisateur

		liste_etu = Etudiant.objects.filter(idgroupe__enseigne__idutil=user.id, idgroupe__enseigne__idcours=cours.idcours)
		nbEtudiant = liste_etu.count()
		context = {'list_etu' : liste_etu, 'nbEtudiant' : nbEtudiant, 'user' : user, 'cours' : cours}
		return render(request, "fiche.html", context)
"""
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

