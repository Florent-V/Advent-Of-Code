import math
from itertools import cycle
import re
import sys

def read_multisection_input(file, transformers=None, example=False):
    """
    Read multisection puzzle input for file `/inputs/day_{day}.txt'
    and apply transformer function to each section.

    If `example` is set to True, read file `/inputs/day_{day}_example.txt`
    instead
    """

    try:
        with open(file) as input_file:
            sections = input_file.read().split('\n\n')
            return [transformer(section) for section, transformer in zip(sections, transformers)]
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

def map_transformer(section):
    the_map = {}
    for line in section.split('\n'):
        key, left, right = re.findall(r'[0-9A-Z]{3}', line)
        the_map[key] = (left, right)
    return the_map

def find_loop(node, the_map, instructions):
    sequence = []
    step = 0
    instructions_length = len(instructions)
    for instruction in cycle(instructions):
        idx = 0 if instruction == 'L' else 1
        node = the_map[node][idx]
        
        mod_step = step % instructions_length
        if (mod_step, node) in sequence:
            print('mod_step', node, mod_step)
            return step, sequence
        
        sequence.append((mod_step, node))
        step += 1
        
def find_last_z_node(seq):
    for i in range(len(seq)):
        node = seq[-(i+1)][1]
        if node.endswith('Z'):
            return i

instructions, the_map = read_multisection_input('input.txt', [str, map_transformer])
print(instructions)
#print(the_map)
start_nodes = [key for key in the_map if key.endswith('A')]
print('start node', start_nodes)
last_z_in_each_loop = []
for node in start_nodes:
    print('node', node)
    loop_step, seq = find_loop(node, the_map, instructions)
    print('loop_step', loop_step)
    #print('seq', seq)
    last_z_offset = find_last_z_node(seq)
    print('last_z_offset', last_z_offset)
    last_z_in_each_loop.append(loop_step - last_z_offset)
    print(last_z_in_each_loop)

# part_2 = math.lcm(*last_z_in_each_loop)
# print(f'Solution: {part_2}')
#assert part_2 == 12357789728873