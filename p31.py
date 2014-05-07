#! python
import sys
import math
import euler

def calc(coins, equation, pence):
    if len(coins) == 0:
        if sum(equation) == pence:
            return 1
        else:
            return 0
    else:
        total = 0
        limit = math.ceil((pence - sum(equation)) / coins[0])
        print(limit)
        for i in range(math.ceil((pence - sum(equation)) / coins[0])):
            new_equation = equation.copy()
            new_equation.append(i * coins[0])
            new_coins = coins.copy()[1:]
            total += calc(new_coins, new_equation, pence)
        return total

def main():
    pence = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coins.reverse()
    total = calc(coins, [], pence)
    print(total)

if __name__ == "__main__":
    main()


