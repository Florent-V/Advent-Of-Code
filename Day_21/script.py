import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

moves_coordinates = [(-1, 0), (1, 0),(0, 1), (0, -1)]

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")
    
def find_start(map):
    # trouver coordonnées du point de départ S dans la map
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'S':
                return x, y
  
def make_one_step(positions, map, max_ligne, max_colonne):
    #print('new step', positions, 'longueur', len(positions))
    new_positions = []
    for position in positions:
        #print('position', position)
        for move in moves_coordinates:
            #print('move', moves_coordinates[move])
            #print('position', position)
            new_position = tuple(a + b for a, b in zip(position, move))
            #print('new_position', new_position)
            if map[new_position[0]%131][new_position[1]%131] != '#':
                #print('possible')
                new_positions.append(new_position)
                #map[new_position[0]][new_position[1]] = '0'
    #print('new_positions', new_positions)
    #print('len new_positions', len(new_positions))
    #print('new_positions', new_positions)
    new_positions = list(set(new_positions))
    new_positions.sort()
    #print('suppression doublons')
    #print('len new_positions', len(new_positions))
    #print('new_positions', new_positions)
    new_positions.sort()
    return new_positions
 
def format_data(lines):
    matrice_garden = []
    for i in lines:
        matrice_garden.append(list(i))
    return matrice_garden
#def part_1(matrice):
#def part_2(matrice):

def main():
    now = time.time()
    map = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    start = find_start(map)
    gardens = []
    gardens.append([start])
    map_matrice = format_data(map)
    max_ligne = len(map_matrice)
    max_colonne = len(map_matrice[0])
    print('start', start)
    print('max_ligne', max_ligne)
    print('max_colonne', max_colonne)
    print('gardens', gardens)
    values = {}
    for i in range(64):
        print('step', i+1)
        gardens.append(make_one_step(gardens[-1], map_matrice, max_ligne, max_colonne))
        print(len(gardens[-1]))
        values[i+1] = len(gardens[-1])
        gardens.pop(0)
    print('gardens', gardens)
    print('longueur garden', len(gardens))
    print(len(gardens[-1]))
    print('values', values)



    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   