#! python
import sys
import math
import euler
import itertools

def main():
    digits = '123456789'
    max_prime = 0
    for i in range(1, len(digits) + 1):
        for p in itertools.permutations(digits[:i]):
            n = int(''.join(p))
            if euler.is_prime(n) and n > max_prime:
                max_prime = n
    print(max_prime)

if __name__ == "__main__":
    main()


