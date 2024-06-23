def convert_hand(hand):
    """Convert a hand string to a tuple for sorting."""
    values = "23456789TJQKA"
    sorted_hand = sorted(hand, key=lambda card: values.index(card))
    return ''.join(sorted_hand)


def card_value(card):
    card_order = "AKQJT98765432A"
    return card_order.index(card)

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

    # Your logic to determine the type of hand goes here
    # You can use regular expressions or other methods to match the hand type

    # Return the index of the hand type in strength_order
    return strength_order.index(hand_type)

def sort_hands(hands):
    # Sort the hands based on their strength
    hands.sort(key=lambda hand: (hand_strength(hand), [card_value(card) for card in hand]))

# Example usage:
hands = ["AAAAA", "AA8AA", "23332", "TTT98", "23432", "A23A4", "23456"]
sort_hands(hands)
print(hands)
