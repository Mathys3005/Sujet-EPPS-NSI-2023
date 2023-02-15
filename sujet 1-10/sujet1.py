
'''
Programmer la fonction verifie qui prend en paramètre un tableau de valeurs 
numériques non vide et qui renvoie True si ce tableau est trié dans l’ordre croissant, 
False sinon.
'''

def verifie(liste):
    for i in range (1,len(liste)):
        if liste[i]<liste[i-1]:
            return False
    return True

            

verifie([8, 12, 4])
