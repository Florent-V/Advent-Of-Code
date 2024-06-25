import sys
import math
import collections

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    data = []
    for line in lines:
        data.append({'hand': line.split()[0], 'mise': line.split()[1]})
    return data
    
def detect_hand_type(hand):
    # Count the occurrences of each card
    card_counts = collections.Counter(hand)

    # Check for Five of a kind
    if 5 in card_counts.values():
        return "Five of a kind"

    # Check for Four of a kind
    if 4 in card_counts.values():
        return "Four of a kind"

    # Check for Full house
    if 3 in card_counts.values() and 2 in card_counts.values():
        return "Full house"

    # Check for Three of a kind
    if 3 in card_counts.values():
        return "Three of a kind"

    # Check for Two pair
    if list(card_counts.values()).count(2) == 2:
        return "Two pair"

    # Check for One pair
    if 2 in card_counts.values():
        return "One pair"

    # If none of the above conditions are met, it's a High card
    return "High card"

def hand_strength(hand):
    # Define a key function to determine the strength of each hand
    strength_order = [
        "Five of a kind",
        "Four of a kind",
        "Full house",
        "Three of a kind",
        "Two pair",
        "One pair",
        "High card"
    ]
    strength_order.reverse()
   
    if 'J' not in hand['hand']:
      return strength_order.index(detect_hand_type(hand['hand']))
    
    possible_strength = []
    print('coucou', hand['hand'])
    # tester le score de la main en remplaçant les J par les valeurs possibles
    for i in "23456789TJQKA":
      possible_hand = hand['hand'].replace('J', i)
      possible_strength.append(strength_order.index(detect_hand_type(possible_hand)))
    # retourner le score le plus élévé
    return max(possible_strength)


def part_1(hands):
    for hand in hands:
        hand['hand_score'] = hand_strength(hand)
    print('data: ', hands)
    # Tri de la liste selon la clé 'hand_score'
    sorted_hands = sorted(hands, key=comparer)
    print('sorted_hands: ', sorted_hands)
    total_winning = 0
    for index, hand in enumerate(sorted_hands):
        total_winning += int(hand['mise']) * (index + 1)
    print('total_winning: ', total_winning)


def part_2(hands):
    for hand in hands:
        hand['hand_score'] = hand_strength(hand)
    print('data: ', hands)
    # Tri de la liste selon la clé 'hand_score'
    sorted_hands = sorted(hands, key=comparer_bis)
    print('sorted_hands: ', sorted_hands)
    total_winning = 0
    for index, hand in enumerate(sorted_hands):
        total_winning += int(hand['mise']) * (index + 1)
    print('total_winning: ', total_winning)


# Exemples
mains = ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]

# Fonction de comparaison pour trier selon deux critères
def comparer(item):
    values_order = "23456789TJQKA"
    return (item['hand_score'], [values_order.index(c) for c in item['hand']])

def comparer_bis(item):
    values_order = "J23456789TQKA"
    return (item['hand_score'], [values_order.index(c) for c in item['hand']])

def main():
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    hands = format_data(lines)
    #part_1(hands)
    hands1 = format_data(lines)
    part_2(hands1)
    

    



if __name__ == "__main__":
    main()
   