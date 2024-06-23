import sys
from itertools import chain, combinations, permutations, combinations_with_replacement
import time
import re

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    data = []
    for line in lines:
        temp = [line.split(":")[0]] + line.split(":")[1].split(" ")
        data.append([elt for elt in temp if elt])
    return data


def part_1(data):
    group_1 = data[0]
    data.pop(0)
    for group in data:
        for elt in group:
            if elt in group_1:
                group_1 += group
                data.remove(group)
                break
    
    group_1 = list(set(group_1))
    print('len group_1', len(group_1))
    print('groupe_1', group_1)
    
    
    
    group_2 = list(chain(*data))
    group_2 = list(set(group_2))
    print('len groupe_2', len(group_2))
    print('group_2', group_2)
            

    
        
    return
    


#def part_2(matrice):

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    data = format_data(lines)
    part_1(data)


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   