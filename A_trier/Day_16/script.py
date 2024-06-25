import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

moves_coordinates = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'O': (0, -1)}
possibles_moves = {
    'E': {'-' : 'E',
          '|' : 'NS',
          '/' : 'N',
          '\\' : 'S',
          '.': 'E'
          },
    'O': {'-' : 'O',
          '|' : 'NS',
          '/' : 'S',
          '\\' : 'N',
          '.': 'O'
          },
    'N': {'-' : 'EO',
          '|' : 'N',
          '/' : 'E',
          '\\' : 'O',
          '.': 'N'
          },
    'S': {'-' : 'EO',
          '|' : 'S',
          '/' : 'O',
          '\\' : 'E',
          '.': 'S'
          },
}


def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    matrice = []
    for line in lines:
        matrice.append(list(line))
    return matrice

def part_1(map_matrice):
    position = (0,0)
    direction = possibles_moves['E'][map_matrice[position[0]][position[1]]]
    history = []
    possibles_way = [{'position': position, 'direction': direction}]
    energy_matrice = [['.' for i in range(len(map_matrice[j]))] for j in range(len(map_matrice))]
    energy_matrice[position[0]][position[1]] = '#'
    flag = True
    energized = 0
    index = 0
    count = 0
    while len(possibles_way) > 0:
        index += 1
        #print('possibles_way', possibles_way)
        #print('history', history)
        for way in possibles_way[:]:
            if way not in history:
                history.append(way.copy())
            else:
                possibles_way.remove(way)
                continue
            #print('history', history)
            #print('way', way)
            #print('position', way['position'])
            #print('direction', way['direction'])
            new_position = tuple(a + b for a, b in zip(way['position'], moves_coordinates[way['direction']]))
            #print('new_position', new_position)
            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(map_matrice) or new_position[1] >= len(map_matrice[new_position[0]]):
                #print('out of range') 
                possibles_way.remove(way)
                continue
            new_pipe = map_matrice[new_position[0]][new_position[1]]
            energy_matrice[new_position[0]][new_position[1]] = '#'
            #print('new_pipe', new_pipe)
            if new_pipe == '.':
                #print('empty pipe')
                way['position'] = new_position
            elif new_pipe == '-':
                #print('horizontal pipe')
                if way['direction'] == 'E' or way['direction'] == 'O':
                    way['position'] = new_position
                elif way['direction'] == 'N' or way['direction'] == 'S':
                    way['position'] = new_position
                    way['direction'] = 'E'
                    possibles_way.append({'position': new_position, 'direction': 'O'})
            elif new_pipe == '|':
                #print('vertical pipe')
                if way['direction'] == 'N' or way['direction'] == 'S':
                    way['position'] = new_position
                elif way['direction'] == 'E' or way['direction'] == 'O':
                    way['position'] = new_position
                    way['direction'] = 'S'
                    possibles_way.append({'position': new_position, 'direction': 'N'})
            elif new_pipe == '/' or new_pipe == '\\':
                way['position'] = new_position
                way['direction'] = possibles_moves[way['direction']][new_pipe]

            
        nb_diese = 0
        for line in energy_matrice:
            nb_diese += line.count('#')
        if nb_diese == energized:
            count += 1
        else:
            count = 0
            energized = nb_diese
        print('nb_diese', nb_diese)
    nb_diese = 0
    for line in energy_matrice:
        print(''.join(line))
        nb_diese += line.count('#')
    print('nb_diese', nb_diese)
    return nb_diese

def finb_nb_diese(map_matrice, direction, position):
    direction = possibles_moves[direction][map_matrice[position[0]][position[1]]]
    #print('direction', direction)
    history = []
    possibles_way = [{'position': position, 'direction': direction} for direction in direction]
    energy_matrice = [['.' for i in range(len(map_matrice[j]))] for j in range(len(map_matrice))]
    energy_matrice[position[0]][position[1]] = '#'
    while len(possibles_way) > 0:
        #print('possibles_way', possibles_way)
        #print('history', history)
        for way in possibles_way[:]:
            if way not in history:
                history.append(way.copy())
            else:
                possibles_way.remove(way)
                continue
            #print('history', history)
            #print('way', way)
            #print('position', way['position'])
            #print('direction', way['direction'])
            new_position = tuple(a + b for a, b in zip(way['position'], moves_coordinates[way['direction']]))
            #print('new_position', new_position)
            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(map_matrice) or new_position[1] >= len(map_matrice[new_position[0]]):
                #print('out of range') 
                possibles_way.remove(way)
                continue
            new_pipe = map_matrice[new_position[0]][new_position[1]]
            energy_matrice[new_position[0]][new_position[1]] = '#'
            #print('new_pipe', new_pipe)
            if new_pipe == '.':
                #print('empty pipe')
                way['position'] = new_position
            elif new_pipe == '-':
                #print('horizontal pipe')
                if way['direction'] == 'E' or way['direction'] == 'O':
                    way['position'] = new_position
                elif way['direction'] == 'N' or way['direction'] == 'S':
                    way['position'] = new_position
                    way['direction'] = 'E'
                    possibles_way.append({'position': new_position, 'direction': 'O'})
            elif new_pipe == '|':
                #print('vertical pipe')
                if way['direction'] == 'N' or way['direction'] == 'S':
                    way['position'] = new_position
                elif way['direction'] == 'E' or way['direction'] == 'O':
                    way['position'] = new_position
                    way['direction'] = 'S'
                    possibles_way.append({'position': new_position, 'direction': 'N'})
            elif new_pipe == '/' or new_pipe == '\\':
                way['position'] = new_position
                way['direction'] = possibles_moves[way['direction']][new_pipe]
    nb_diese = 0
    for line in energy_matrice:
        #print(''.join(line))
        nb_diese += line.count('#')
    print('nb_diese', nb_diese)
    return nb_diese

def part_2(map_matrice):
    liste = []
    for i in range(len(map_matrice[0])):
        liste.append(finb_nb_diese(map_matrice, 'S', (0,i)))
        liste.append(finb_nb_diese(map_matrice, 'N', (len(map_matrice)-1,i)))
    for i in range(len(map_matrice)):
        liste.append(finb_nb_diese(map_matrice, 'E', (i,0)))
        liste.append(finb_nb_diese(map_matrice, 'O', (i,len(map_matrice[0])-1)))
    print('liste', liste)
    print('max', max(liste))
        


def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #print(lines)
    map_matrice = format_data(lines)
    #print(map_matrice) 
    #part_1(map_matrice)
    part_2(map_matrice)


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   