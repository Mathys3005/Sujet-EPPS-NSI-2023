"""
Programmer la fonction moyenne prenant en paramètre un tableau d'entiers tab (de type 
list) qui renvoie la moyenne de ses éléments si le tableau est non vide. Proposer une 
façon de traiter le cas où le tableau passé en paramètre est vide. 

Dans cet exercice, on s’interdira d’utiliser la fonction Python sum. 
"""

def moyenne(tab):
    assert tab!=[],"Tableau vide"
    somme=0
    for e in tab:
        somme+=e
    return somme/len(tab)
moyenne([1,2,3,4,5,6,7,8,9,10])
