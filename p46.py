#! python
import sys
import math
import euler
import itertools

def main():
    n = 9
    while True:
        if not euler.is_prime(n) and not euler.is_sum_of_prime_and_twice_square(n):
            break;
        n += 2
    print(n)

if __name__ == "__main__":
    main()


