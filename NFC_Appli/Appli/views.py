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
"""
def hello(request):
    return HttpResponse("Hello, world. You're at the Appli index.")

def signup(request):
    import hashlib
	#Ajouter l'utilisateur
    import time
    print time.time()
    uname = request.POST.get('username', '')
    mail = request.POST.get('mail', '')
    fname = request.POST.get('first_name', '')
    lname = request.POST.get('last_name', '')
    upass = request.POST.get('passwd1','')
    #validationkey = 
    hash_object = hashlib.sha1(upass)
    hex_dig = hash_object.hexdigest()
    user = Utilisateur(username=uname, email=mail, first_name=fname, last_name=lname, password=hex_dig, validationkey='', validated=0)
    user.save()
    return render(request, "login.html")
"""

def update_scanning(request):
	admin = Utilisateur.objects.get(username="Admin")
	if admin.isscanning == 0:
		admin.isscanning = 1
		admin.save()
	traces = Trace.objects.all()
	ntraces = traces.count()
	if ntraces>0:
		data = { 'tracenfc': traces.first().tracenfc }
		traces.first().delete()
		admin.isscanning = 0
		admin.save()
		return JsonResponse(data)
	else:
		empty_data = {}
		return JsonResponse(empty_data)


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
		if user.issuperuser == 1: #Scolarite (Administrateur)
			liste_utilisateurs = Utilisateur.objects.all()
			liste_etudiants = Etudiant.objects.all()
			liste_cours = Cours.objects.all()
			liste_promo = Promotion.objects.all()
			liste_fiche = Fiche.objects.all()
			return render(request, 'accueil.html', {'user' : user, 'liste_etud' : liste_etudiants, 'liste_util' : liste_utilisateurs, 'liste_cours' : liste_cours, 'liste_promo' : liste_promo, 'liste_fiche' : liste_fiche})

		else: #Professeur (Non-administrateur)
			request.session['userid'] = user.idutil
			request.session.set_expiry(0)
			if user.validated == 1:
				return redirect('fiche')
			else:
				return errorPage(request, 'Compte non activé.')
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
        tracenfc = util.tracenfc
    else:
        uname=''
        fname=''
        lname=''
        mail=''
        tracenfc=''
    data = {
    'user_name': uname,
    'first_name': fname,
    'last_name': lname,
    'mail': mail,
    'tracenfc': tracenfc
    }
    return JsonResponse(data)
    
def ajaxfiche(request):
	import json
	
	idFiche = request.GET.get('id', None)
	fiche = Fiche.objects.get(idfiche=idFiche)
	idfiche = fiche.idfiche
	valide = fiche.valide
	#Ici deux cas se présentent : 
	#Soit la fiche est validée : On récupère les étudiants validés sur la fiche et donc on va chercher dans la table Contient
	#Soit la fiche n'est pas validée : On récupère les étudiants correspondants au groupe du cours correspondant
	if (valide == 1):
		listetud = Etudiant.objects.filter(contient__idfiche = idFiche)
	else:
		cours = Cours.objects.filter(enseigne__idfiche = idFiche) #Le cours correspondant à la fiche
		listetud = Etudiant.objects.filter(appartient__idgroupe = cours[0].idgroupe)
		
	liste = [e.as_json() for e in listetud]

	data = {
		'id': idfiche,
		'valide': valide,
		'listetudfiche': json.dumps(liste)
	}
	return JsonResponse(data)    

def adduser(request):
    import time
    import md5
    import hashlib
    from django.core.mail import send_mail
    username = request.GET.get('username', None)
    try:
        test = Utilisateur.objects.get(username=username)
    except ObjectDoesNotExist:
        nomutil = request.GET.get('nameutil', None)
        prenomutil = request.GET.get('prenomutil',None)
        mailutil = request.GET.get('mailutil',None)
        tracenfc = request.GET.get('tracenfc',None)
        #Mot de passe par defaut
        upass = 'root'
        hash_object = hashlib.sha1(upass)
        hex_dig = hash_object.hexdigest()
        #Generation de la validationkey
        t = time.time()
        key = md5.new(str(t))
        user = Utilisateur(username=username, email=mailutil, first_name=prenomutil, last_name=nomutil, password=hex_dig, validationkey=key.hexdigest(), validated=0, hasbadged=0, tracenfc=tracenfc)
        user.save()
        lastuser = Utilisateur.objects.latest('idutil')
        iduser = lastuser.idutil
        send_mail(
    'eLOG Mailing Confirmation',
    'Bonjour, vous venez de vous inscrire sur eLOG, veuillez confirmer votre inscription à l url suivante : http://127.0.0.1:8000/Appli/accueil/validateAccount?validationkey='+key.hexdigest(),
    'NoReply@elog.com',
    [mailutil],
    fail_silently=False,
    )
    
        data = {
        'id': iduser,
        'last_name': nomutil,
        'first_name': prenomutil,
        }
        return JsonResponse(data)
    empty_data={}
    return JsonResponse(empty_data)

def EcranLogin(request):
	try:
		del request.session['userid']
	except KeyError:
		pass
	return render(request, "login.html")

def log_out(request):
	return redirect('login')


def fiche(request):
	###On récupère l'id de l'utilisateur connecté
	try:	
		user = request.session['userid']
	except KeyError:
		user = None
	if user is None:
		return errorPage(request, 'Opération non autorisée.')
	###	
	
	###On récupère la date et heure actuelle
	date = datetime.datetime.now()
	###
	
	#On récupère le cours correspondant au professeur concerné ET
	#correspondant à la date et heure actuelle
	#cours = Cours.objects.filter(enseigne__idutil = user.idutil, debutcours__lt=date, fincours__gt=date)
	###DEBUG
	cours = Cours.objects.filter(enseigne__idutil = user)
	###
	
	###On récupère la fiche
	fiche = Fiche.objects.filter(enseigne__idutil = user, enseigne__idcours = cours[0].idcours)
	###
	#On récupère le groupe correspondant au cours actuellement donné par le professeur concerné
	groupe = Groupe.objects.filter(cours__idcours = cours[0].idcours)
	#On récupère la liste des étudiants correspondants au groupe, on retire ceux n'ayant pas badgé
	liste_etu = Etudiant.objects.filter(appartient__idgroupe = groupe[0].idgroupe).exclude(hasbadged = 0)
	nbEtudiant = liste_etu.count()
	context = {'list_etu' : liste_etu, 'nbEtudiant' : nbEtudiant, 'user' : user, 'cours' : cours[0], 'fiche' : fiche[0].idfiche}
	return render(request, "fiche.html", context)
"""
		cours = Cours.objects.get(pk=1) #Il correspondra au cours donne par l'utilisateur
		liste_etu = Etudiant.objects.filter(idgroupe__enseigne__idutil=user.id, idgroupe__enseigne__idcours=cours.idcours)
		nbEtudiant = liste_etu.count()
		context = {'list_etu' : liste_etu, 'nbEtudiant' : nbEtudiant, 'user' : user, 'cours' : cours}
		return render(request, "fiche.html", context)
"""
		
def trace(request):
    #print request.session['scanning']
    if request.method == 'POST':
        trace_NFC = request.POST.get('traceNFC')

        if trace_NFC is not None:
            import time
            from datetime import datetime
	        #print time.strftime('%d/%m/%y %H:%M',time.localtime())
            hour = int(time.strftime('%H', time.localtime()))
	        #verifier que nous ne sommes pas dans une periode creuse
            addToTrace = Trace(tracenfc = trace_NFC)
            if hour < 5 or hour > 18:
				return errorPage(request, 'Unauthorized operation.')
			
            try:
				etud = Etudiant.objects.get(tracenfc=trace_NFC)
				#tester aussi si l'utilisateur existe déjà dans Utilisateur.objects
            except ObjectDoesNotExist:
				try:
					util = Utilisateur.objects.get(tracenfc=trace_NFC)
				except ObjectDoesNotExist:
					admin = Utilisateur.objects.get(username="Admin")
					if admin.isscanning==1:
						NFC = Trace(tracenfc=trace_NFC)
						NFC.save()
						return HttpResponse('Ok')
					else:
						return HttpResponse('Error')
				
				util.hasbadged = 1
				util.save()
				return errorPage(request, 'Unauthorized operation.')	
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
    username = request.GET.get('username', None)
    Ok=False
    try:
        test = Utilisateur.objects.get(username=username)
    except ObjectDoesNotExist:
        Ok=True
    
    if Ok or str(test.idutil) == str(idutil):
        mailutil = request.GET.get('mailutil', '')
        prenomutil = request.GET.get('prenomutil', None)
        nomutil = request.GET.get('nameutil', None)
        util = Utilisateur.objects.get(idutil=idutil)
        util.username = username
	#Si le mail a ete change par l'administrateur, alors redemander la validation
        if util.email != mailutil and mailutil != '':
            from django.core.mail import send_mail
            key = util.validationkey
	    send_mail('eLOG Mailing Confirmation',
	    'Bonjour, vous venez de vous inscrire sur eLOG, veuillez confirmer votre inscription à l url suivante : http://127.0.0.1:8000/Appli/accueil/validateAccount?validationkey='+key,
		'NoReply@elog.com',
		[mailutil],
		fail_silently=False)
        util.email = mailutil
        util.first_name = prenomutil
        util.last_name = nomutil
        util.issuperuser = 0
        util.save()
        data = {
            'id': idutil,
            'first_name': prenomutil,
            'last_name': nomutil
            }
        return JsonResponse(data)
    empty_data={}
    return JsonResponse(empty_data)
    
def printfiche(request):
	idfiche = request.GET.get('id', None)
	return errorPage(request, "Impression de la fiche présomptive depuis le secrétariat.")

def validateAccount(request):
    key = request.GET.get('validationkey', None)
    if key is not None:
        user = Utilisateur.objects.get(validationkey=key)
    
        if user.validated != 1:
	    user.validated=1
        else:
            return HttpResponse("Votre compte est déjà activé!")
    
        user.save()
        return HttpResponse("Bonjour, vous avez bien activé votre compte!<br> Vous pouvez vous connecter en suivant <a href=\"http://127.0.0.1:8000/\">ce lien</a>.")
    else:
        return errorPage(request, 'Opération non autorisée.')


def validated(request): #Cette vue permet d'effectuer les traitements suite à la validation de la fiche
	try:	
		user = request.session['userid']
	except KeyError:
		user = None
		
	if user is None:
		return errorPage(request, 'Opération non autorisée.')
	
	idfiche = request.POST.get('fiche','')
	fiche = Fiche.objects.get(idfiche = idfiche)

	list_etu = request.POST.getlist('list_etu')
	for idetudiant in list_etu:
		print idetudiant
		etudiant = Etudiant.objects.get(idetud=idetudiant)
		try:
			dejaPresent = Contient.objects.get(idfiche=fiche, idetud = etudiant)
		except Contient.DoesNotExist:
			addtoFiche = Contient(idfiche=fiche, idetud = etudiant)
			addtoFiche.save()
	#On valide la fiche présomptive dans la BDD
	if fiche.valide == 0:
		fiche.valide = 1
		fiche.save()
	return render(request, 'validated.html')

def test(request):
    return render(request, 'test.html')
