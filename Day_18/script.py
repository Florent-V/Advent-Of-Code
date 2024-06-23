import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

moves_coordinates = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
true_moves_coordinates = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    temp = [line.split(' ') for line in lines]
    print(temp)
    dig_instruction = []
    true_dig_instruction = []
    for i in temp:
        dig_instruction.append([moves_coordinates[i[0]],int(i[1])])
        true_instruction = i[2].strip('()')
        #print('true_instruction', true_instruction)
        true_dig_instruction.append([moves_coordinates[true_moves_coordinates[true_instruction[-1]]],int(true_instruction[1:-1], 16)])
        #print('true_dig_instruction', true_dig_instruction)
    return dig_instruction, true_dig_instruction


  
def part_1(dig_instruction):
    dig_position = []
    position = (0,0)
    max_line = 0
    max_column = 0
    min_line = 0
    min_column = 0
    dig_position.append(position)
    nb_dig = 0
    for line in dig_instruction:
          nb_dig += line[1]
          position = tuple(a + b*line[1] for a, b in zip(position, line[0]))
          dig_position.append(position)
    print('dig_position', dig_position)
    print('aire_shoelace', aire_shoelace(dig_position))
    print('shoelace_area', shoelace_area(dig_position))
    dig_inside = volume_inside(dig_position, nb_dig) 
    dig_total = dig_inside + nb_dig
    print('dig_total', dig_total)

        
    return
#def part_2(matrice):

def shoelace_area(vertices):
    print(vertices)
    area = 0
    for i in range(-1, len(vertices)-1):
        area += vertices[i][0]*(vertices[i+1][1] - vertices[i-1][1])
    return abs(area/2)

def volume_inside(vertices, count):
    area =  shoelace_area(vertices)
    total = area + 1 - (count//2)
    return int(total) 

def aire_shoelace(coord_sommets):
    n = len(coord_sommets)
    aire = 0

    for i in range(n):
        x1, y1 = coord_sommets[i]
        x2, y2 = coord_sommets[(i + 1) % n]  # Pour obtenir le dernier sommet pour la connexion circulaire

        aire += x1 * y2
        aire -= x2 * y1

    return abs(aire) / 2.0

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    dig_instruction, true_dig_instruction = format_data(lines)
    part_1(dig_instruction)
    part_1(true_dig_instruction)



    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   