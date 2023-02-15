"""
Écrire une fonction tri_selection qui prend en paramètre une liste tab de nombres 
entiers et qui renvoie la liste triée par ordre croissant. Il est demandé de ne pas créer de 
nouvelle liste mais de modifier celle fournie. 

On utilisera l’algorithme suivant : 
  on recherche le plus petit élément de la liste, en la parcourant du rang 0 au dernier 

rang, et on l'échange avec l'élément d'indice 0 ; 

  on recherche ensuite le plus petit élément de la liste restreinte du rang 1 au dernier 

rang, et on l'échange avec l'élément d'indice 1 ;  

  on continue de cette façon jusqu'à ce que la liste soit entièrement triée. 
"""

def  tri_selection(tab):
    for i in range(len(tab)):
        min=i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min=j
        tab[min], tab[i] = tab[i], tab[min]
    return tab
tri_selection([1, 52, 6, -9, 12])
