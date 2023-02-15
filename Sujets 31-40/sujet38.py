"""
On  considère  des  mots  à  trous  :  ce  sont  des  chaînes  de  caractères  contenant 
uniquement des majuscules et des caractères '*'. Par exemple 'INFO*MA*IQUE', 
'***I***E**' et '*S*' sont des mots à trous. 

Programmer une fonction correspond qui : 

 prend en paramètres deux chaînes de caractères mot et mot_a_trous où 

mot_a_trous est un mot à trous comme indiqué ci-dessus, 
renvoie : 

o  True si on peut obtenir mot en remplaçant convenablement les 

caractères '*' de mot_a_trous. 

o  False sinon. 
"""


def correspond(mot,mot_a_trou):
    if len(mot)!=len(mot_a_trou):
        return False
    for i in range(len(mot)):
        if mot[i]!=mot_a_trou[i] and mot_a_trou[i]!="*":
            return False
    return True
correspond('INFORMATIQUE', 'INFO*MA*IQUE')
