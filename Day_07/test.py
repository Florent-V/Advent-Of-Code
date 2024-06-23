def convert_hand(hand):
    """Convert a hand string to a tuple for sorting."""
    values = "23456789TJQKA"
    sorted_hand = sorted(hand, key=lambda card: values.index(card))
    return tuple(sorted_hand)

def sort_hands(mains):
    """Sort the hands based on the rules."""
    hand_types = {
        'Five of a kind': 0,
        'Four of a kind': 1,
        'Full house': 2,
        'Three of a kind': 3,
        'Two pair': 4,
        'One pair': 5,
        'High card': 6,
    }

    def hand_key(hand):
        """Generate a key for sorting based on hand type and card values."""
        values = "23456789TJQKA"
        card_counts = {card: hand.count(card) for card in set(hand)}
        sorted_counts = sorted(card_counts.items(), key=lambda x: (x[1], values.index(x[0])), reverse=True)
        hand_type = next(hand_type for hand_type, count in hand_types.items() if count in [count for card, count in sorted_counts])
        return hand_types[hand_type], convert_hand(hand)

    sorted_mains = sorted(mains, key=hand_key)
    return sorted_mains

# Example usage:
mains = ["KTJJT", "QQQJA", "KK677", "32T3K", "T55J5"]
sorted_hands = sort_hands(mains)
print(sorted_hands)
