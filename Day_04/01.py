import sys
import re
from string import punctuation

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")
    


def main():
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    cards = list(map(lambda x: re.split(r'[:,|]', x), lines))
    print(cards)
    total_points = 0
    formatted_cards = []
    count_scratchcards = []
    for card in cards:
        card_number = card[0].split()[1]
        winning_numbers = set(card[1].split())
        my_numbers = set(card[2].split())
        bilan = list(my_numbers & winning_numbers)
        #print(len(bilan))
        card_points = 1 * (2**(len(bilan)-1)) if len(bilan) > 0 else 0
        total_points += card_points
        formatted_cards.append([int(card_number), len(bilan)])
        count_scratchcards.append([int(card_number), 1])
        #print(card_number, winning_numbers, my_numbers, bilan, card_points)
    print(total_points)
    print(formatted_cards)
    print(count_scratchcards)
    total_scrarchcards = 0
    for card in formatted_cards:
        for i in range(card[0], card[0]+card[1]):
            count_scratchcards[i][1] += 1*count_scratchcards[card[0]-1][1]
    print(count_scratchcards)
    for card in count_scratchcards:
        total_scrarchcards += card[1]
    print(total_scrarchcards)
    
    


    



if __name__ == "__main__":
    main()
   