# encoding: utf-8

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

	print "p ",p, "\nq ",q, "\nphi_n ",phi_n
	
def chiffrer_rsa(uid):
	taille_du_mot = len(uid)
	i = 0
	global uid_crypted	
	uid_crypted = []

	while i< taille_du_mot :
		ascii = ord(uid[i]) # On convertie chaque lettre de la trace NFC
		lettre_crypt = pow(ascii,e)%n # On chiffre la lettre ou plutôt son code ASCII
		 
		if ascii > n : # Si le code ASCII est supérieur à n
			print "Les nombres p et q sont trop petits veuillez recommencer."

		if lettre_crypt > phi_n : # Si le bloc chiffré est supérieur à phi(n)
			print "Erreur de calcul"
		uid_crypted.append(lettre_crypt)
		i = i + 1 # On incrémente i
################################ DEBUT ###################################

## -- ETABLISSEMENT DE LA CLE PUBLIQUE -- ##
creerPQ()
chercher_e(p, q, phi_n)
print "clé publique (",e,",",n,")"
## -------------------------------------- ##

uid= "AED06796" 
chiffrer_rsa(uid)

print uid_crypted

