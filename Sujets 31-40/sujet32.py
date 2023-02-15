"""
Écrire une fonction min_et_max qui prend en paramètre un tableau de nombres tab non 
vide,  et  qui  renvoie  la  plus  petite  et  la  plus  grande  valeur du  tableau  sous  la  forme  d’un 
dictionnaire à deux clés 'min' et 'max'. 

Les tableaux seront représentés sous forme de liste Python. 

L’utilisation des fonctions natives min, max et sorted, ainsi que la méthode sort n’est pas 
autorisée. 

Ne  pas  oublier  d’ajouter  au  corps  de  la  fonction  une  documentation  et  une  ou  plusieurs 
assertions pour vérifier les pré-conditions. 
"""

def min_et_max(tab):
    d={}
    d['min']=tab[0]
    d['max']=tab[0]
    for e in tab:
        if e > d['max']:
            d['max']=e
        if e < d['min']:
            d['min']=e
    return d
min_et_max([-1, -1, -1, -1, -1])
        
