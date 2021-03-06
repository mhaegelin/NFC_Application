# encoding: utf-8

import nxppy
import urllib2
import time
from urllib import urlencode
import requests
from bs4 import BeautifulSoup

## -- fonctions -- ##
# La fonction PGCD avec ses 2 arguments a et b
def pgcd(a,b):
    # L'algo PGCD
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a;

def chercher_e(p, q, phi_n):
	# Variables de la boucle
	compteur = 0
	PGCD1 = 0
	global e
	e = q  #notre e qui s'incrémentera
	# Tant que PGCD de e et phi(n) différents de 1
	while PGCD1 != 1 :
		# Si p inférieur à e et si q inférieur à e et si e inférieur à n
		if(e > phi_n) : 
			# La boucle se coupe 
			print "e non trouvé"
			break    
		# Tant que rien n'est trouvé, e s'incrémente
		e = e + 1
		
		# On récupère le résultat du pgcd    
		PGCD1 = pgcd(e,phi_n)

def creerPQ():
	global p
	global q
	global n
	global phi_n
	p=29
	q=37
	n= p*q
	phi_n= (p-1)*(q-1)

	print "Choix de p : ",p, "\nChoix de q : ",q, "\nphi_n : ",phi_n
	
def chiffrer_rsa(uid):
	taille_du_mot = len(uid)
	i = 0
	global uid_crypted	
	tab = []

	while i< taille_du_mot :
		ascii = ord(uid[i]) # On convertie chaque lettre de la trace NFC
		lettre_crypt = pow(ascii,e)%n # On chiffre la lettre ou plutôt son code ASCII
		 
		if ascii > n : # Si le code ASCII est supérieur à n
			print "Les nombres p et q sont trop petits veuillez recommencer."

		if lettre_crypt > phi_n : # Si le bloc chiffré est supérieur à phi(n)
			print "Erreur de calcul"
		tab.append(str(lettre_crypt))
		i = i + 1 # On incrémente i
	uid_crypted= ','.join(tab)
#####################

## -- debut -- ##

fichier = open("adressIPserver.txt", "r")
url= fichier.read()
#url= "http://109.15.75.65/Appli/trace"
fichier.close()
temps=0
ancien_uid= "petitTasDeMerde"

## -- ETABLISSEMENT DE LA CLE PUBLIQUE -- ##
print "Génération de la clé publique..."
creerPQ()
chercher_e(p, q, phi_n)
print "Clé publique (",e,",",n,")\n"
## -------------------------------------- ##

client = requests.session()
# Retrieve the CSRF token
print "Récupération du token de l'application eLog"
soup = BeautifulSoup(client.get(url).content, "lxml")
csrftoken = soup.find('input', {"name": "csrfmiddlewaretoken"}).get("value")
debug=0

mifare=nxppy.Mifare()
try:
	print "Pret pour lecture"
	
	inDebug = raw_input('Lecture silencieuse des cartes ? (O/n) : ')
	if inDebug:
		if ((debug=="n")or(debug=="N")):
			debug=1
		else:
			debug=0
	else:
		debug=0

	while True:
		try:
			uid= mifare.select()
        		if (uid != ancien_uid) or ((time.time() - temps) >3):
				ancien_uid= uid
				temps= time.time()
				
				chiffrer_rsa(uid) #la version cryptée se trouve mtn dans la var globale uid_crypted
				
				params = dict(traceNFC=uid_crypted, csrfmiddlewaretoken=csrftoken)
				r = client.post(url, data=params, headers=dict(Referer=url))

				if debug==1:
                                        print "Read UID : ", uid,"\nUID cryptée : ",uid_crypted

				#enregistrement dans le log
                                t= time.localtime(temps)
                                timelog= time.strftime("[%d.%m.%Y at %H:%M] ", t)
                                with open("card_log.txt", "a") as logFile:
                                        logFile.write(timelog+uid_crypted+"\n")

				"""methode post classique
				params = {'pseudo': uid}
				http_params = urlencode(params)

				req= urllib2.Request(url, http_params)
				connection = urllib2.urlopen(req)"""

		except nxppy.SelectError:
        		pass
	 	time.sleep(0.2)   
except KeyboardInterrupt:
        pass
