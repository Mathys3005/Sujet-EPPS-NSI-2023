"""
Dans cet exercice, l’opérateur ** et la fonction pow ne sont pas autorisés.  

Programmer en langage Python une fonction liste_puissances qui prend en argument 
un nombre entier a, un entier strictement positif n et qui renvoie la liste de ses puissances 
[a1, a2, ... , an ]. 

Programmer  également  une  fonction  liste_puisssances_borne  qui  prend  en 
argument un nombre entier a supérieur ou égal à 2 et un entier borne, et qui renvoie la 
liste de ses puissances, à l’exclusion de a0, strictement inférieures à borne. 
"""

def liste_puissances(a,n):
    out=[a]*n
    for i in range (1,n):
        out[i]*=out[i-1]
    return out
#liste_puissances(3,5)
def liste_puissances_borne(a,borne):
    n=a
    out=[]
    while n< borne:
        out.append(n)
        n*=a
    return out
liste_puissances_borne(5,5)
