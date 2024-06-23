import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re
import copy

moves_coordinates = [(-1, 0), (1, 0),(0, 1), (0, -1)]

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")
    
def find_start(map):
    return 0, map[0].index('.')

def find_part_ways(map, current_ways, one_ways):
    new_ways = []
    for way in current_ways:
        positions = way[:]
        possibles_new_positions = [tuple(a + b for a, b in zip(positions[-1], move)) for move in moves_coordinates]
        new_positions = []
        for position in possibles_new_positions:
            if position[0] < 0 or position[0] >= len(map) or position[1] < 0 or position[1] >= len(map[0]):
                continue
            if map[position[0]][position[1]] in '#O' or position in way:
                continue
            new_positions.append(position)
        if len(new_positions) == 1:
            map[new_positions[0][0]][new_positions[0][1]] = 'O'
            positions.append(new_positions[0])
            new_ways.append(positions)
        else:
            one_ways.append(positions)
            for new_position in new_positions:
                map[new_position[0]][new_position[1]] = 'O'
                new_ways.append([new_position])
    return new_ways, one_ways

def count_point(map):
    count = 0
    for i in map:
        for j in i:
            if j != '#':
                count += 1
    return ('nombre de point', count)

def find_first_step(one_ways):
    for way in one_ways:
        if way[0] == (0, 1):
            one_ways.remove(way)
            return one_ways, [way]

def find_next_ways(one_ways, positions):
    next_ways = []
    for position in positions:
        for way in one_ways:
            if way[0] == position:
                next_ways.append(way)
            elif way[-1] == position:
                next_ways.append(list(reversed(way)))
    return next_ways

def find_all_ways(map, possible_ways, one_ways, final_ways):
    new_ways = []
    for i in range(len(possible_ways)):
        print('way en cours', possible_ways[i])
        last_position = possible_ways[i][-1]
        print('last_position', last_position)
        possibles_new_positions = [tuple(a + b for a, b in zip(last_position, move)) for move in moves_coordinates]
        new_positions = []
        for position in possibles_new_positions:
            if position[0] < 0 or position[0] >= len(map) or position[1] < 0 or position[1] >= len(map[0]):
                continue
            new_positions.append(position)
        print('new next _positions possible', new_positions)
        possible_next_ways = find_next_ways(one_ways, new_positions)
        print('possible_next_ways')
        for j in possible_next_ways:
            print(j)
        for possible_next_way in possible_next_ways:
            temp_way = possible_ways[i] + possible_next_way
            if len(set(temp_way)) != len(temp_way):
                print('#####################################################################doublon')
                continue
            if possible_next_way[-1] == (22,21):
                print('###########################################################YOUHOU')
                final_ways.append(temp_way)
            print('new temp_way', temp_way)
            new_ways.append(temp_way)

    return new_ways, final_ways



#def format_data(lines):
def part_2(map):
    current_ways = []
    map = [list(i) for i in map]
    nb_points = count_point(map)
    current_ways.append([find_start(map)])
    end_position = len(map)-1, map[len(map)-1].index('.')
    print('end_position', end_position)
    print('initial ways', current_ways)
    one_ways = []
    while len(current_ways) > 0:
        current_ways, one_ways = find_part_ways(map, current_ways, one_ways)
        # print('ways fin de step', ways)
        # print('matrice fin de step')
    for i in map:
        print(''.join(i))
    for way in one_ways:
        print(way)
    print('nombre de point', nb_points)
    one_ways, possible_ways = find_first_step(one_ways)
    print('one_ways', one_ways)
    print('possible_ways', possible_ways)
    final_ways = []
    while len(possible_ways) > 0:
        print('coucou')
        possible_ways, final_ways = find_all_ways(map, possible_ways, one_ways, final_ways)
    for i in final_ways:
        print('longeur', len(i))
        print(i)





    

        
def main():
    now = time.time()
    map = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #print(map)
    part_2(map)


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   