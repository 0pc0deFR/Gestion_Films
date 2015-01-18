import os

def arborescence(home):
	tab = {}
	for fichier in os.listdir(home):
		contenu = home + "\\" + fichier
		if os.path.isfile(contenu) == True:
			tab[fichier] = home
		elif os.path.isdir(contenu) == True:
			tab.update(arborescence(contenu))
	return tab