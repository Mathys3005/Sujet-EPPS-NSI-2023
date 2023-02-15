"""Écrire une fonction max_et_indice qui prend en paramètre une liste non vide tab de 
nombres  entiers et  qui renvoie  la  valeur du  plus  grand  élément de  cette  liste  ainsi  que 
l’indice de sa première apparition dans cette liste. 

L’utilisation de la fonction native max n’est pas autorisée. 

Ne pas oublier d’ajouter au corps de la fonction une documentation et une ou plusieurs 
assertions pour vérifier les pré-conditions. 
"""


def max_et_indice(tab):
    max=tab[0]
    ind=0
    assert tab!=[],"la liste ne doit pas etre vide"
    for i in range(len(tab)):
        if tab[i]>max:
            max=tab[i]
            ind=i
    return (max,ind)
max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
