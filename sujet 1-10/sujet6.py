"""
Programmer la fonction recherche, prenant en paramètre un tableau non vide tab (de 
type list) d'entiers et un entier n, et qui renvoie l'indice de la dernière occurrence de 
l'élément  cherché.  Si  l'élément  n'est  pas  présent,  la  fonction  renvoie  la  longueur  du 
tableau. 
"""
def recherche(tab,n):
    L=len(tab)
    for i in range(len(tab)):
        if tab[i]==n:
            L=i
    return L
            

        
            
        

recherche([2,3,5,2,4],2)
#recherche([2,4],2)
    
