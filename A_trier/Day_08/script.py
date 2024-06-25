import sys
from itertools import cycle
import math
import time

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    data = {}
    for line in lines:
        split = line.split(' = ')
        data[split[0]] = (split[1].strip('()').split(', ')[0], split[1].strip('()').split(', ')[1])
    return data

def part_1(lines):
    instructions = lines[0]
    nodes = format_data(lines[2:])
    print('instructions', instructions)
    print('nodes', nodes)
    flag = True
    destination = 'AAA'
    nb_steps = 0
    while flag:
        for i in instructions:
            nb_steps += 1
            if i == 'R':
                destination = nodes[destination][1]
            else:
                destination = nodes[destination][0]
            if destination == 'ZZZ':
                flag = False
                break
    print('nb_steps', nb_steps)

def find_loop(node, map_nodes, instructions):
    loop = []
    step = 0
    instructions_length = len(instructions)
    for instruction in cycle(instructions):
        dir = 0 if instruction == 'L' else 1
        node = map_nodes[node][dir]

        if node.endswith('Z'):
            loop.append(step)
        
        if len(loop) == 2:
            return loop[1] - loop[0]
      
        step += 1
    

    
def part_2(lines):
    instructions = lines[0]
    map_nodes = format_data(lines[2:])
    initial_nodes = [dest for dest in map_nodes if dest.endswith('A')]
    print('instructions', instructions)
    print('longueur instructions', len(instructions))
    #print('nodes', map_nodes)
    freq_z_in_each_node = []
    for node in initial_nodes:
        print('node', node)
        loop = find_loop(node, map_nodes, instructions)
        print('loop', node, loop)
        freq_z_in_each_node.append(loop)

        #last_z = find_last_z_node(loop)
    print('freq_z_in_each_node', freq_z_in_each_node)
    part_2 = math.lcm(*freq_z_in_each_node)
    print(f'Solution: {part_2}')

    

def main():
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #part_1(lines)
    now = time.time()

    part_2(lines)
    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   