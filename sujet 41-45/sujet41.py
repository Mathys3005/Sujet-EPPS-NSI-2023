"""
Écrire une fonction recherche(caractere, chaine) qui prend en paramètres 
caractere, un unique caractère (c’est-à-dire une chaîne de caractère de longueur 1), 
et chaine, une chaîne de caractères. Cette fonction renvoie le nombre d’occurrences 
de caractere dans chaine, c’est-à-dire le nombre de fois où caractere apparaît 
dans chaine. 
"""

def recherche(caractere,chaine):
    cpt=0
    for e in chaine:
        if e==caractere:
            cpt+=1
    return cpt
recherche('i',"mississippi")
