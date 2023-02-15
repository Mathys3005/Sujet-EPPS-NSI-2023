"""
Écrire en langage Python une fonction recherche prenant comme paramètres une 
variable a de type numérique (float ou int) et un tableau tab (de type list) et qui 
renvoie le nombre d'occurrences de a dans tab. 
"""

def recherche (a,tab):
    cpt=0
    for i in tab:
        if i==a:
            cpt+=1
    return cpt
recherche(5, [-2, 5, 3, 5, 4, 5])
