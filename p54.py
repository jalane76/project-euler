#! python
import poker

def main():
    rounds = []
    with open('poker-test.txt') as f:
        for line in f:
            cards = line.split()
            round = (poker.Hand(cards[:5]), poker.Hand(cards[5:]))
            rounds.append(round)

    wins = 0
    for r in rounds:
        s1 = r[0].get_rank()
        s2 = r[1].get_rank()
        if s1 > s2:
            wins += 1
            continue
        elif s1 < s2:
            continue
        else:
            if s1 == 9 or s1 == 6 or s1 == 5 or s1 == 1:   # high card alone can win these hands
                h1 = r[0].get_high_card().value
                h2 = r[1].get_high_card().value
                if h1 > h2:
                    wins += 1
            elif s1 == 8 or s1 == 4:
                


if __name__ == "__main__":
    main()


