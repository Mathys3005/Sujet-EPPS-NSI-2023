"""
Écrire  une  fonction  python  appelée  nb_repetitions  qui  prend  en  paramètres  un 
élément elt et une liste tab et renvoie le nombre de fois où l’élément apparaît dans la 
liste.  
"""

def nb_repetitions(elt,tab):
    cpt=0
    for e in tab:
        if e==elt:
            cpt+=1
    return cpt
nb_repetitions(12, [1, '!', 7, 21, 36, 44])
