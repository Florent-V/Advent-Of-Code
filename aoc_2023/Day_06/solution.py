from Libs.SolutionBase import SolutionBase
import math

class Solution(SolutionBase):
  
  def format_data(self, lines):
    data = {}
    for line in lines:
        info = line.split()
        data[info[0]] = info[1:]
    return data
    
  def find_way_to_win(self, time, distance):
    number_of_way = 0
    for i in range(0, time+1):
        dist = (time - i) * i
        if dist > distance:
            number_of_way += 1
    return number_of_way

  def part_1(self, lines):
    """returns the solution for part_a"""
    data = self.format_data(lines)
    ways = []
    for i in range(len(data['Time:'])):
        ways.append(self.find_way_to_win(int(data['Time:'][i]), int(data['Distance:'][i])))
    return math.prod(ways)

  def part_2(self, lines):
    """returns the solution for part_b"""
    data = self.format_data(lines)
    data['Time:'] = ''.join(data['Time:'])
    data['Distance:'] = ''.join(data['Distance:'])
    return self.find_way_to_win(int(data['Time:']), int(data['Distance:']))

