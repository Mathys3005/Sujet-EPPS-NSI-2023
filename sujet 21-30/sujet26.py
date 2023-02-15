"""

Programmer la fonction multiplication, prenant en paramètres deux nombres entiers 
n1 et n2, et qui renvoie le produit de ces deux nombres.  

Les seules opérations autorisées sont l’addition et la soustraction.  

"""
def multiplication(n1,n2):
    if n1<0:
        return -multiplication(-n1,n2)
    if n2<0:
        return -multiplication(n1,-n2)
    res=0
    for i in range(n2):
        res+=n1
    return res
multiplication(-4, -8)
