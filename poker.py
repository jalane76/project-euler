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

    def __lt__(self, other):
        self_rank = self.__get_rank()
        other_rank = other.__get_rank()
        if self_rank < other_rank:
            return True
        elif self_rank > other_rank:
            return False
        else:
            if self.__is_flush() or self.__is_straight() or self.__is_high_card():
                return self.__get_high_card() < other.__get_high_card()
            if self.__is_four_of_a_kind():
                c1 = self.__get_four_of_a_kinds()[0][0]
                c2 = other.__get_four_of_a_kinds()[0][0]
                return c1 < c2
            if self.__is_full_house() or self.__is_three_of_a_kind():
                c1 = self.__get_three_of_a_kinds()[0][0]
                c2 = other.__get_three_of_a_kinds()[0][0]
                return c1 < c2
            if self.__is_two_pairs():
                p1_high = self.__get_pairs()[0][0]
                p1_low = self.__get_pairs()[1][0]
                if p1_high < p1_low:
                    tmp = p1_high
                    p1_high = p1_low
                    p1_low = tmp

                p2_high = other.__get_pairs()[0][0]
                p2_low = other.__get_pairs()[1][0]
                if p2_high < p2_low:
                    tmp = p2_high
                    p2_high = p2_low
                    p2_low = tmp

                if p1_high < p2_high:
                    return True
                elif p1_high > p2_high:
                    return False
                else:
                    if p1_low < p2_low:
                        return True
                    elif p1_low > p2_low:
                        return False
                    else:
                        h1 = Hand(self.__get_singles())
                        h2 = Hand(other.__get_singles())
                        return h1 < h2
            if self.__is_one_pair():
                p1 = self.__get_pairs()[0][0]
                p2 = other.__get_pairs()[0][0]
                if p1 < p2:
                    return True
                elif p1 > p2:
                    return False
                else:
                    h1 = Hand(self.__get_singles())
                    h2 = Hand(other.__get_singles())
                    return h1 < h2

    def __get_high_card(self):
        high_card = None
        for c in self.cards:
            if high_card is None or c > high_card:
                high_card = c
        return high_card

    def __get_singles(self):
        return [str(p[0]) for p in self.__get_kinds() if len(p) == 1]

    def __get_pairs(self):
        return [p for p in self.__get_kinds() if len(p) == 2]

    def __get_three_of_a_kinds(self):
        return [p for p in self.__get_kinds() if len(p) == 3]

    def __get_four_of_a_kinds(self):
        return [p for p in self.__get_kinds() if len(p) == 4]

    def __get_kinds(self):
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

    def __is_straight(self):
        for i in range(0, len(self.cards) - 1):
            if self.cards[i].value + 1 != self.cards[i + 1].value:
                return False
        return True

    def __is_flush(self):
        for i in range(0, len(self.cards) - 1):
            if not self.cards[i].same_suit(self.cards[i + 1]):
                return False
        return True

    def __is_royal_flush(self):
        return self.__is_straight() and self.__is_flush() and self.__get_high_card().value == 14

    def __is_straight_flush(self):
        return self.__is_straight() and self.__is_flush()

    def __is_four_of_a_kind(self):
        return len(self.__get_four_of_a_kinds()) > 0

    def __is_full_house(self):
        return len(self.__get_three_of_a_kinds()) > 0 and len(self.__get_pairs()) > 0

    def __is_three_of_a_kind(self):
        return len(self.__get_three_of_a_kinds()) > 0 and not self.__is_full_house()

    def __is_two_pairs(self):
        return len(self.__get_pairs()) == 2

    def __is_one_pair(self):
        return len(self.__get_pairs()) == 1 and not self.__is_full_house()

    def __is_high_card(self):
        return len(self.__get_kinds()) == len(self.cards) and not self.__is_straight() and not self.__is_flush()

    def __get_rank(self):
        if self.__is_royal_flush():
            return 10
        if self.__is_straight_flush():
            return 9
        if self.__is_four_of_a_kind():
            return 8
        if self.__is_full_house():
            return 7
        if self.__is_flush():
            return 6
        if self.__is_straight():
            return 5
        if self.__is_three_of_a_kind():
            return 4
        if self.__is_two_pairs():
            return 3
        if self.__is_one_pair():
            return 2
        return 1
