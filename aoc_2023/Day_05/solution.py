from Libs.SolutionBase import SolutionBase
import math

class Solution(SolutionBase):

  # Commons methods
  def parse_input(self, lines):
    """returns the parsed input"""
    lines = [line for line in lines if line]
    seeds = [int(i) for i in lines.pop(0).split()[1:]]
    sections = {}
    current_key = ''
    for line in lines:
      if line.endswith('map:'):
        current_key = line.replace('map:', '').strip()
        continue
      sections.setdefault(current_key, []).append([int(x) for x in line.split()])
    return seeds, sections

  def sort_section(self, sections):
    for section in sections:
        sections[section].sort(key=lambda x: x[1])
    return sections

  def find_correspondance(self, number, section):
      for elt in section:
          if (number >= elt[1]) and (number < (elt[1] + elt[2])):
              return number + (elt[0]-elt[1])
      return number

  def calculate_location(self, seed, sections):
      steps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
      for step in steps:
          seed = self.find_correspondance(seed, sections[step])
      return seed
  
  # Part 2 Methods
  def best_location_range(self, item_range, sections):
    test = item_range
    sample = []
    step = 10000
    shortest_location = math.inf
    for i in range(test[0], test[1], step):
        location = self.calculate_location(i, sections)
        if location < shortest_location:
            shortest_location = location
            sample = [i, location]
    for i in range(sample[0]-step, sample[0]+step, 1):
        location = self.calculate_location(i, sections)
        if location < shortest_location:
            shortest_location = location
            sample = [i, location]
    return sample

  
  def part_1(self, lines):
    """returns the solution for part_a"""
    seeds, sections = self.parse_input(lines)
    sections = self.sort_section(sections)
    shortest_location = math.inf
    for seed in seeds:
        location = self.calculate_location(seed, sections)
        if location < shortest_location:
            shortest_location = location
    return shortest_location

  def part_2(self, lines):
    """returns the solution for part_b"""
    seeds, sections = self.parse_input(lines)
    sections = self.sort_section(sections)
    range_seeds = []
    for i in range(0, len(seeds), 2):
        range_seeds.append([seeds[i], seeds[i+1]])
    for item in range_seeds:
        item[1] = item [0] + item [1]
    best_locations = []
    for range_item in range_seeds:
        best_locations.append(self.best_location_range(range_item, sections))
    tableau_plus_petit = min(best_locations, key=lambda x: x[1])
    return min(tableau_plus_petit)
