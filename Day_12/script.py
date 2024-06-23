import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    return [list(line) for line in lines]

def combinaisons_points(chaine, nombre_de_parties):
    # Longueur de la chaîne
    longueur_chaine = len(chaine)

    # Utilisation de itertools.combinations pour générer les combinaisons
    combinaisons = combinations(range(1, longueur_chaine), nombre_de_parties - 1)

    liste = []

    # Affichage des résultats
    for index, combinaison in enumerate(combinaisons, 1):
        parties = [chaine[i:j] for i, j in zip((0,) + combinaison, combinaison + (None,))]
        liste.append(parties)
        #print(f'Possibilité {index}: {parties}')
    
    return liste

def fusionner_en_alternance(list1, list2):
    fusion = []
    min_len = min(len(list1), len(list2))

    for i in range(min_len):
        fusion.append(list1[i])
        fusion.append(list2[i])

    # Ajouter les éléments restants de la liste la plus longue
    # fusion.extend(list1[min_len:])
    # fusion.extend(list2[min_len:])

    return fusion

def fusionner_en_alternance_variable(list1, list2):
    fusion = []

    for i in range(len(list1)):
        fusion.append(list1[i])
        if i < len(list2):
            fusion.append(list2[i])

    # Ajouter les éléments restants de la liste la plus longue
    # fusion.extend(list1[len(list2):])
    # fusion.extend(list2[len(list1):])

    return fusion

def combi_point_diese(list_point, list_diese, pattern):
    # Combinaisons possibles des deux listes
    combinaisons_points = permutations(list_point)
    # supprimer les doublons
    combinaisons_points = list(set(combinaisons_points))
    #print('combinaisons_points', combinaisons_points)

    combinaisons_possibles = []
    for combinaison in combinaisons_points:
        if len(combinaison) == len(list_diese):
            combinaisons_possibles.append(''.join(fusionner_en_alternance(combinaison, list_diese)))
            combinaisons_possibles.append(''.join(fusionner_en_alternance(list_diese, combinaison)))
        elif len(combinaison) == len(list_diese) + 1:
            combinaisons_possibles.append(''.join(fusionner_en_alternance_variable(combinaison, list_diese)))
        elif len(combinaison) + 1 == len(list_diese):
            combinaisons_possibles.append(''.join(fusionner_en_alternance_variable(list_diese, combinaison)))
    #print('combinaisons_possibles', combinaisons_possibles)


    resultat = []
    for combinaison in combinaisons_possibles:
        if pattern.match(combinaison) and combinaison not in resultat:
            resultat.append(combinaison)

    # for combinaison in combinaisons_possibles:
    #     #string_combinaison = ''.join(combinaison)
    #     if all(combinaison[i][0] != combinaison[i+1][0] and pattern.match(string_combinaison) for i in range(len(combinaison)-1)):
    #         if [i for i in combinaison if i in list_diese] == list_diese and string_combinaison not in resultat:
    #             resultat.append(string_combinaison)
    return resultat

def trouver_combinaisons(n, nb_termes):
    combinaisons = list(combinations_with_replacement(range(1, n + 1), nb_termes))
    return [list(comb) for comb in combinaisons if sum(comb) == n]

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    nb_arrangements_tot = 0
    index = 0
    for line in lines:
        splitted_line = line.split(' ')
        #print('splitted_line', splitted_line)

        line = splitted_line[0]
        #print('longueur line', len(line))
        pattern = line.replace('?', '[.#]')
        pattern = pattern.replace('.', '\.')
        pattern = re.compile(pattern)

        pattern_diese = [int(i) for i in splitted_line[1].split(',') if i]
        #print('pattern_diese', pattern_diese)
        list_diese = ['#'*i for i in pattern_diese]
        #print('list_diese', list_diese)
        nb_point = len(line) - sum(pattern_diese)
        #print('nb_point', nb_point)

        
        arrangements = []
        for i in range(len(list_diese)-1, len(list_diese)+2):
            list_combinaisons_points = trouver_combinaisons(nb_point, i)
            for combi in list_combinaisons_points:
                arrangements += combi_point_diese(['.'*i for i in combi], list_diese, pattern)
                arrangements = list(set(arrangements))
        
        #print('combinaisons_points', list_combinaisons_points)
        print('longueur combinaisons_points', len(list_combinaisons_points))
        
        
        #arrangements = list(set(arrangements))
        #print('arrangements', arrangements)
        #print('taille arrangement', len(arrangements))
        nb_arrangements_tot += len(arrangements)
        index += 1
        print(f'index {index} done, nb_arrangements de la ligne : {len(arrangements)}')

    print('nb_arrangements_tot', nb_arrangements_tot)





    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   