# This Python file uses the following encoding: utf-8
import os, sys

from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django.template import loader
from Appli.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.core.urlresolvers import reverse
import datetime
from django.contrib import messages

def errorPage(request, errorMessage):#Page regroupant toutes les erreurs de l'appli	
	return render(request, 'error.html', {'errorMessage' : errorMessage})

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
	print user
	if user is not None: #Utilisateur reconnu
		if user.issuperuser == 1: #Scolarite (Administrateur)
			liste_utilisateurs = Utilisateur.objects.all()
			liste_etudiants = Etudiant.objects.all()
			liste_cours = Cours.objects.all()
			liste_promo = Promotion.objects.all()
			return render(request, 'accueil.html', {'user' : user, 'liste_etud' : liste_etudiants, 'liste_util' : liste_utilisateurs, 'liste_cours' : liste_cours, 'liste_promo' : liste_promo})
		else: #Professeur (Non-administrateur)
			request.session['userid'] = user.idutil
			request.session.set_expiry(0)
			return redirect('fiche')
	else:
		return errorPage(request, 'Utilisateur inconnu.')

def ajaxlistetud(request):
	import json
	promo = request.GET.get('id', None)
	listetud = Etudiant.objects.filter(idpromo=promo)
	liste = [e.as_json() for e in listetud]
	data = {
		'listetud': json.dumps(liste)
	}	
	return JsonResponse(data)


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
	try:
		del request.session['userid']
	except KeyError:
		pass
	return render(request, "login.html")

def log_out(request):
	return redirect('login')


def fiche(request):
	try:	
		user = request.session['userid']
	except KeyError:
		user = None
	print user
	if user is None:
		return errorPage(request, 'Opération non autorisée.')
	#On récupère la date et heure actuelle
	date = datetime.datetime.now()
	
	#On récupère le cours correspondant au professeur concerné ET
	#correspondant à la date et heure actuelle
	#cours = Cours.objects.filter(enseigne__idutil = user.idutil, debutcours__lt=date, fincours__gt=date)
	###DEBUG
	cours = Cours.objects.filter(enseigne__idutil = user)
	###	

	#On récupère la fiche présomptive du cours actuellement donné par le professeur concerné
	groupe = Groupe.objects.filter(cours__idcours = cours[0].idcours)
	#On récupère la liste des étudiants correspondants à la fiche présomptive
	liste_etu = Etudiant.objects.filter(appartient__idgroupe = groupe[0].idgroupe)
	nbEtudiant = liste_etu.count()
	context = {'list_etu' : liste_etu, 'nbEtudiant' : nbEtudiant, 'user' : user, 'cours' : cours}
	return render(request, "fiche.html", context)
"""
		cours = Cours.objects.get(pk=1) #Il correspondra au cours donne par l'utilisateur
		liste_etu = Etudiant.objects.filter(idgroupe__enseigne__idutil=user.id, idgroupe__enseigne__idcours=cours.idcours)
		nbEtudiant = liste_etu.count()
		context = {'list_etu' : liste_etu, 'nbEtudiant' : nbEtudiant, 'user' : user, 'cours' : cours}
		return render(request, "fiche.html", context)
"""
		
def trace(request):
    if request.method == 'POST':
        trace_NFC = request.POST.get('traceNFC')

        if trace_NFC is not None:
            import time
            #print trace_NFC
	        #print time.strftime('%d/%m/%y %H:%M',time.localtime())
            hour = int(time.strftime('%H', time.localtime()))
	        #verifier que nous ne sommes pas dans une periode creuse
	        #Comment changer le fuseau horaire?
	        
            if hour < 5 or hour > 18:
				return errorPage(request, 'Could not reach server. Try again later.')
				
            etud = Etudiant.objects.get(tracenfc=trace_NFC)
            etud.hasbadged = 1
            etud.save()
	
    return errorPage(request, 'Unauthorized operation.')
    
def deleteuser(request):
    idutil = request.GET.get('id', None)
    util = Utilisateur.objects.get(idutil=idutil)
    util.delete()
    empty_data={}
    return JsonResponse(empty_data)

def changeuser(request):
    idutil = request.GET.get('id', None)
    util = Utilisateur.objects.get(idutil=idutil)
    util.delete()
    data = {
        'listeutil' : '',
    }
    return JsonResponse(data)


def validated(request): #Cette vue permet d'effectuer les traitements suite à la validation de la fiche
	try:	
		user = request.session['userid']
	except KeyError:
		user = None
		
	if user is None:
		return errorPage(request, 'Opération non autorisée.')
	###DEBUG
	user = Utilisateur.objects.get(idutil=user)
	fiche = Fiche.objects.get(pk=1) # On récupère la fiche présomptive concernée par la validation fiche = request.POST.get('fiche', '')
	###
	
	list_etu = request.POST.getlist('list_etu')
	for idetudiant in list_etu:
		etudiant = Etudiant.objects.get(idetud=idetudiant)
		dejaPresent = Contient.objects.get(idfiche=fiche, idetud = etudiant)
		if dejaPresent is None:
			addtoFiche = Contient(idfiche=fiche, idetud = etudiant)
			addtoFiche.save()
	#On valide la fiche présomptive dans la BDD
	if fiche.valide == 0:
		fiche.valide = 1
		fiche.save()
	return render(request, 'validated.html', {'user' : user})

def test(request):
    toto = 'FFFFA'
    url = reverse('traceNFC', args={'traceNFC' : toto})
    return HttpResponseRedirect(url)
