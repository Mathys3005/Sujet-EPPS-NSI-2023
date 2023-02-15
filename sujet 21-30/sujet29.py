"""
Un arbre binaire est implémenté par la classe Arbre donnée ci-dessous. 
Les attributs fg et fd prennent pour valeurs des instances de la classe Arbre ou None. 

Écrire une fonction récursive taille prenant en paramètre une instance a de la classe 
Arbre et qui renvoie la taille de l’arbre que cette instance implémente. 

Écrire de même une fonction récursive hauteur prenant en paramètre une instance a 
de la classe Arbre et qui renvoie la hauteur de l’arbre que cette instance implémente. 

Si un arbre a un seul nœud, sa taille et sa hauteur sont égales à 1. 
S’il est vide, sa taille et sa hauteur sont égales à 0. 


a = Arbre(1)
a.fg = Arbre(4)
a.fd = Arbre(0)
a.fd.fd = Arbre(7)

"""


class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None
        
    
def taille(a):
    if a is None:
        return 0
    return 1 + taille(a.fg)+taille(a.fd)

def hauteur(a):
    if a is None:
        return 0
    else:
        return 1+max(hauteur(a.fg),hauteur(a.fd))

a = Arbre(1)
a.fg = Arbre(4)
a.fd = Arbre(0)
a.fd.fd = Arbre(7)

hauteur(a)
