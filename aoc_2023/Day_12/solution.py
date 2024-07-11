from Libs.SolutionBase import SolutionBase
from functools import cache

class Solution(SolutionBase):

  def format_data(self, lines):
    return [ (a, tuple(int(x) for x in b.split(','))) for a, b in [line.split() for line in lines]]
  
  @cache
  def get_arrangements(self, record, criteria, size=0):
      if not record:
          return 1 if not criteria or (len(criteria) == 1 and criteria[0] == size) else 0

      arrangements = 0
      for case in ('#', '.') if record[0] == '?' else record[0]:
          if case == '#':
              if criteria:
                  arrangements += self.get_arrangements(record[1:], criteria, size + 1)
          else:
              if 0 < size == criteria[0]:
                  arrangements += self.get_arrangements(record[1:], criteria[1:])
              elif size == 0:
                  arrangements += self.get_arrangements(record[1:], criteria)

      return arrangements
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    data = self.format_data(lines)
    return sum(
        self.get_arrangements(record, criteria)
        for record, criteria in data)

  def part_2(self, lines):
    """returns the solution for part_b"""
    data = self.format_data(lines)
    return sum(
        self.get_arrangements((("?" + record) * 5)[1:], criteria * 5)
        for record, criteria in data)
