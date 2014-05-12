#! python
import sys
import math
import euler
import itertools

def main():
    n = 647
    first_found = 0
    is_found = False
    while not is_found:
        if len(euler.prime_factors(n)) == 4 \
                and len(euler.prime_factors(n + 1)) == 4 \
                and len(euler.prime_factors(n + 2)) == 4 \
                and len(euler.prime_factors(n + 3)) == 4:
            first_found = n
            is_found = True
        n += 1
    print(first_found)

if __name__ == "__main__":
    main()


