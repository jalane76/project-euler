class Card:
    rank = ''
    suit = ''
    value = 0
    __rep = ''

    def __init__(self, s):
        self.__rep = s
        self.rank = s[:-1]
        self.suit = s[-1]
        self.value = self.__card_to_value(self.rank)

    def __str__(self):
        return self.__rep

    def __repr__(self):
        return self.__rep

    def __lt__(self, other):
        return self.value < other.value

    def __card_to_value(self, c):
        if c == 'T':
            return 10
        elif c == 'J':
            return 11
        elif c == 'Q':
            return 12
        elif c == 'K':
            return 13
        elif c == 'A':
            return 14
        else:
            return int(c)

    def same_rank(self, other):
        return self.value == other.value

    def same_suit(self, other):
        return self.suit == other.suit

class Hand:
    cards = []

    def __init__(self, cards):
        self.cards = cards
        self.cards = [Card(c) for c in cards]
        self.cards = sorted(self.cards)

    def __str__(self):
        return str([str(c) for c in self.cards])

    def __repr__(self):
        return str([str(c) for c in self.cards])

    def get_high_card(self):
        high_card = None
        for c in self.cards:
            if high_card is None or c > high_card:
                high_card = c
        return high_card

    def get_pairs(self):
        return [p for p in self.get_kinds() if len(p) == 2]

    def get_three_of_a_kinds(self):
        return [p for p in self.get_kinds() if len(p) == 3]

    def get_four_of_a_kinds(self):
        return [p for p in self.get_kinds() if len(p) == 4]

    def get_kinds(self):
        kinds = []
        head = 0
        tail = head + 1
        while head != tail and tail < len(self.cards):
            while tail < len(self.cards) and self.cards[head].same_rank(self.cards[tail]):
                tail += 1
            kinds.append(self.cards[head:tail])
            head = tail
            tail = head + 1
        if tail == len(self.cards) and head == tail - 1:
            kinds.append(self.cards[head:tail])
        return kinds

    def is_straight(self):
        for i in range(0, len(self.cards) - 1):
            if self.cards[i].value + 1 != self.cards[i + 1].value:
                return False
        return True

    def is_flush(self):
        for i in range(0, len(self.cards) - 1):
            if not self.cards[i].same_suit(self.cards[i + 1]):
                return False
        return True

    def get_rank(self):
        if self.is_straight() and self.is_flush():
            if self.get_high_card().value == 14:
                return 10 # Royal Flush
            return 9 # Straight Flush
        if len(self.get_four_of_a_kinds()) > 0:
            return 8 # Four of a Kind
        if len(self.get_three_of_a_kinds()) > 0 and len(self.get_pairs()) > 0:
            return 7 # Full House
        if self.is_flush():
            return 6 # Flush
        if self.is_straight():
            return 5 # Straight
        if len(self.get_three_of_a_kinds()) > 0:
            return 4 # Three of a Kind
        if len(self.get_pairs()) > 1:
            return 3 # Two Pairs
        if len(self.get_pairs()) > 0:
            return 2 # One Pair
        return 1
