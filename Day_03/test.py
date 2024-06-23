import re

def est_symbole(caractere):
    return caractere in {'*', '#', '+', '$'}

def somme_numeros_accoles(schema):
    lignes = schema.split('\n')
    numeros_accoles = []

    for i in range(len(lignes)):
        numeros = re.findall(r'\d+', lignes[i])
        for numero in numeros:
            if any(est_symbole(lignes[i][j]) for j in range(len(lignes[i]))) or (
                    i > 0 and any(est_symbole(lignes[i - 1][j]) for j in range(len(lignes[i - 1]))) and any(
                        est_symbole(lignes[i][j]) for j in range(len(lignes[i]))) or
                    i < len(lignes) - 1 and any(est_symbole(lignes[i + 1][j]) for j in range(len(lignes[i + 1]))) and any(
                        est_symbole(lignes[i][j]) for j in range(len(lignes[i])))
            ):
                numeros_accoles.append(int(numero))

    return sum(numeros_accoles)

# Votre schéma de moteur
schema_moteur = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# Calculer la somme des numéros accolés
somme_resultat = somme_numeros_accoles(schema_moteur)

# Afficher le résultat
print("La somme des numéros accolés est :", somme_resultat)