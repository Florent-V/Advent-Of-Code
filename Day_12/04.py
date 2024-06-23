from itertools import combinations_with_replacement

def trouver_combinaisons(n, nb_termes):
    combinaisons = list(combinations_with_replacement(range(1, n + 1), nb_termes))
    return [list(comb) for comb in combinaisons if sum(comb) == n]

# Exemple d'utilisation pour obtenir toutes les combinaisons pour former 9 avec 5 termes
resultat = trouver_combinaisons(13, 7)

# Affichage des résultats
for combinaison in resultat:
    print(combinaison)

print(len(resultat))