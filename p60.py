#! python

import euler
import itertools

def main():
    # primes = [3, 7, 109, 673, 129976621]
    primes = []
    upper_bound = 150
    num_primes = 5

    for n in range(1, upper_bound):
        if euler.is_prime(n):
            primes.append(n)

    # build up a list of unique pairs of primes and concatenate to primes
    combos = itertools.combinations(primes, 2)
    pairs = []
    for pair in combos:
        p_1 = int(str(pair[0]) + str(pair[1]))
        p_2 = int(str(pair[1]) + str(pair[0]))
        if euler.is_prime(p_1) and euler.is_prime(p_2):
            pairs.append(pair)

    pairs = [sorted(list(p)) for p in pairs]
    pairs = {tuple(p) for p in pairs}
    pairs = [set(p) for p in pairs]



if __name__ == "__main__":
    main()