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
    stopscanning=request.GET.get('stopscanning', None)
    print stopscanning
    admin = Utilisateur.objects.get(username="Admin")
    if stopscanning==str(0):
        if admin.isscanning == 0:
            admin.isscanning = 1
            admin.save()
            print 'Ok!!'
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
    else:
        admin.isscanning=0
        admin.save()
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
            liste_groupe = Groupe.objects.all()
            return render(request, 'accueil.html', {'user' : user, 'liste_groupe' : liste_groupe, 'liste_etud' : liste_etudiants, 'liste_util' : liste_utilisateurs, 'liste_cours' : liste_cours, 'liste_promo' : liste_promo, 'liste_fiche' : liste_fiche})

        else: #Professeur (Non-administrateur)
            request.session['userid'] = user.idutil
            request.session.set_expiry(0)
            print "OK"
            if user.validated == 1:
                return redirect('fiche')
            else:
                return errorPage(request, 'Compte non activé.')
    else:
        return errorPage(request, 'Utilisateur inconnu.')


def ajaxdelpromo(request):
    import json
    idpromo = request.GET.get('idpromo', None)
    promo = Promotion.objects.get(idpromo=idpromo)
    promo.delete()
    data = {
    'idpromo':idpromo
    }
    return JsonResponse(data)
    
    
    
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def ajaxaddpromo(request):
    import json
    intitule = request.GET.get('intitule', None)
    groupes = request.GET.get('groupes', None)
    print groupes
    promo = Promotion(intitulepromo=intitule)
    promo.save()
    latest = Promotion.objects.latest('idpromo')
    cpt=0
    for i in range(len(groupes)):
        if is_number(groupes[i]):
            cpt=10*cpt+int(groupes[i])
        else:
            if cpt!=0:
                groupe = Groupe.objects.get(idgroupe=cpt)
                groupe.idpromo = latest
                groupe.save()
                cpt=0
    data = {
    'idpromo':latest.idpromo,
    'intitule':intitule
    }
    return JsonResponse(data)

def ajaxdelgroupe(request):
	import json
	idgroupe = request.GET.get('idgroupe', None)
	
	data = {}
	
	return JsonResponse(data)
	

def ajaxchangepromo(request):
    import json
    idpromo = request.GET.get('idpromo', None)
    intitule = request.GET.get('intitule', None)
    groupes = request.GET.get('groupes', None)
    promo = Promotion.objects.get(idpromo=idpromo)
    promo.intitulepromo = intitule
    promo.save()
    cpt=0
    #Passer à null l'idpromo des groupes supprimés de la promotion!
    groups = Groupe.objects.filter(idpromo=idpromo)
    listeid = []
    listenew = []
    for i in range(groups.count()):
        listeid.append(groups[i].idgroupe)

    for i in range(len(groupes)):
        if is_number(groupes[i]):
            cpt=10*cpt+int(groupes[i])
        else:
            if cpt!=0:
                listenew.append(cpt)
                cpt=0

    for i in range(len(listeid)): # On passe tous les idpromo à NULL dans la liste d'origine
		groupe = Groupe.objects.get(idgroupe=listeid[i])
		groupe.idpromo = None
		groupe.save()    
    
    for i in range(len(listenew)): #On ajoute les bonnes valeurs pour les groupes concernés
        groupe = Groupe.objects.get(idgroupe=listenew[i])
        groupe.idpromo = promo
        groupe.save()

    data = {
    'idpromo':idpromo,
    'intitule':intitule
    }
    return JsonResponse(data)

def ajaxlistetud(request):
    import json
    promo = request.GET.get('id', None)
    listetud = Etudiant.objects.filter(idpromo=promo)
    liste = [e.as_json() for e in listetud]
    data = {
        'listetud': json.dumps(liste)
    }    
    return JsonResponse(data)

def ajaxlistpromo(request): #MAJ des champs du formulaire promo
    import json
    idpromo = request.GET.get('id', None)
    promo = Promotion.objects.get(idpromo=idpromo)
    intitule = promo.intitulepromo
    listgroupes = Groupe.objects.filter(idpromo=idpromo)
    liste = [e.as_json() for e in listgroupes]
    data = {
        'intitule':intitule,
        'listgroupes': json.dumps(liste)
    }    
    return JsonResponse(data)

def ajaxetud(request):
    import json
    idetud = request.GET.get('id', None)
    etud = Etudiant.objects.get(idetud=idetud)
    name = etud.nometud
    surname = etud.prenometud
    mail = etud.mailetud
    tracenfc = etud.tracenfc
    listegroupes = Appartient.objects.filter(idetud=idetud).values('idgroupe')
    data = {
    'name': name,
    'surname': surname,
    'mail': mail,
    'tracenfc': tracenfc,
    'groupes': list(listegroupes)
    }
    return JsonResponse(data)


def ajaxaddetud(request):
    import json
    etudnom = request.GET.get('etudnom', None)
    etudprenom = request.GET.get('etudprenom', None)
    etudmail = request.GET.get('etudmail', None)
    etudtracenfc = request.GET.get('etudtracenfc', None)
    etudgroupes = request.GET.get('etudgroupes', None)
    idpromo = request.GET.get('idpromo', None)
    promo = Promotion.objects.get(idpromo=idpromo)
    etud = Etudiant(nometud=etudnom, prenometud=etudprenom, mailetud=etudmail, tracenfc=etudtracenfc, hasbadged=0, idpromo=promo)
    etud.save()
    lastetud = Etudiant.objects.latest('idetud')
    idetud = lastetud.idetud
    cpt=0
    for i in range(len(etudgroupes)):
        if is_number(etudgroupes[i]):
            cpt=10*cpt+int(etudgroupes[i])
        else:
            if cpt!=0:
                groupe = Groupe.objects.get(idgroupe=cpt)
                appartient = Appartient(idgroupe=groupe, idetud=etud)
                appartient.save()
                cpt=0
    
    data={
    'idetud': idetud,
    'nom': etudnom,
    'prenom': etudprenom
    }
    return JsonResponse(data)
    

def ajaxchangeetud(request):
    import json
    idetud = request.GET.get('idetud', None)
    etudnom = request.GET.get('etudnom', None)
    etudprenom = request.GET.get('etudprenom', None)
    etudmail = request.GET.get('etudmail', None)
    etudtracenfc = request.GET.get('etudtracenfc', None)
    etudgroupes = request.GET.get('etudgroupes', None)
    etud = Etudiant.objects.get(idetud=idetud)
    etud.nometud = etudnom
    etud.prenometud = etudprenom
    etud.mailetud = etudmail
    etud.tracenfc = etudtracenfc
    etud.save()
    cpt=0
    Appartient.objects.filter(idetud=idetud).delete()    
    for i in range(len(etudgroupes)):
        if is_number(etudgroupes[i]):
            cpt=10*cpt+int(etudgroupes[i])
        else:
            if cpt!=0:
                groupe = Groupe.objects.get(idgroupe=cpt)
                appartient = Appartient(idgroupe=groupe, idetud=etud)
                appartient.save()
                cpt=0
    
    data={
    'idetud': idetud,
    'nom': etudnom,
    'prenom': etudprenom
    }
    return JsonResponse(data)
    
def changepassword(request):
    import json
    import hashlib
    try:    
        user = request.session['userid']
    except KeyError:
        user = None
    if user is None:
        return errorPage(request, 'Opération non autorisée.')
        
    newPassword = request.POST.get('newPassword', None)
    oldPassword = request.POST.get('oldPassword', None)
    if (newPassword == "" or oldPassword == ""):
		return errorPage(request, "Champ non renseigné")
    hash_object = hashlib.sha1(oldPassword)
    hex_dig = hash_object.hexdigest()
    util = Utilisateur.objects.get(idutil=user)
    if (util.password != hex_dig):
        return errorPage(request, 'Ancien mot de passe incorrect')
    hash_object = hashlib.sha1(newPassword)
    util.password = hash_object.hexdigest()
    util.save()
    return render(request, "fiche.html") 

def ajaxdeletud(request):
    import json
    idetud = request.GET.get('idetud', None)
    print idetud
    etud = Etudiant.objects.get(idetud=idetud)
    etud.delete()
    data = {
    'idetud':idetud
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
    #On récupère les étudiants correspondants au groupe du cours actuel
    cours = Cours.objects.filter(enseigne__idfiche = idFiche) #Le cours correspondant à la fiche
    liste = []
    try:
        agroupe = AGroupe.objects.filter(idcours=cours[0].idcours)
    except IndexError:
        data = {
        'id': " ",
        'valide': "",
        'listetudfiche': json.dumps(liste)
        }
        return JsonResponse(data)		
    for i in range(agroupe.count()):
        listetud = Etudiant.objects.filter(appartient__idgroupe = agroupe[i].idgroupe)
        for etud in listetud:
            try:
                presence = ' '
                dejaPresent = Contient.objects.get(idfiche=idfiche, idetud = etud.idetud)
            except Contient.DoesNotExist:
                presence = 'Absent' 
            dict = etud.as_json()
            dict['presence'] = presence    
            liste = liste + [dict]
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
        user = Utilisateur(username=username, email=mailutil, issuperuser=0, first_name=prenomutil, last_name=nomutil, password=hex_dig, validationkey=key.hexdigest(), validated=0, hasbadged=0, tracenfc=tracenfc)
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
    import time
    from datetime import date
    from datetime import datetime
    ###On récupère l'id de l'utilisateur connecté
    try:    
        user = request.session['userid']
    except KeyError:
        user = None
    if user is None:
        return errorPage(request, 'Opération non autorisée.')
    ###

    now=datetime.now()
    print now
    #On récupère le cours correspondant au professeur concerné ET
    #correspondant à la date et heure actuelle
    cours = Cours.objects.filter(enseigne__idutil = user)
    cours = cours.filter(debutcours__lte=datetime(now.year, now.month, now.day, now.hour + 2, now.minute, now.second), fincours__gte=datetime(now.year, now.month, now.day, now.hour + 1, now.minute, now.second))

    
    ###On récupère la fiche
    try:
        fiche = Fiche.objects.filter(enseigne__idutil = user, enseigne__idcours = cours[0].idcours)
        #On récupère l'ensemble des groupes correspondant au cours actuellement donné par le professeur concerné
        groupe = Groupe.objects.filter(agroupe__idcours = cours[0].idcours)
        #On récupère la liste des étudiants correspondants au groupe, on retire ceux n'ayant pas badgé
        liste_etu = Etudiant.objects.filter(appartient__idgroupe = groupe[0].idgroupe).exclude(hasbadged = 0)
        nbEtudiant = liste_etu.count()
        context = {'list_etu' : liste_etu, 'nbEtudiant' : nbEtudiant, 'user' : user, 'cours' : cours[0], 'fiche' : fiche[0].idfiche}
    except IndexError:
        context = {'list_etu' : " ", 'nbEtudiant' : " ", 'user' : user, 'cours' : " ", 'fiche' : " "}
    ###
    return render(request, "fiche.html", context)

        
def trace(request):
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
            send_mail(
    'eLOG Mailing Confirmation',
    'Bonjour, vous venez de vous inscrire sur eLOG, veuillez confirmer votre inscription à l url suivante : http://127.0.0.1:8000/Appli/accueil/validateAccount?validationkey='+str(key),
    'NoReply@elog.com',
    [mailutil],
    fail_silently=False,
    )
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
    
def changefiche(request):
    idFiche = request.GET.get('idFiche', None)
    valide = request.GET.get('valide', None)
    fiche = Fiche.objects.get(idfiche=idFiche)
    fiche.valide = valide
    fiche.save()
    data = {
        'id': idFiche,
        'valide': valide
        }
    return JsonResponse(data)
    
        
def printfiche(request):
    from reportlab.pdfgen import canvas
    from reportlab.platypus import Table, TableStyle, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
    from reportlab.lib import colors, pagesizes
    from reportlab.lib.units import cm
    
    idfiche = request.POST.get('print_fiche', None)
    if idfiche is None:
        return errorPage(request, "Impression impossible. La fiche n'est pas reconnue.")
    
    #On recupere le cours correspondant à la fiche
    cours = Cours.objects.filter(enseigne__idfiche = idfiche)
    
    #On recupere le professeur correspondant à la fiche
    prof = Utilisateur.objects.filter(enseigne__idfiche = idfiche)
    
    agroupe = AGroupe.objects.filter(idcours=cours[0].idcours)
    
    #On recupere la fiche
    fiche = Fiche.objects.get(idfiche=idfiche)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="FichePresomptive'+str(idfiche)+'.pdf"'
	
    p = canvas.Canvas(response)
    
    (width, height) = pagesizes.A4
    
    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_LEFT
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER

    p.drawString(width/2 - 50, height - 30, "FICHE PRESOMPTIVE N°"+str(idfiche))
    p.setLineWidth(.3)
    p.line(10,height - 50,width - 10,height - 50)
    
    p.drawString(15, height - 100, "Professeur : "+str(prof[0].first_name)+" "+str(prof[0].last_name))
    p.drawString(15, height - 150, "Cours : "+str(cours[0].intitulecours))
    if fiche.valide == 1:
        p.drawString(width - 120, height - 100, "Statut : Validé")
    else:
        p.drawString(width - 120, height - 100, "Statut : Non validé")

    p.line(10,height - 175,width - 10,height - 175)
    
    hnom = Paragraph('''<b>Nom</b>''', styleBH)
    hprenom = Paragraph('''<b>Prenom</b>''', styleBH)
    hpresence = Paragraph('''<b>Présence</b>''', styleBH)

    data = []
    data.append([hnom, hprenom, hpresence])    
    for i in range(agroupe.count()):
        listetud = Etudiant.objects.filter(appartient__idgroupe = agroupe[i].idgroupe)
        for user in listetud:
            try:
                presence = ' '
                dejaPresent = Contient.objects.get(idfiche=idfiche, idetud = user.idetud)
            except Contient.DoesNotExist:
                presence = 'Absent'
            data.append([user.nometud, user.prenometud, presence])
        
    table = Table(data, colWidths=[width/3.0 - 10] )

    table.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 1, colors.black),
                           ]))

    tableW, tableH = table.wrapOn(p, 0, 0)
    table.drawOn(p, 15, height - 200 - tableH)
    p.showPage()
    p.save()
    return response
    

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
    try:
        fiche = Fiche.objects.get(idfiche = idfiche)
    except ValueError:
        return errorPage(request, "Validation impossible")
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
