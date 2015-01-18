import urllib

def html_head_delete(contenu):
	if(contenu.find('<table class="totalwidth noborder purehtml">') != -1):
		stop = contenu.find('<table class="totalwidth noborder purehtml">')
		contenu = contenu[stop:]
		return contenu
	else:
		return contenu

def html_parse(contenu):
	contenu = html_head_delete(contenu)
	if(contenu.find(")") < contenu.find("<br />")):
		return contenu[contenu.find("(")+1:contenu.find(")")]
	else:
		return "ERROR"

def search(film):
	url = "http://www.allocine.fr/recherche/?q="
	f = urllib.urlopen(url + film)
	contenu = f.read()
	return html_parse(contenu)