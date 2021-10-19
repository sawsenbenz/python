tuple_var = (14,4)

def somme2(t):
    # Crée la variable de résultat toujours out de
    # ta boucle et l'initialiser
    result = 0
    for item in t:
        result = result + item
    # le retour d'une fonction ne peut etre mit dans une boucle
    return result

print(somme2(tuple_var))



