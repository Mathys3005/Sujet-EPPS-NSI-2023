"""
Écrire une fonction indices_maxi qui prend en paramètre une liste tab, non vide, de 
nombres entiers et renvoie un couple donnant d’une part le plus grand élément de cette 
liste et d’autre part la liste des indices de la liste tab où apparaît ce plus grand élément. 
"""
def indices_maxi(tab):
    out=[]
    max=tab[0]
    for i in range(len(tab)):
        if tab[i]>max:
            max=tab[i]
    for j in range (len(tab)):
        if tab[j]==max:
            out.append(j)
    return(max,out)
        
            
    
    return (max,out)
indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) 
