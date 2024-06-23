import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

#def format_data(lines):
#def part_1(matrice):
#def part_2(matrice):

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   