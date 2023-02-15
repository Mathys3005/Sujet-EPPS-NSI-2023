"""
Écrire une fonction a_doublon qui prend en paramètre une liste triée de nombres et renvoie True si la liste 
contient au moins deux nombres identiques, False sinon.
"""

def a_doublon(liste):
    liste.sort()
    for i in range(1,len(liste)):
        if liste[i]==liste[i-1]:
            return True
    return False
#a_doublon([1]) 
a_doublon([1, 2, 4, 6, 6])
