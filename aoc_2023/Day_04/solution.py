from Libs.SolutionBase import SolutionBase
import re

class Solution(SolutionBase):

  def format_data(self, card):
    winning_numbers = set(card[1].split())
    my_numbers = set(card[2].split())
    bilan = list(my_numbers & winning_numbers)
    return bilan
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    cards = list(map(lambda x: re.split(r'[:,|]', x), lines))
    total_points = 0
    for card in cards:
        bilan = self.format_data(card)
        card_points = 1 * (2**(len(bilan)-1)) if len(bilan) > 0 else 0
        total_points += card_points
    return total_points

  def part_2(self, lines):
    """returns the solution for part_b"""
    cards = list(map(lambda x: re.split(r'[:,|]', x), lines))
    formatted_cards = []
    count_scratchcards = []
    for card in cards:
        card_number = card[0].split()[1]
        bilan = self.format_data(card)
        formatted_cards.append([int(card_number), len(bilan)])
        count_scratchcards.append([int(card_number), 1])
    total_scrarchcards = 0
    for card in formatted_cards:
        for i in range(card[0], card[0]+card[1]):
            count_scratchcards[i][1] += 1*count_scratchcards[card[0]-1][1]
    for card in count_scratchcards:
        total_scrarchcards += card[1]
    return total_scrarchcards
