"""
Programmer une fonction renverse, prenant en paramètre une chaîne de caractères non vide, 
mot, et qui renvoie une chaîne de caractères en inversant ceux de la chaîne mot. 
"""
def renverse(mot):
    out = ''
    for e in mot:
        out = e + out
    return out
renverse("informatique")
