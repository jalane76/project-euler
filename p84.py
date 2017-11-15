#! python

import time
import random
import math

def main():
    board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL',
             'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP',
             'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J',
             'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

    visit_count = [0] * len(board)
    chest = ['GO', 'JAIL', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY']
    chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'NEXTR', 'NEXTR', 'NEXTU', 'BACK3', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY']

    die_limits = (1, 4)
    chance_round_ends = 0.01
    min_rolls = 1000

    num_rounds = 10000

    for round in range(0, num_rounds):
        # shuffle decks
        random.shuffle(chest)
        random.shuffle(chance)

        # reset indices
        roll_count = 0
        double_count = 0
        player_pos = 0
        chest_index = 0
        chance_index = 0

        continue_round = True

        while continue_round:
            # roll dice
            die1 = random.randint(die_limits[0], die_limits[1])
            die2 = random.randint(die_limits[0], die_limits[1])
            roll_count += 1

            # check for doubles
            if die1 == die2:
                double_count += 1
            else:
                double_count = 0

            # if third double, go to jail
            if double_count == 3:
                double_count = 0
                player_pos = board.index('JAIL')
                visit_count[player_pos] += 1
                continue

            # move player according to dice roll
            player_pos = (player_pos + die1 + die2) % len(board)

            # check if player landed on go to jail
            if board[player_pos] == 'G2J':
                player_pos = board.index('JAIL')
                visit_count[player_pos] += 1
                continue

            # check if player landed on community chest and deal with it
            if board[player_pos] in ['CC1', 'CC2', 'CC3']:
                card = chest[chest_index]
                chest_index = (chest_index + 1) % len(chest)
                if card in ['GO', 'JAIL']:
                    player_pos = board.index(card)
                visit_count[player_pos] += 1
                continue

            # check if player landed on chance and deal with it
            if board[player_pos] in ['CH1', 'CH2', 'CH3']:
                card = chance[chance_index]
                chance_index = (chance_index + 1) % len(chance)
                if card in ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1']:
                    player_pos = board.index(card)
                elif card == 'NEXTR':
                    while board[player_pos] not in ['R1', 'R2', 'R3', 'R4']:
                        player_pos = (player_pos + 1) % len(board)
                elif card == 'NEXTU':
                    while board[player_pos] not in ['U1', 'U2']:
                        player_pos = (player_pos + 1) % len(board)
                elif card == 'BACK3':
                    player_pos -= 3
                visit_count[player_pos] += 1
                continue

            # we didn't hit any of the special conditions so update count
            visit_count[player_pos] += 1

            # end round?
            if roll_count >= min_rolls and random.random() < chance_round_ends:
                continue_round = False;

    # done simulating, now calculate statistics
    visit_sum = sum(visit_count)
    max1 = (visit_count.index(max(visit_count)), max(visit_count))
    visit_count[max1[0]] = 0
    max2 = (visit_count.index(max(visit_count)), max(visit_count))
    visit_count[max2[0]] = 0
    max3 = (visit_count.index(max(visit_count)), max(visit_count))
    #print(board[max1[0]], ' ', max1[1] / visit_sum * 100, '%')
    #print(board[max2[0]], ' ', max2[1] / visit_sum * 100, '%')
    #print(board[max3[0]], ' ', max3[1] / visit_sum * 100, '%')

    modal1 = str(max1[0]).zfill(2);
    modal2 = str(max2[0]).zfill(2);
    modal3 = str(max3[0]).zfill(2);

    print(modal1 + modal2 + modal3)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')
