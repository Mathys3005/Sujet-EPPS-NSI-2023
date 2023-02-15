"""
Écrire une fonction recherche_indices_classement qui prend en paramètres un 
entier elt et une liste d’entiers tab, et qui renvoie trois listes : 

la première liste contient les indices des valeurs de la liste tab strictement 
inférieures à elt ;  
la deuxième liste contient les indices des valeurs de la liste tab égales à elt ; 
la troisième liste contient les indices des valeurs de la liste tab strictement 
supérieures à elt. 
"""
def recherche_indices_classement(elt,tab):
    out1=[]
    out2=[]
    out3=[]
    for i in range(len(tab)):
        if tab[i]==elt:
            out2.append(i)
        elif tab[i]>elt:
            out3.append(i)
        else:
            out1.append(i)
    return(out1,out2,out3)
recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0])
