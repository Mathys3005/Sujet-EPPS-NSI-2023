"""
Écrire une fonction moyenne renvoyant la moyenne pondérée d’une liste non vide, 
passée en paramètre, de tuples à deux éléments de la forme (valeur, 
coefficient) où valeur et coefficient sont des nombres positifs ou nuls.  
Si la somme des coefficients est nulle, la fonction renvoie None, si la somme des 
coefficients est non nulle, la fonction renvoie, sous forme de flottant, la moyenne des 
valeurs affectées de leur coefficient.
"""


def moyenne(liste):
    coef=0
    somme=0
    for (n,c) in liste:
        somme+=n*c
        coef+=c
    if coef==0:
        return None
    return somme/coef
moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
#moyenne([(3, 0), (5, 0)])        
