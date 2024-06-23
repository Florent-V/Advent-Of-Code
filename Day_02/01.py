import sys
from math import prod

game = {
    "red": 12,
    "blue": 14,
    "green": 13,
}

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")
    
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

def main():
    games = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    possible_games = []
    minimum_games = []
    for game in games:
        [part_1, part_2] = game.split(':')
        if (is_game_valid(part_2)):
            possible_games.append(int(part_1.split()[1]))
        minimum_games.append(min_game_token(part_2))
    print('somme des jeux possibles', sum(possible_games))
    print('somme', process_minimum_games(minimum_games))

if __name__ == "__main__":
    main()
   