import sys
import os
import time
from math import prod
# Get and add the Tools directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'Tools'))
sys.path.append(tools_dir)
from PuzzleReader import PuzzleReader
from CalculateDuration import CalculateDuration

game = {
    "red": 12,
    "blue": 14,
    "green": 13,
}

def get_file():
    file_name = sys.argv[1] if len(sys.argv) > 1 else 'input_light.txt'
    return PuzzleReader(file_name, os.path.dirname(os.path.abspath(__file__))).read_file()

def is_record_valid(record):
    for j in record.split(','):
        number, color = j.split()
        if int(number) > game[color]:
            return False
    return True
    
def is_game_valid(game):
    for record in game.split(';'):
      if (not is_record_valid(record)):
          return False
    return True

def min_game_token(game):
    token = {'red': 0, 'blue': 0, 'green': 0}
    for record in game.split(';'):
        for j in record.split(','):
            number, color = j.split()
            if int(number) > token[color]:
                token[color] = int(number)
    return token
            
def process_minimum_games(minimum_games):
    numbers = [list(dico.values()) for dico in minimum_games]
    return sum([prod(array) for array in numbers])

def common_part(games):
    possible_games = []
    minimum_games = []
    for game in games:
        [part_1, part_2] = game.split(':')
        if (is_game_valid(part_2)):
            possible_games.append(int(part_1.split()[1]))
        minimum_games.append(min_game_token(part_2))
    return possible_games, minimum_games

def part_1(possible_games):
    """Return the sum of possible games"""
    return sum(possible_games)


def part_2(minimum_games):
    """Return the sum of the power of the minimum games"""
    numbers = [list(dico.values()) for dico in minimum_games]
    return sum([prod(array) for array in numbers])


def main():
    games = get_file()
    chrono = CalculateDuration()
    possible_games, minimum_games = common_part(games)
    chrono.calculate()
    print(f"Durée d'exécution Partie Commune: {chrono.duration:.2e} sec")
    chrono.start()
    print(f"Résultat Partie 1: {part_1(possible_games)}")
    chrono.calculate()
    print(f"Durée d'exécution Partie 1: {chrono.duration:.2e} sec")
    chrono.start()
    print(f"Résultat Partie 2: {part_2(minimum_games)}")
    chrono.calculate()
    print(f"Durée d'exécution Partie 2: {chrono.duration:.2e} sec")


if __name__ == "__main__":
    main()
