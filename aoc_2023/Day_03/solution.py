from Libs.SolutionBase import SolutionBase
from itertools import product
from Libs.Utils import find_matches_with_positions, search_item_in_matrix_around
from math import prod
import re

class Solution(SolutionBase):

  @staticmethod
  def is_part(char):
    return char not in ".0123456789"

  def is_valid_number(self, lines, i, number):
    for j in range(number[1], number[2]):
          match = search_item_in_matrix_around(lines, i, j, Solution.is_part)
          if match:
            return True
          
          lambda x: x == '*'
                
  def valid_gear(self, lines, i, number):
    for j in range(number[1], number[2]):
          match = search_item_in_matrix_around(lines, i, j, lambda x: x == '*')
          if match:
            return (match[0], match[1], number[0])
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    valid_parts = []
    for i in range(len(lines)):
      numbers = find_matches_with_positions(r'\d+', lines[i])
      for number in numbers:
         if self.is_valid_number(lines, i, number):
           valid_parts.append(int(number[0]))
    return sum(valid_parts)


  def part_2(self, lines):
    """returns the solution for part_b"""
    gear_dict = {}
    for i in range(len(lines)):
      matches = find_matches_with_positions(r'\d+', lines[i])
      for number in matches:
         gear = self.valid_gear(lines, i, number)
         if gear:
           gear_dict.setdefault((gear[0], gear[1]), []).append(int(gear[2]))

    return sum([prod(v) for v in {k: v for k, v in gear_dict.items() if len(v) >= 2}.values()])

