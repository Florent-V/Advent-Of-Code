from Libs.SolutionBase import SolutionBase

class Solution(SolutionBase):

  moves_coordinates = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'O': (0, -1)}
  moves = {
      '-': ['E', 'O'],
      '|': ['S', 'N'],
      'J': ['O', 'N'],
      'L': ['E', 'N'],
      'F': ['S', 'E'],
      '7': ['S', 'O'],
      'S': ['N', 'S', 'E', 'O'],
  }

  def search_adjacent(self,tile, position, a_max, b_max):
    adjacent = []
    if tile not in Solution.moves:
        return adjacent
    for move in Solution.moves[tile]:
        new_position = tuple(a + b for a, b in zip(position, Solution.moves_coordinates[move]))
        if all(0 <= coord < max_val for coord, max_val in zip(new_position, (a_max, b_max))):
            adjacent.append(new_position)
    return adjacent

  def find_starting_point(self, lines):
      for i in range(len(lines)):
          for j in range(len(lines[i])):
              if lines[i][j] == 'S':
                  return (i, j)
  
  def part_1(self, map):
    """returns the solution for part_a"""
    start = self.find_starting_point(map)
    i_max, j_max = len(map), len(map[0])
    visited = set([start])
    queue = [start]  
    step = 0
    while queue:
        position = queue.pop(0)
        tile = map[position[0]][position[1]]
        for position in self.search_adjacent(tile, position, i_max, j_max):
            if position not in visited and map[position[0]][position[1]] != '.':
                visited.add(position)
                queue.append(position)            
        step += 1
    return step/2

  def part_2(self, map):
    """returns the solution for part_b"""
    start = self.find_starting_point(map)
    i_max, j_max = len(map), len(map[0])
    queue = [start]  
    pipes = set()
    while queue:
        x1, y1 = queue.pop(0)
        tile = map[x1][y1]
        for x2, y2 in self.search_adjacent(tile, (x1, y1), i_max, j_max):
            if (x1,y1) not in self.search_adjacent(map[x2][y2], (x2, y2), i_max, j_max):
                continue
            pipe = (*sorted((x1, x2)), *sorted((y1, y2)))
            if pipe not in pipes:
                pipes.add(pipe)
                queue.append((x2, y2))            
 
    m, n = len(map), len(map[0])
    visited = set()
    corner_q = [(0, 0)]

    while corner_q:
        x, y = corner_q.pop()
        requirements = (x > 0, y < n, x < m, y > 0)
        adjacent = ((x-1, y), (x, y+1), (x+1, y), (x, y-1))
        tile_pairs = ((x-1, x-1, y-1, y),   # up
                      (x-1, x, y, y),       # right
                      (x, x, y-1, y),       # down
                      (x-1, x, y-1, y-1))   # left
        for req, corner, tile_pair in zip(requirements, adjacent, tile_pairs):
            if req and corner not in visited and tile_pair not in pipes:
                visited.add(corner)
                corner_q.append(corner)

    total = m * n - len(pipes)
    for i in range(m):
        for j in range(n):
            corners = ((i, j), (i+1, j), (i, j+1), (i+1, j+1))
            if all(c in visited for c in corners):
                total -= 1

    return total
