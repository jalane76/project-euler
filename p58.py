#! python

import euler

def main():
    diagonals = [1]
    primes = []
    ratio = 1
    side_length = 1

    while ratio > 0.1:
        side_length += 2
        new_diags = []
        new_primes = []
        for i in range(0, 4):
            d = (side_length ** 2) - i * (side_length - 1)
            new_diags.append(d)
        new_primes = [p for p in new_diags if euler.is_prime(p)]
        diagonals.extend(new_diags)
        primes.extend(new_primes)
        ratio = len(primes) / len(diagonals)
    print(side_length)

if __name__ == "__main__":
    main()