from Libs.SolutionBase import SolutionBase
from Libs.Parsers import parse_matrice_string_to_int_list

class Solution(SolutionBase):

  def calc_diff_to_zero(self, line):
    flag = True
    work = [line]
    # print('line', line)
    while flag:
        new_line = [work[-1][i+1] - work[-1][i] for i in range(len(work[-1])-1)]
        work.append(new_line)
        if all(element == 0 for element in new_line):
            flag = False            
    return work

  def extrapolate_next_value(self, dataset):
      for i in range(len(dataset)-1):
        step = dataset[-(i+1)]
        # print('step', step)
        dataset[-(i+2)].append(dataset[-(i+1)][-1] + dataset[-(i+2)][-1])
      return dataset[0][-1]

  def extrapolate_previous_value(self, dataset):
      for i in range(len(dataset)-1):
        step = dataset[-(i+1)]
        # print('step', step)
        dataset[-(i+2)].insert(0, - dataset[-(i+1)][0] + dataset[-(i+2)][0])
      return dataset[0][0]
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    lines = parse_matrice_string_to_int_list(lines)
    extrapolated_values = []
    for line in lines:
        dataset = self.calc_diff_to_zero(line)
        extrapolated_values.append(self.extrapolate_next_value(dataset))
    return sum(extrapolated_values)

  def part_2(self, lines):
    """returns the solution for part_b"""
    lines = parse_matrice_string_to_int_list(lines)
    extrapolated_values = []
    for line in lines:
        dataset = self.calc_diff_to_zero(line)
        extrapolated_values.append(self.extrapolate_previous_value(dataset))
    return sum(extrapolated_values)
