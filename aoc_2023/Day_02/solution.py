from Libs.SolutionBase import SolutionBase
from math import prod

class Solution(SolutionBase):

  game = {
    "red": 12,
    "blue": 14,
    "green": 13,
  }

  def is_record_valid(self, record):
    for j in record.split(','):
        number, color = j.split()
        if int(number) > self.game[color]:
            return False
    return True
    
  def is_game_valid(self, game):
    for record in game.split(';'):
      if (not self.is_record_valid(record)):
          return False
    return True

  def min_game_token(self, game):
    token = {'red': 0, 'blue': 0, 'green': 0}
    for record in game.split(';'):
        for j in record.split(','):
            number, color = j.split()
            if int(number) > token[color]:
                token[color] = int(number)
    return token
            
  def process_minimum_games(self, minimum_games):
    numbers = [list(dico.values()) for dico in minimum_games]
    return sum([prod(array) for array in numbers])

  def common_part(self, games):
    possible_games = []
    minimum_games = []
    for game in games:
        [part_1, part_2] = game.split(':')
        if (self.is_game_valid(part_2)):
            possible_games.append(int(part_1.split()[1]))
        minimum_games.append(self.min_game_token(part_2))
    return possible_games, minimum_games

  def part_1(self, lines):
    """returns the solution for part_a"""
    possible_games, _minimum_games = self.common_part(lines)
    return sum(possible_games)

  def part_2(self, lines):
    """returns the solution for part_b"""
    _possible_games, minimum_games = self.common_part(lines)
    numbers = [list(dico.values()) for dico in minimum_games]
    return sum([prod(array) for array in numbers])
