#! python

import euler
import itertools

def main():
    # primes = [3, 7, 109, 673, 129976621]
    primes = []
    upper_bound = 10000
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

    print('Starting with ', len(primes), ' primes and ', len(pairs), ' pairs for ', len(primes) * len(pairs), ' operations')

    S = [list(p) for p in pairs]
    for i in range(2, num_primes):
        print('len(S) = ', len(S))
        new_S = []
        for p in primes:
            for s in S:
                concats_all = True
                for n in s:
                    p_1 = int(str(n) + str(p))
                    p_2 = int(str(p) + str(n))
                    if not euler.is_prime(p_1) or not euler.is_prime(p_2):
                        concats_all = False
                        break
                if concats_all:
                    new_S = new_S + [s + [p]]
        S = [sorted(s) for s in new_S]
        S = {tuple(s) for s in S}
        S = [list(s) for s in S]

    print(S)
    print(min([sum(s) for s in S]))


if __name__ == "__main__":
    main()