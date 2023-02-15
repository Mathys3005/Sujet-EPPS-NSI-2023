"""
Écrire  une  fonction  recherche  qui  prend  en  paramètres  elt  un  nombre  et  tab  un 
tableau de nombres, et qui renvoie l’indice de la dernière occurrence de elt dans tab si 
elt est dans tab et renvoie -1 sinon. 
"""

def recherche(elt,tab):
    ind=-1
    for i in range(len(tab)):
        if tab[i]==elt:
            ind=i
    return ind
recherche(1, [8, 1, 10, 1, 7, 1, 8])
