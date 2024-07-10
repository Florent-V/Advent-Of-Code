from Libs.SolutionBase import SolutionBase
from Libs.Parsers import parse_matrice_string_to_list
from Libs.Utils import matrix_shape
from itertools import combinations

class Solution(SolutionBase):

  def expand_universe(self, galaxies, empy_lines, empty_columns, expansion_coeff):
      empy_lines.reverse()
      empty_columns.reverse()
      for empty_line in empy_lines:
          for galaxy in galaxies:
              if galaxy[0] > empty_line:
                  galaxy[0] += expansion_coeff - 1

      for empty_col in empty_columns:
          for galaxy in galaxies:
              if galaxy[1] > empty_col:
                  galaxy[1] += expansion_coeff - 1

      return galaxies
  
  def get_galaxies_map(self, input_lines, expansion_coeff):
    matrice = parse_matrice_string_to_list(input_lines)
    empty_lines = [i for i, ligne in enumerate(matrice) if '#' not in ligne]
    empty_columns = [j for j in range(len(matrice[0])) if all(matrice[i][j] == '.' for i in range(len(matrice)))]
    y, x = matrix_shape(matrice)
    galaxies = [[i, j] for i in range(y) for j in range(x) if matrice[i][j] == '#']
    new_galaxies = self.expand_universe(galaxies, empty_lines, empty_columns, expansion_coeff)
    return new_galaxies
  
  def sum_shortest_distance(self, galaxies):
    total_distance = 0
    for paire in list(combinations(galaxies, 2)):
        total_distance += abs(paire[0][0] - paire[1][0]) + abs(paire[0][1] - paire[1][1])
    return total_distance
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    new_galaxies = self.get_galaxies_map(lines, expansion_coeff=2)
    return self.sum_shortest_distance(new_galaxies)

  def part_2(self, lines):
    """returns the solution for part_b"""
    new_galaxies = self.get_galaxies_map(lines, expansion_coeff=1_000_000)
    return self.sum_shortest_distance(new_galaxies)

