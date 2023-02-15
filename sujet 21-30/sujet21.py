"""
Le codage par différence (delta encoding en anglais) permet de compresser un tableau 
de données en indiquant pour chaque donnée, sa différence avec la précédente (plutôt 
que la donnée elle-même). On se retrouve alors avec un tableau de données plus petit, 
nécessitant donc moins de place en mémoire. Cette méthode se révèle efficace lorsque 
les valeurs consécutives sont proches. 

Programmer la fonction delta(liste) qui prend en paramètre un tableau non vide de 
nombres entiers et qui renvoie un tableau contenant les valeurs entières compressées à 
l’aide de cette technique. 
"""


def delta (tab):
    out=[tab[0]]
    for i in range (1,len(tab)):
        out.append(tab[i]-tab[i-1])
    return out

delta([1000, 800, 802, 1000, 1003])
        
