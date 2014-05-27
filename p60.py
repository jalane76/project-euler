#! python

import euler
import math

def get_next_prime(p):
    p = p + 1
    while not euler.is_prime(p):
        p = p + 1
    return p

def main():
    primes = [3]
    current_prime = 5
    log_level = 2

    num_primes = 5
    while len(primes) < num_primes:
        concats_with_all = True
        for p in primes:
            p_1 = int(str(p) + str(current_prime))
            p_2 = int(str(current_prime) + str(p))
            if not euler.is_prime(p_1) or not euler.is_prime(p_2):
                concats_with_all = False
                break
        if concats_with_all:
            primes.append(current_prime)
        current_prime = get_next_prime(current_prime)
        if math.log10(current_prime) > log_level:
            print(10 ** log_level)
            log_level = log_level + 1

    print(primes)
    print(sum(primes))

if __name__ == "__main__":
    main()