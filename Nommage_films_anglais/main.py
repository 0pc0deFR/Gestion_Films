import rename_film
import directory
import sys
import os

if(len(sys.argv)) > 1:
	dossier = sys.argv[1]
	list_films = directory.arborescence(dossier)
	for titre in list_films:
		new_titre = rename_film.search(titre[0:-4])
		if(new_titre != "ERROR"):
			os.chdir(list_films[titre])
			print "Ancien nom: %s, nouveau nom: %s" % (titre[0:-4], new_titre)
			os.rename(titre, new_titre.replace('\r\n', '').replace('\r', '').replace('\n', '').replace(':', '').replace('\\', '').replace('/', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '') + titre[len(titre)-4:])
	print "Le programme s'est fini avec succes"
else:
	print "Preciser un dossier"