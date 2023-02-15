"""
Écrire une fonction moyenne(liste_notes) qui renvoie la moyenne pondérée des 
résultats contenus dans la liste liste_notes, non vide, donnée en paramètre. Cette 
liste contient des couples (note, coefficient) dans lesquels : 

  note est un nombre de type float compris entre 0 et 20 ; 
  coefficient est un nombre entier strictement positif. 

Ainsi, l’expression moyenne([(15, 2), (9, 1), (12, 3)]) devra renvoyer 
12.5 : 
"""

def moyenne(liste_notes):
    c=0
    somme=0
    for (note,coef) in liste_notes:
        somme+=note*coef
        c+=coef
    out=somme/c
    return out

moyenne([(15,2),(9,1),(12,3)])
    
