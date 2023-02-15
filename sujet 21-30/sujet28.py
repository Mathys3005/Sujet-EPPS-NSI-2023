"""
Ecrire une fonction qui prend en paramètre un tableau d'entiers non vide et qui renvoie la 
moyenne de ces entiers. La fonction est spécifiée ci-après et doit passer les assertions 
fournies. 

def moyenne (tab): 
    ''' 
        moyenne(list) -> float 
        Entrée : un tableau non vide d'entiers 
        Sortie : nombre de type float  
        Correspondant à la moyenne des valeurs présentes dans le 
        tableau 
    '''   
"""

def moyenne(tab):
    cpt=0
    somme=0
    for e in tab:
        cpt+=1
        somme+=e
    return somme/cpt
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
