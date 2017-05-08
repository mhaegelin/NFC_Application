# La fonction factoriser avec en argument n
def factoriser(n):
    b=2
    while b:
        while n%b!=0 :
            b=b+1
        if n/b==1 :
            print "p = ", b,
            # On cree une variable globale p pour la reutiliser hors de la fonction et p=b
            global p
            p = b
            break
        print "\nq = ", b,
        # On cree une variable globale q pour la reutiliser hors de la fonction et q=b
        global q
        q=b
        n=n/b;

# La fonction PGCD avec ses 2 arguments a et b
def pgcd(a,b):
    # L'algo PGCD
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a;

def recuperer_cle_publique():
	global n
	global e
	n = 1073 #cle publique
	e = 41 #ca peut etre recalcule, mais pas la peine car c'est dans la cle publique
	factoriser(n) # On recupere n, on appelle la fonction pour le factoriser.
	# On calcule phi(n)
	global phi_n	
	phi_n = (p-1)*(q-1)

def calculer_d():
	global d
	d = 0
	compteur = 0
	while compteur == 0:
		# Les conditions vues ci-dessus :
		if((e * d % phi_n == 1)and(p < d)and(q < d)and(d < phi_n)):
			compteur = 1
		d = d + 1
	d = d - 1

################################ DEBUT ###################################

## -- ETABLISSEMENT DE LA CLE PRIVEE -- ##
recuperer_cle_publique()
calculer_d()
print "\ncle privee (",d,",",n,")" # On affiche la cle privee

## -- EXEMPLE -- ##
"""
uid_crypted = [373,427,142,451,500,126,869,500] #correspond a la trace NFC de Marc

compteur = 0
msg = []
while compteur < len(uid_crypted) : #On decode le code ASCII de chaque lettre
	ascii = (pow(uid_crypted[compteur],d)%n)
	msg.append(chr(ascii)) # Avec la fn chr(ASCII), on trouve le caractere correspondant
	compteur = compteur + 1

uid_uncrypted= "".join(msg)
print uid_uncrypted"""
## ------------- ##
