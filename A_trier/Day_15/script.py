import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re

def read_file(file):
    with open(file, "r") as f:
        return f.read().split(",")
    
def hash_algorithm(input_string):
    current_value = 0

    for char in input_string:
        ascii_code = ord(char)  # Determine the ASCII code for the current character
        current_value += ascii_code  # Increase the current value by the ASCII code
        current_value *= 17  # Multiply the current value by 17
        current_value %= 256  # Set the current value to the remainder of dividing itself by 256

    return current_value

#def format_data(lines):

def part_1(data):
    sum1 = 0
    for elt in data:
        sum1 += hash_algorithm(elt)
    print('part 1 :', sum1)
    
    
    
def part_2(data):
    dico = {}
    for elt in data:
        #print(elt)
        label = elt.split("=")[0].split("-")[0]
        #print('label', label)
        h = hash_algorithm(label)
        #print('h', h)
        if '=' in elt:
            dico.setdefault(h, {})[label] = elt.split('=')[1]            
        elif '-' in elt and h in dico:
            # Supprimer le label s'il existe
            #print('label', label)
            #print('dico', dico)
            #print('h', h)
            if label in dico[h]:
                del dico[h][label]
    #print(dico)
    sum2 = 0
    for elt in dico:
        index = 1
        for label in dico[elt]:
            sum2 += (int(elt)+1) * int(dico[elt][label])*index
            index += 1
    print('part 2 :', sum2)

def main():
    now = time.time()
    data = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #print(data)
    part_1(data)
    part_2(data)



    # Example usage:
    # input_string = "cm-"
    # result = hash_algorithm(input_string)
    # print(f"The HASH value for '{input_string}' is: {result}")


    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   