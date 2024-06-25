import collections

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

def hand_strength(hand_type):
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
    return strength_order.index(hand_type)

# Example usage:
hand = "AAAAA"
hand_type = detect_hand_type(hand)

hands = ["AAAAA", "AA8AA", "23332", "TTT98", "23432", "A23A4", "23456"]
for hand in hands:
    hand_type = detect_hand_type(hand)
    print(f"The hand '{hand}' is a {hand_type}. It has a strength of {hand_strength(hand_type)}.")




