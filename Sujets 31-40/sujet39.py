"""
On s’intéresse à la suite d’entiers définie par : 

les deux premiers termes sont égaux à 1, 
  ensuite,  chaque  terme  est  obtenu  en  faisant  la  somme  des  deux  termes  qui  le 

précèdent. 

En mathématiques, on le formule ainsi : 

u1 = 1, u2 = 1 et, pour tout entier naturel non nul n,  un+2 = un+1 + un. 

Cette suite est connue sous le nom de suite de Fibonacci. 
Écrire en Python une fonction fibonacci qui prend en paramètre un entier n supposé 
strictement positif et qui renvoie le terme d’indice n de cette suite. 

"""

def fibonacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fibonacci(25)
