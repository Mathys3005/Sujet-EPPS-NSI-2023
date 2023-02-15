"""
Pour cet exercice : 

  On appelle « mot » une chaîne de caractères composée de caractères choisis 

parmi les 26 lettres minuscules ou majuscules de l'alphabet, 

  On appelle « phrase » une chaîne de caractères : 

o  composée d’un ou de plusieurs « mots » séparés entre eux par un seul 

caractère espace ' ', 

o  se finissant : 

  soit par un point '.' qui est alors collé au dernier mot,  
  soit par un point d'exclamation '!' ou d'interrogation '?' qui est 
alors séparé du dernier mot par un seul caractère espace ' '. 

Voici deux exemples de phrases : 

  'Cet exercice est simple.' 
  'Le point d exclamation est separe !' 

Après avoir remarqué le lien entre le nombre de mots et le nombres de caractères 
espace dans une phrase, programmer une fonction nombre_de_mots qui prend en 
paramètre une phrase et renvoie le nombre de mots présents dans celle-ci. 

"""

def nombre_de_mots(phrase):
    out=0
    for e in phrase:
        if e==" " or e==".":
            out+=1
    return out
nombre_de_mots('Fin.')
