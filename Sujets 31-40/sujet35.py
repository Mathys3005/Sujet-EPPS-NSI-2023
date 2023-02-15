"""
L'opérateur « ou exclusif » entre deux bits renvoie 0 si les deux bits sont égaux et 1 s'ils 
sont différents. Il est symbolisé par le caractère ⊕. 
Ainsi : 

  0 ⊕ 0 = 0  
  0 ⊕ 1 = 1 
  1 ⊕ 0 = 1 
  1 ⊕ 1 = 0 

On représente ici une suite de bits par un tableau contenant des 0 et des 1. 

Écrire  la  fonction  ou_exclusif  qui  prend  en  paramètres  deux  tableaux  de  même 
longueur  et  qui  renvoie  un  tableau  où  l’élément  situé  à  position  i  est  le  résultat,  par 
l’opérateur  « ou  exclusif »,  des  éléments  à  la  position  i  des  tableaux  passés  en 
paramètres.  
"""

def ou_exclusif(tab1,tab2):
    assert len(tab1)==len(tab2),"tableau de longueur différente"
    out=[]
    taille=len(tab1)
    for i in range(taille):
        if tab1[i]==0 and tab2[i]==1:
            out.append(1)
        elif tab1[i]==0 and tab2[i]==0:
            out.append(0)
        elif tab1[i]==1 and tab2[i]==0:
            out.append(1)
        elif tab1[i]==1 and tab2[i]==1:
            out.append(0)
    return out
a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

ou_exclusif(a,b)
    
