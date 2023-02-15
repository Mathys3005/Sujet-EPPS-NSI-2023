"""
Écrire la fonction maxliste, prenant en paramètre un tableau non vide de nombres tab 
(de type list) et renvoyant le plus grand élément de ce tableau. 
"""

def max_liste(tab):
    max=tab[0]
    for i in tab:
        if i>max:
            max=i
    return max
max_liste([98, 12, 104, 23, 131, 9])
