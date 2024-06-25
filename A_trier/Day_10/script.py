import sys
from itertools import cycle
import math
import time

moves_coordinates = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'O': (0, -1)}
possibles_moves = {
    'E': {'-' : 'E',
          'J' : 'EN',
          '7' : 'ES'
          },
    'O': {'-' : 'O',
          'L' : 'ON',
          'F' : 'OS'
          },
    'S': {'|' : 'S',
          'L' : 'SE',
          'J' : 'SO'
          },
    'N': {'|' : 'N',
          'F' : 'NE',
          '7' : 'NO'
          }
}

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    for i in range(len(lines)):
        lines[i] = [int(i) for i in lines[i].split()]
    return lines


def find_starting_point(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                return (i, j)

def set_matrice_value(matrice, position, value):
    matrice[position[0]][position[1]] = value
    return matrice


def find_possible_starting_ways(position, pipe_map):
    possible_ways = []
    print('start_position', position)
    for move in possibles_moves:
        # Addition des coordonnées
        #print('possible move', move)
        new_position = tuple(a + b for a, b in zip(position, moves_coordinates[move]))
        new_pipe = pipe_map[new_position[0]][new_position[1]]
        if new_pipe in possibles_moves[move]:
            possible_ways.append({'dir': possibles_moves[move][new_pipe][-1], 'position': new_position})
                                  
        #print('new_posiible_position', new_position)
        #print('pipe', pipe_map[new_position[0]][new_position[1]])
    #print('possible_ways', possible_ways)
    return possible_ways
        
        
def run_through_pipe(pipe_map, matrice, position):
    ways = find_possible_starting_ways(position, pipe_map)
    for way in ways:
        matrice = set_matrice_value(matrice, way['position'], 1)
    print('ways', ways)
    flag = True
    index = 1
    while flag:
        index += 1
        for way in ways:
            #print('origine', way['position'])
            #print('direction', way['dir'])
            new_position = tuple(a + b for a, b in zip(way['position'], moves_coordinates[way['dir']]))
            if all(0 <= coord < 140 for coord in new_position):
              #print("Les coordonnées additionnées sont :", new_position)
              way['position'] = new_position
              matrice = set_matrice_value(matrice, way['position'], index)
            else:
              print("Les coordonnées ne respectent pas la plage spécifiée.")
            new_pipe = pipe_map[new_position[0]][new_position[1]]
            #print('new_pipe', new_pipe)
            way['dir']= possibles_moves[way['dir']][new_pipe][-1]
            #print('way', way)
        if ways[0]['position'] == ways[1]['position']:
            flag = False
            print('ways', ways)
            print('index', index)
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] != '.':
                matrice[i][j] = 'X'
    return matrice



    

   

def part_1(pipe_map):
    position = find_starting_point(pipe_map)
    print('start_point', position)
    print('nombre lignes', len(pipe_map))
    print('nombre colonnes', len(pipe_map[0]))
    matrice = [['.' for i in range(len(pipe_map))] for j in range(len(pipe_map))]
    matrice = set_matrice_value(matrice, position, 0)
    matrice = run_through_pipe(pipe_map, matrice, position)
    #print('matrice', matrice)
    return matrice
    

def part_2(pipe_map, matrice):
    print('matrice')
    for line in matrice:
        print(''.join([str(element) for element in line]))

    print('\n')
    print('pipe_map')
    for line in pipe_map:
        print(''.join([str(element) for element in line]))

    print('\n') 

    pipe_map_matrice = []
    for line in pipe_map:
        pipe_map_matrice.append([element for element in line])

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 'X':
                pipe_map_matrice[i][j] = 'X'
  
    nbX = 0
    for line in pipe_map_matrice:
        for element in line:
            if element == 'X':
                nbX += 1
    print('nbX', nbX)

    print('pipe_map_matrice')
    for line in pipe_map_matrice:
        print(''.join([str(element) for element in line]))
    
    point_position = []
    for i in range(len(pipe_map_matrice)):
        if i == 0 or i == len(pipe_map_matrice) - 1:
            for j in range(len(pipe_map_matrice[i])):
                if pipe_map_matrice[i][j] != 'X':
                    pipe_map_matrice[i][j] = 'O'
                    point_position.append((i, j))
        else :
            if pipe_map_matrice[i][0] != 'X':
                    pipe_map_matrice[i][0] = 'O'
                    point_position.append((i, 0))
            if pipe_map_matrice[i][-1] != 'X':
                    pipe_map_matrice[i][-1] = 'O'
                    point_position.append((i, len(pipe_map_matrice[i]) - 1))
    print('\n')
    print('pipe_map_matrice')
    for line in pipe_map_matrice:
        print(''.join([str(element) for element in line]))
    print('nb_invalid_points initial', len(point_position))
    flag = True
    while flag:
        nb_invalid_points = len(point_position)
        all_neighbors = []
        for point in point_position:
            neighbors = get_neighbors(pipe_map_matrice, point[0], point[1])
            # Fusion des deux listes sans doublons
            ensemble_coordonnees = set(neighbors + all_neighbors)
            # Conversion de l'ensemble en liste (si nécessaire)
            all_neighbors = list(ensemble_coordonnees)
        # Fusion des deux listes sans doublons
        ensemble_coordonnees = set(all_neighbors + point_position)
        # Conversion de l'ensemble en liste (si nécessaire)
        point_position = list(ensemble_coordonnees)
        print('point_position', len(point_position))
        if len(point_position) == nb_invalid_points:
            flag = False
    for point in point_position:
        pipe_map_matrice[point[0]][point[1]] = 'O'
    print('\n')
    print('pipe_map_matrice')
    for line in pipe_map_matrice:
        print(''.join([str(element) for element in line]))
    #compter les points restant dans la matrice
    nb_points = 0
    for line in pipe_map_matrice:
        trap = False
        for element in line:
            if element != 'X' and element != 'O' and trap:
                nb_points += 1
            if element == 'X':
                trap = not trap
    print('nb_points', nb_points)
    nb_points = 0
    for i in range(35,35+70,1):
        for j in range(35,37+70,1):
            if pipe_map_matrice[i][j] != 'X' and pipe_map_matrice[i][j] != 'O':
                nb_points += 1
    print('nb_points', nb_points)

    print('\n')

    pipe_map_matrice_2 = []
    for line in pipe_map:
        pipe_map_matrice_2.append([element for element in line])

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 'X':
                continue
            if pipe_map_matrice[i][j] == 'O':
                pipe_map_matrice_2[i][j] = 'O'
            else:
                pipe_map_matrice_2[i][j] = 'I'

            
    print('pipe_map_matrice_2')
    for line in pipe_map_matrice_2:
        print(''.join([str(element) for element in line]))

    possible_inside_point = []
    for i in range(len(pipe_map_matrice_2)):
        for j in range(len(pipe_map_matrice_2[i])):
            if pipe_map_matrice_2[i][j] == 'I':
                possible_inside_point.append((i, j))
    print('possible_inside_point', len(possible_inside_point))
    inside_point = 0
    for point in possible_inside_point:
        x = point[0]
        y = point[1]
        nb_wall = 0
        while x < len(matrice):
            if pipe_map_matrice_2[y][x] in 'FLJ7|S':
                nb_wall += 1
            if pipe_map_matrice_2[y][x] == 'F' and pipe_map_matrice_2[y][x+1] == 'J':
                x += 2
            elif pipe_map_matrice_2[y][x] == 'L' and pipe_map_matrice_2[y][x+1] == '7':
                x += 2
            else:
                x += 1
        if nb_wall % 2 == 1:
            inside_point += 1
    print('inside_point', inside_point)





    for line in pipe_map_matrice_2:
        trap = True
        for element in line:
            # if element != 'O' and element != 'I':
            #     trap = not trap
            if element == 'I' and trap:
                nb_points += 1
    print('nb_points', nb_points)
    nb_0 = 0
    nb_total = 0
    for line in pipe_map_matrice_2:
        for element in line:
            nb_total += 1
            if element == 'O':
                nb_0 += 1
    print('nb_0', nb_0)
    print('nb_total', nb_total)


        



def get_neighbors(matrice, row, col):
    neighbors = []

    # Directions possibles : haut, bas, gauche, droite
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        try:
            # Tentative d'accéder au voisin
            neighbor_value = matrice[row + dr][col + dc]
            if neighbor_value != 'X' and neighbor_value != 'O':
              neighbors.append((row + dr, col + dc))
        except IndexError:
            # Gestion de l'exception si la position est en dehors des limites de la matrice
            pass

    return neighbors
  

def main():
    pipe_map = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #print(pipe_map)

    matrice = part_1(pipe_map)
    part_2(pipe_map, matrice)

    

    



if __name__ == "__main__":
    main()
   