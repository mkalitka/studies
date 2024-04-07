from itertools import combinations

# suits: S - spades, H - hearts, D - diamonds, C - clubs
# hand are sorted by value, then by suit

def straight_flush(hand):
    if flush(hand) and straight(hand):
        return True
    return False

def four_of_a_kind(hand):
    if hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0]:
        return True
    if hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]:
        return True
    return False

def full_house(hand):
    if hand[0][0] == hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
        return True
    if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] == hand[4][0]:
        return True
    return False

def flush(hand):
    return hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]

def straight(hand):
    return hand[0][0] + 4 == hand[1][0] + 3 == hand[2][0] + 2 == hand[3][0] + 1 == hand[4][0]

def three_of_a_kind(hand):
    if hand[0][0] == hand[1][0] == hand[2][0]:
        return True
    if hand[1][0] == hand[2][0] == hand[3][0]:
        return True
    if hand[2][0] == hand[3][0] == hand[4][0]:
        return True
    return False

def two_pairs(hand):
    if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
        return True
    if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
        return True
    if hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
        return True
    return False

def one_pair(hand):
    if hand[0][0] == hand[1][0]:
        return True
    if hand[1][0] == hand[2][0]:
        return True
    if hand[2][0] == hand[3][0]:
        return True
    if hand[3][0] == hand[4][0]:
        return True
    return False

def high_card(hand):
    return True

def evaluate_hand(hand):
    if straight_flush(hand):
        return 9
    if four_of_a_kind(hand):
        return 8
    if full_house(hand):
        return 7
    if flush(hand):
        return 6
    if straight(hand):
        return 5
    if three_of_a_kind(hand):
        return 4
    if two_pairs(hand):
        return 3
    if one_pair(hand):
        return 2
    if high_card(hand):
        return 1

class DeckStats():
    def __init__(self, deck):
        self.deck = deck
        self.size = len(deck)
        self.distribution = {}

    def every_hand(self):
        if self.size < 5:
            raise ValueError("Deck is too small")
        
        for hand in combinations(self.deck, 5):
            yield hand

    def find_distribution(self):
        if self.distribution != {}: return 

        for hand in self.every_hand():
            hand = sorted(hand, key=lambda x: x[0])
            hand_value = evaluate_hand(hand)
            if hand_value in self.distribution:
                self.distribution[hand_value] += 1
            else:
                self.distribution[hand_value] = 1
    
SUITS = ['S', 'H', 'D', 'C']    

FIGURANT_VALUES = [11, 12, 13, 14]
FIGURANT_DECK = [(val, suit) for val in FIGURANT_VALUES for suit in SUITS]
FIGURANT_DECK = DeckStats(FIGURANT_DECK)
FIGURANT_DECK.find_distribution()

def count_prob(BLOTKARZ_DECK):
    wins = 0
    for valB in BLOTKARZ_DECK.distribution:
        for valF in FIGURANT_DECK.distribution:
            if valB > valF:
                wins += BLOTKARZ_DECK.distribution[valB] * FIGURANT_DECK.distribution[valF]

    return (wins * 100) / (sum(BLOTKARZ_DECK.distribution.values()) * sum(FIGURANT_DECK.distribution.values()))

def main():
    BLOTKARZ_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    BLOTKARZ_DECK = [(val, suit) for val in BLOTKARZ_VALUES for suit in SUITS]
    BLOTKARZ_DECK = DeckStats(BLOTKARZ_DECK)
    BLOTKARZ_DECK.find_distribution()

    print("Full deck:", count_prob(BLOTKARZ_DECK))

def propositions():
    def proposition1():
        BLOTKARZ_VALUES = [8, 9 , 10]
        BLOTKARZ_DECK = [(val, suit) for val in BLOTKARZ_VALUES for suit in SUITS]
        BLOTKARZ_DECK = DeckStats(BLOTKARZ_DECK)
        BLOTKARZ_DECK.find_distribution()

        print("proposition1", count_prob(BLOTKARZ_DECK))

    def proposition2():
        BLOTKARZ_VALUES = [8, 9 , 10]
        BLOTKARZ_DECK = [(val, suit) for val in BLOTKARZ_VALUES for suit in SUITS]
        BLOTKARZ_DECK.append((7, 'S'))
        BLOTKARZ_DECK = DeckStats(BLOTKARZ_DECK)
        BLOTKARZ_DECK.find_distribution()

        print("proposition2", count_prob(BLOTKARZ_DECK))

    def proposition3():
        BLOTKARZ_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        BLOTKARZ_DECK = [(val, suit) for val in BLOTKARZ_VALUES for suit in ['S']]
        BLOTKARZ_DECK = DeckStats(BLOTKARZ_DECK)
        BLOTKARZ_DECK.find_distribution()

        print("proposition3", count_prob(BLOTKARZ_DECK))


    def proposition4():
        BLOTKARZ_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        BLOTKARZ_DECK = [(val, suit) for val in BLOTKARZ_VALUES for suit in ['S']]
        BLOTKARZ_DECK.append((7, 'H'))
        BLOTKARZ_DECK = DeckStats(BLOTKARZ_DECK)
        BLOTKARZ_DECK.find_distribution()

        print("proposition4", count_prob(BLOTKARZ_DECK))

    def proposition5():
        BLOTKARZ_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        BLOTKARZ_DECK = [(val, suit) for val in BLOTKARZ_VALUES for suit in ['S', 'H']]
        BLOTKARZ_DECK = DeckStats(BLOTKARZ_DECK)
        BLOTKARZ_DECK.find_distribution()

        print("proposition5", count_prob(BLOTKARZ_DECK))

    proposition1()
    proposition2()
    proposition3()
    proposition4()
    proposition5()

if __name__ == "__main__":
    main()
    propositions()
