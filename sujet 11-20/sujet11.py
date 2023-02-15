"""
On modélise la représentation binaire d'un entier non signé par un tableau d'entiers dont 
les éléments sont 0 ou 1. Par exemple, le tableau [1, 0, 1, 0, 0, 1, 1] représente 
l'écriture binaire de l'entier dont l'écriture décimale est  

2**6 + 2**4 + 2**1 + 2**0 = 83. 

À  l'aide  d'un  parcours  séquentiel,  écrire  la  fonction  convertir  répondant  aux 
spécifications suivantes : 

def convertir(tab): 
tab est un tableau d'entiers, dont les éléments sont 0 ou 1, 
et représentant un entier écrit en binaire.  
Renvoie l'écriture décimale de l'entier positif dont la 
représentation binaire est donnée par le tableau tab 
"""


def convertir(tab):
    pui=len(tab)-1
    out=0
    for i in tab:
        if i==1:
            out=out+2**pui
        pui-=1
    return out
convertir([0,0,0,1,0])

            
