"""
Écrire  une  fonction  recherche_min  qui  prend  en  paramètre  un  tableau,  non  vide,  de 
nombres non trié tab, et qui renvoie l'indice de la première occurrence du minimum de 
ce tableau. Les tableaux seront représentés sous forme de listes Python. 
"""
def recherche_min(tab):
    min=tab[0]
    ind=0
    for i in range(len(tab)):
        if tab[i]<min:
            min=tab[i]
            ind=i
    return ind
recherche_min([5, 3, 2, 2, 4])

