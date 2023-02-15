"""
Écrire en python deux fonctions : 

  lancer de paramètre n, un entier positif, qui renvoie un tableau de type list de 

n entiers obtenus aléatoirement entre 1 et 6 (1 et 6 inclus) ; 

  paire_6  de paramètre tab, un tableau de type list de n entiers entre 1 et 
6 obtenus aléatoirement, qui renvoie un booléen égal à True si le nombre de 6 
est supérieur ou égal à 2, False sinon. 

On pourra utiliser la fonction randint(a,b)du module random pour laquelle la 
documentation officielle est la suivante : 

Renvoie un entier aléatoire N tel que a <=N <= b. 
"""
from random import randint
def lancer(n):
    out=[]
    for i in range(n):
        out.append(randint(1,6))
    return out

def paire_6(tab):
    cpt=0
    for i in tab:
        if i==6:
            cpt+=1
    if cpt>2:
        return True
    return False

paire_6(lancer(15))
