#! python
import poker

def main():
    rounds = []
    with open('poker.txt') as f:
        for line in f:
            cards = line.split()
            round = (poker.Hand(cards[:5]), poker.Hand(cards[5:]))
            rounds.append(round)

    wins = 0
    for r in rounds:
        player1 = r[0]
        player2 = r[1]
        arrow = ''
        winner = ''
        if player1 > player2:
            wins += 1
            arrow = ' > '
            winner = " Player 1"
        else:
            arrow = ' < '
            winner = " Player 2"
        print(player1, arrow, player2, winner)

    print(wins)

if __name__ == "__main__":
    main()