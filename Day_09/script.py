import sys
from itertools import cycle
import math
import time

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    for i in range(len(lines)):
        lines[i] = [int(i) for i in lines[i].split()]
    return lines

def calc_diff_to_zero(line):
    flag = True
    work = [line]
    print('line', line)
    while flag:
        new_line = [work[-1][i+1] - work[-1][i] for i in range(len(work[-1])-1)]
        work.append(new_line)
        if all(element == 0 for element in new_line):
            flag = False            
    return work

def extrapolate_next_value(dataset):
    for i in range(len(dataset)-1):
      step = dataset[-(i+1)]
      #print('step', step)
      dataset[-(i+2)].append(dataset[-(i+1)][-1] + dataset[-(i+2)][-1])
    for set in dataset:
        print('set', set)
    return dataset[0][-1]

def extrapolate_previous_value(dataset):
    for i in range(len(dataset)-1):
      step = dataset[-(i+1)]
      print('step', step)
      dataset[-(i+2)].insert(0, - dataset[-(i+1)][0] + dataset[-(i+2)][0])
    for set in dataset:
        print('set', set)
    return dataset[0][0]

    

def part_1(lines):
    lines = format_data(lines)
    #print(lines)
    extrapolated_values = []
    for line in lines:
        dataset = calc_diff_to_zero(line)
        #print('dataset', dataset)
        extrapolated_values.append(extrapolate_next_value(dataset))
    print('somme_extrapolated_values', sum(extrapolated_values))


        
def part_2(lines):
    lines = format_data(lines)
    print(lines)
    extrapolated_values = []
    for line in lines:
        dataset = calc_diff_to_zero(line)
        print('dataset', dataset)
        extrapolated_values.append(extrapolate_previous_value(dataset))
    print('somme_extrapolated_values', sum(extrapolated_values))
        
    
    

    

def main():
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    print(lines)
    #part_1(lines)
    part_2(lines)

    

    



if __name__ == "__main__":
    main()
   