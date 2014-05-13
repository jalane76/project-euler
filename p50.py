#! python
import sys
import math
import euler
import itertools

def main():
    primes = []
    max_primes = []
    max_prime = 0

    limit = 1000000
    for i in range(1, limit):
        if euler.is_prime(i):
            primes.append(i)

    begin = 0
    end = begin + 1
    while begin < len(primes) - 1 and end < len(primes):
        p = primes[begin:end]
        s = sum(p)
        if s < limit:
            if euler.is_prime(s) and len(p) > len(max_primes):
                max_primes = p
                max_prime = s
            end += 1
        else:
            begin += 1
            end = begin + 1
    print(max_prime)


if __name__ == "__main__":
    main()


