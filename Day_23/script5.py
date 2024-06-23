import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re
import copy

moves_coordinates = [(-1, 0), (1, 0),(0, 1), (0, -1)]

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def count_point(map):
    count = 0
    for i in map:
        for j in i:
            if j != '#':
                count += 1
    return ('nombre de point', count)

def format_data(map):
    nodes = []
    matrice = [list(i) for i in map]
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == '#':
                continue
            matrice[i][j] = '.'
            neighbours = find_neighbours(matrice, i, j)
            if len(neighbours) != 2:
                matrice[i][j] = 'O'
                nodes.append((i,j))
            
    ecrire_matrice_dans_fichier(matrice, 'output.txt')
    print('len nodes', len(nodes))
    print('nodes', nodes)
    return matrice, nodes

def find_neighbours(matrice, i, j):
    neighbours = []
    for move in moves_coordinates:
        new_position = tuple(a + b for a, b in zip((i,j), move))
        if new_position[0] < 0 or new_position[0] >= len(matrice) or new_position[1] < 0 or new_position[1] >= len(matrice[0]) or matrice[new_position[0]][new_position[1]] == '#':
            continue
        neighbours.append(new_position)
    return neighbours

def ecrire_matrice_dans_fichier(matrice, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        for ligne in matrice:
            ligne_concatenee = ''.join(map(str, ligne))
            fichier.write(ligne_concatenee + '\n')


def part_2(matrice, nodes):
    ranges = []
    for node in nodes:
        start_position = node
        neighbours = find_neighbours(matrice, start_position[0], start_position[1])
        #print('neighbours', neighbours)
        matrice[start_position[0]][start_position[1]] = 'X'
        for neighbour in neighbours:
            #print('neighbour', neighbour)
            result = dfs(matrice, neighbour[1], neighbour[0], 1)
            if result:
                #print('result', result)
                ranges.append({'start': start_position, 'end': result[0], 'step': result[1]})
    
    ecrire_matrice_dans_fichier(matrice, 'output2.txt')
    ways = []
    for elt in ranges:
        if elt['start'] == (0,1):
            ways.append([elt])
            ranges.remove(elt)
    
    print('len ranges', len(ranges))  
    
    completed_ways = []
    while len(ways) > 0:
        ways, completed_ways = find_all_ways(ranges, ways, completed_ways)

    

    # print('ranges', ranges)
    # print('completed_ways', completed_ways)
    # print('len completed_ways', len(completed_ways))
    # print('1er completed_ways', completed_ways[0])
    # print('somme', sum([elt['step'] for elt in completed_ways[0]]))
    print('somme', max([sum([elt['step'] for elt in way]) for way in completed_ways]))
        
    return

def find_all_ways(ranges, ways, completed_ways):
    new_ways = []

    for way in ways:
        last_step = way[-1]
        for elt in ranges:
            # print('last_step', last_step)
            # print('elt', elt)
            if last_step['end'] == elt['start']:
                reversed_elt = copy.deepcopy(elt)
                reversed_elt['start'], reversed_elt['end'] = reversed_elt['end'], reversed_elt['start']
                if elt not in way and reversed_elt not in way:
                    temp_way = way + [elt]
                    if elt['end'] == (22,21):
                        completed_ways.append(temp_way)
                    else:
                        new_ways.append(temp_way)
            elif last_step['end'] == elt['end']:
                reversed_elt = copy.deepcopy(elt)
                reversed_elt['start'], reversed_elt['end'] = reversed_elt['end'], reversed_elt['start']
                if elt not in way and reversed_elt not in way:
                    temp_way = way + [reversed_elt]
                    if elt['end'] == (22,21):
                        completed_ways.append(temp_way)
                    else:
                        new_ways.append(temp_way)
    return new_ways, completed_ways

# Fonction auxiliaire pour effectuer le parcours en profondeur
def dfs(matrice, x, y, step):
    lignes = len(matrice)
    colonnes = len(matrice[0])

    # Vérifier si les coordonnées sont valides
    if 0 <= y < lignes and 0 <= x < colonnes:
        if matrice[y][x] == 'O':
            return (y,x), step

        elif matrice[y][x] == '.':
            # Marquer la case comme visitée
            matrice[y][x] = 'X'
            possibles_new_positions = [tuple(a + b for a, b in zip((y,x), move)) for move in moves_coordinates]
            for y,x in possibles_new_positions:
                result = dfs(matrice, x, y, step+1)
                if result:
                    return result
            



    
#def part_2(matrice):

def main():
    now = time.time()
    map = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    matrice, nodes = format_data(map)
    part_2(matrice, nodes)


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   