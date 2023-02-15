"""

Sur  le  réseau  social  TipTop,  on  s’intéresse  au  nombre  de  « like »  des  abonnés.  
Les données sont stockées dans des dictionnaires où les clés sont les pseudos et les valeurs 
correspondantes sont les nombres de « like » comme ci-dessous : 

{'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50} 

Écrire une fonction max_dico qui : 
 prend en paramètre un dictionnaire dico non vide dont les clés sont des chaînes de 

caractères et les valeurs associées sont des entiers positifs ou nuls ; 
renvoie un tuple dont : 

la première valeur est une clé du dictionnaire associée à la valeur maximale ; 
la seconde valeur est la valeur maximale présente dans le dictionnaire. 
"""



def max_dico(dico):
    max=0
    cle=""
    for e in dico:
        if dico[e]>max:
            max=dico[e]   #cle[e]= valeurs de la clé et cle c'est le nom de la clé donc le prénom ici
            cle=e
    return (cle,max)
max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50})

