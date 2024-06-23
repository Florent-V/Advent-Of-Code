import sys
from itertools import combinations
import time

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    return [list(line) for line in lines]

def part_1(matrice):
    indices_lignes_zero = [i for i, ligne in enumerate(matrice) if all(element == '.' for element in ligne)]
    indices_colonnes_zero = [j for j in range(len(matrice[0])) if all(matrice[i][j] == '.' for i in range(len(matrice)))]
    indices_lignes_zero.reverse()
    for i in indices_lignes_zero:
        matrice.insert(i, ['.']*len(matrice[i]))
    indices_colonnes_zero.reverse()
    for ligne in matrice:
        for i in indices_colonnes_zero:
            ligne.insert(i, '.')
    # for i in matrice:
    #     print(i)

    galaxies = []
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == '#':
                galaxies.append((i, j))
    #print(galaxies)
    paires_possibles = list(combinations(galaxies, 2))
    print(paires_possibles)
    print(len(paires_possibles))
    total_distance = 0
    for paire in paires_possibles:
        total_distance += abs(paire[0][0] - paire[1][0]) + abs(paire[0][1] - paire[1][1])
    print('total_distance', total_distance)

def part_2(matrice):
    galaxies = []
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == '#':
                galaxies.append((i, j))
    for i in galaxies:
        print(i)

    indices_lignes_zero = [i for i, ligne in enumerate(matrice) if all(element == '.' for element in ligne)]
    indices_colonnes_zero = [j for j in range(len(matrice[0])) if all(matrice[i][j] == '.' for i in range(len(matrice)))]

    print('indices_lignes_zero', indices_lignes_zero)
    print('indices_colonnes_zero', indices_colonnes_zero)

    # for i, coord in enumerate(galaxies):
    #   for j, palier in enumerate(indices_lignes_zero):
    #       if coord[0] >= palier:
    #           # Ajouter la valeur correspondante au palier
    #           galaxies[i] = (coord[0] + (j + 1) * 1000000, coord[1])
    #           break  # Sortir de la boucle dès qu'un palier est atteint
    for i, coord in enumerate(galaxies):
      for j, palier in enumerate(indices_lignes_zero):
          if coord[0] >= palier:
              # Ajouter la valeur correspondante au palier
              galaxies[i] = (coord[0] + (j + 1) * 999999, coord[1])
          else:
              # Si coord[0] < palier, ne rien ajouter et sortir de la boucle
              break
      # else:
      #     # Cette partie est exécutée si la boucle interne n'est pas interrompue (tous les paliers ont été vérifiés)
      #     print('coucou1')
      #     galaxies[i] = (coord[0] + len(indices_lignes_zero) * 1000000, coord[1])
      
    print('galaxies')
    for i in galaxies:
        print(i)

    for i, coord in enumerate(galaxies):
      for j, palier in enumerate(indices_colonnes_zero):
          if coord[1] >= palier:
              # Ajouter la valeur correspondante au palier
              galaxies[i] = (coord[0], coord[1] + (j + 1) * 999999)
          else:
              # Si coord[0] < palier, ne rien ajouter et sortir de la boucle
              break
    #   else:
    #       # Cette partie est exécutée si la boucle interne n'est pas interrompue (tous les paliers ont été vérifiés)
    #       print('coucou2')
    #       galaxies[i] = (coord[0] + len(indices_lignes_zero) * 1000000, coord[1])

    print('galaxies')
    for i in galaxies:
        print(i)
  
    
    paires_possibles = list(combinations(galaxies, 2))
    print(paires_possibles)
    print(len(paires_possibles))
    total_distance = 0
    for paire in paires_possibles:
        total_distance += abs(paire[0][0] - paire[1][0]) + abs(paire[0][1] - paire[1][1])
    print('total_distance', total_distance)

    

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    matrice = format_data(lines)
    print('matrice', matrice)
    for i in matrice:
        print(i)
    #part_1(matrice)
    matrice = format_data(lines)
    part_2(matrice)





    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   