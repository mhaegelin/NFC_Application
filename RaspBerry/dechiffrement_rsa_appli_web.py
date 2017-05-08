def decoder(uid_crypted, d, n):
	compteur = 0
	msg = []
	while compteur < len(uid_crypted) : #On decode le code ASCII de chaque lettre
		ascii = (pow(uid_crypted[compteur],d)%n)
		msg.append(chr(ascii)) # Avec la fn chr(ASCII), on trouve le caractere correspondant
		compteur = compteur + 1
	return "".join(msg);

d= 713
n= 1073
uid_crypted = [373,427,142,451,500,126,869,500] #exemple correspondant a la trace NFC de Marc
uid_uncrypted = decoder(uid_crypted, d, n)

print uid_uncrypted
