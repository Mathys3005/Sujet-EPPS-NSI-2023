"""

On considère des tables (des tableaux de dictionnaires) qui contiennent des 
enregistrements relatifs à des animaux hébergés dans un refuge. Les attributs des 
enregistrements sont 'nom', 'espece', 'age', 'enclos'. Voici un exemple 
d'une telle table : 

animaux = [ {'nom':'Medor',  'espece':'chien', 'age':5, 'enclos':2}, 
            {'nom':'Titine', 'espece':'chat',  'age':2, 'enclos':5}, 
            {'nom':'Tom',    'espece':'chat',  'age':7, 'enclos':4}, 
            {'nom':'Belle',  'espece':'chien', 'age':6, 'enclos':3}, 
            {'nom':'Mirza',  'espece':'chat',  'age':6, 'enclos':5}] 

Programmer une fonction selection_enclos qui prend en paramètres : 

o  une table table_animaux contenant des enregistrements relatifs à 

des animaux (comme dans l'exemple ci-dessus), 

o  un numéro d'enclos num_enclos ; 
renvoie une table contenant les enregistrements de table_animaux dont 
l'attribut 'enclos' est num_enclos. 
"""

def selection_enclos(table_animaux,num_enclos):
    out=[]
    for i in table_animaux:
        if i['enclos']==num_enclos:
            out.append(i)
    return out

animaux = [ {'nom':'Medor',  'espece':'chien', 'age':5, 'enclos':2}, 
            {'nom':'Titine', 'espece':'chat',  'age':2, 'enclos':5}, 
            {'nom':'Tom',    'espece':'chat',  'age':7, 'enclos':4}, 
            {'nom':'Belle',  'espece':'chien', 'age':6, 'enclos':3}, 
            {'nom':'Mirza',  'espece':'chat',  'age':6, 'enclos':5}] 

selection_enclos(animaux, 7)
