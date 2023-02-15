"""
Écrire  une  fonction  couples_consecutifs  qui  prend  en  paramètre  une  liste  de 
nombres entiers tab non vide, et qui renvoie la liste (éventuellement vide) des couples 
d'entiers consécutifs successifs qu'il peut y avoir dans tab. 

Ne pas oublier d’ajouter au corps de la fonction une documentation et une ou plusieurs 
assertions pour vérifier les pré-conditions.
"""

def couples_consecutifs(tab):
    out=[]
    for i in range(1,len(tab)):
        if tab[i-1]+1==tab[i]:
            out.append((tab[i-1],tab[i]))
    return out

couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7])
