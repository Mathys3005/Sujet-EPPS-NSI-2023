"""
Écrire  une  fonction  moyenne  qui  prend  en  paramètre  un  tableau  non  vide  de  nombres 
flottants  et  qui  renvoie  la  moyenne  des  valeurs  du  tableau.  Les  tableaux  seront 
représentés sous forme de liste Python. 
"""

def moyenne(tab):
    somme=0
    for e in tab:
        somme+=e
    return somme/len(tab)
moyenne([1.0, 2.0, 4.0])
