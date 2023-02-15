"""
Écrire  une  fonction  recherche  qui  prend  en  paramètres  un  tableau  tab  de  nombres 
entiers  triés  par  ordre  croissant  et  un  nombre  entier  n,  et  qui  effectue  une  recherche 
dichotomique du nombre entier n dans le tableau non vide tab.  

Cette fonction doit renvoyer un indice correspondant au nombre cherché s’il est dans le 
tableau, -1 sinon. 
"""
def recherche(tab,n):
    debut=0
    fin=len(tab)-1
    while debut<=fin:
        m=(debut+fin)//2
        if n>tab[m]:
            debut=m+1
        elif n<tab[m]:
            fin=m-1
        elif n==tab[m]:
            return m
    return -1
recherche([2, 3, 4, 6, 7], 5)
