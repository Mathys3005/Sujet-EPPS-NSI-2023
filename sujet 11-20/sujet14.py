"""
Écrire une fonction recherche qui prend en paramètres un nombre entier elt et un 
tableau tab de nombres entiers, et qui renvoie l’indice de la première occurrence de 
elt dans tab si elt est dans tab et -1 sinon. 

Ne pas oublier d’ajouter au corps de la fonction une documentation et une ou plusieurs 
assertions pour vérifier les pré-conditions. 
"""

def recherche(elt,tab):
    assert tab != [], "le tableau est vide"
    for i in range(len(tab)):
        if tab[i]==elt:
            return i
    return -1
recherche(15, [8, 9, 10, 15])
