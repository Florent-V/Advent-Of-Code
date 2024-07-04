from Libs.SolutionBase import SolutionBase
from itertools import cycle
import math

class Solution(SolutionBase):

  def format_data(self, lines):
    data = {}
    for line in lines:
        split = line.split(' = ')
        data[split[0]] = (split[1].strip('()').split(', ')[0], split[1].strip('()').split(', ')[1])
    return data
  
  def find_loop(self, node, map_nodes, instructions):
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
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    instructions = lines[0]
    nodes = self.format_data(lines[2:])
    flag = True
    destination = 'AAA'
    nb_steps = 0
    for instruction in cycle(instructions):
      dir = 0 if instruction == 'L' else 1
      nb_steps += 1
      destination = nodes[destination][dir]
      if destination == 'ZZZ':
        flag = False
        break
    return nb_steps
    

  def part_2(self, lines):
    """returns the solution for part_b"""
    instructions = lines[0]
    map_nodes = self.format_data(lines[2:])
    initial_nodes = [dest for dest in map_nodes if dest.endswith('A')]
    freq_z_in_each_node = []
    for node in initial_nodes:
        loop = self.find_loop(node, map_nodes, instructions)
        freq_z_in_each_node.append(loop)
    part_2 = math.lcm(*freq_z_in_each_node)
    return part_2
