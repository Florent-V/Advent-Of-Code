import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

moves_coordinates = [(-1, 0), (1, 0),(0, 1), (0, -1)]
illegal_moves = {(-1,0): 'v#', (1,0): '#^', (0,1): '<#', (0,-1): '>#'}

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")
    
def find_start(map):
    # trouver coordonnées du point de départ  dans la map
    # trouver index du '.' dans la 1ère ligne
    return 0, map[0].index('.')

def find_next_step(map, ways):
    #print('new step', positions, 'longueur', len(positions))
    new_ways = []
    step = 0
    for way in ways:
        # print('way in traitement', way)
        for move in moves_coordinates:
            positions = way['positions'][:]
            # print('way', way)
            # print('position', positions)
            # print('move', move)
            new_position = tuple(a + b for a, b in zip(positions[-1], move))
            # print('new_position', new_position)
            #check if new_position is in map
            if new_position[0] < 0 or new_position[0] >= len(map) or new_position[1] < 0 or new_position[1] >= len(map[0]):
                # print('out of map')
                continue
            if map[new_position[0]][new_position[1]] not in illegal_moves[move] and new_position not in way['positions']:
                # print('possible')
                positions.append(new_position)
                step = way['steps'] + 1
                new_ways.append({'positions': positions , 'steps': step})
                #map[new_position[0]][new_position[1]] = 'O'
    # print('new_ways', new_ways)
    return new_ways, step

#def format_data(lines):
def part_1(map):
    ways = []
    map = [list(i) for i in map]
    ways.append({'positions': [find_start(map)], 'steps': 0})
    #ways.append({'positions': [(19,12)], 'steps': 0})
    end_position = len(map)-1, map[len(map)-1].index('.')
    print('end_position', end_position)
    print('initial ways', ways)
    max_step = 0
    while len(ways) > 0:
        ways, step = find_next_step(map, ways)
        max_step = max(max_step, step)
        # print('ways fin de step', ways)
        # print('matrice fin de step')
    print('final ways', ways)
    print('final step', max_step)
        
    
#def part_2(matrice):

def main():
    now = time.time()
    map = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #print(map)
    part_1(map)


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   