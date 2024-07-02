from Libs.SolutionBase import SolutionBase
import collections

class Solution(SolutionBase):

  strength_order = [
        "Five of a kind",
        "Four of a kind",
        "Full house",
        "Three of a kind",
        "Two pair",
        "One pair",
        "High card"
  ]
  reversed_strength_order = strength_order[::-1]

  def format_data(self, lines):
    data = []
    for line in lines:
        data.append({'hand': line.split()[0], 'mise': line.split()[1]})
    return data

  def detect_hand_type(self, hand):
    # Count the occurrences of each card
    card_counts = collections.Counter(hand)

    if 5 in card_counts.values():
        return "Five of a kind"

    if 4 in card_counts.values():
        return "Four of a kind"

    if 3 in card_counts.values() and 2 in card_counts.values():
        return "Full house"

    if 3 in card_counts.values():
        return "Three of a kind"

    if list(card_counts.values()).count(2) == 2:
        return "Two pair"

    if 2 in card_counts.values():
        return "One pair"

    return "High card"
  
  def hand_strength(self, hand):
    # Define a key function to determine the strength of each hand
   
    if 'J' not in hand['hand']:
      return Solution.reversed_strength_order.index(self.detect_hand_type(hand['hand']))
    
    possible_strength = []
    # tester le score de la main en remplaçant les J par les valeurs possibles
    for i in "23456789TJQKA":
      possible_hand = hand['hand'].replace('J', i)
      possible_strength.append(Solution.reversed_strength_order.index(self.detect_hand_type(possible_hand)))
    # retourner le score le plus élévé
    return max(possible_strength)

  def compare(self, item, values_order):
    return (item['hand_score'], [values_order.index(c) for c in item['hand']])
  
  def sort_hand(self, hands, values_order):
    return sorted(hands, key=lambda item: self.compare(item, values_order))
  
  def calculate_total_winning(self, hands, values_order):
    sorted_hands = self.sort_hand(hands, values_order)
    total_winning = 0
    for index, hand in enumerate(sorted_hands):
        total_winning += int(hand['mise']) * (index + 1)
    return total_winning
  
  def part_1(self, lines):
    """returns the solution for part_a"""
    hands = self.format_data(lines)
    for hand in hands:
        hand['hand_score'] = Solution.reversed_strength_order.index(self.detect_hand_type(hand['hand']))
    return self.calculate_total_winning(hands, "23456789TJQKA")

  def part_2(self, lines):
    """returns the solution for part_b"""
    hands = self.format_data(lines)
    for hand in hands:
        hand['hand_score'] = self.hand_strength(hand)
    return self.calculate_total_winning(hands, "J23456789TQKA")
    
