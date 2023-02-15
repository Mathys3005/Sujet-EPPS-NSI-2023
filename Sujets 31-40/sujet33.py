"""
Un arbre binaire de caractères est stocké sous la forme d’un dictionnaire où les clés sont 
les caractères des nœuds de l’arbre et les valeurs, pour chaque clé, la liste des caractères 
des fils gauche et droit du nœud. 

Par exemple, l’arbre 

est stocké dans 

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \ 
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \ 
     'H':['','']} 

Écrire une fonction récursive taille prenant en paramètres un arbre binaire arbre 
sous la forme d’un dictionnaire et un caractère lettre qui est la valeur du sommet de 
l’arbre, et qui renvoie la taille de l’arbre, à savoir le nombre total de nœud. 

On observe que, par exemple, arbre[lettre][0], respectivement 
arbre[lettre][1], permet d’atteindre la clé du sous-arbre gauche, respectivement 
droit, de l’arbre arbre de sommet lettre.
"""


def taille(arbre,lettre):
    g=arbre[lettre][0]
    d=arbre[lettre][1]
    if g!="" and d != "":
        return 1+taille(arbre,g)+taille(arbre,d)
    elif g=="" and d!="":
        return 1+taille(arbre,d)
    elif g!="" and d=="":
        return 1+ taille(arbre,g)
    return 1
    
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 
     'H':['','']} 
taille(a,'F')
