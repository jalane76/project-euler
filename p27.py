#! python
import sys
import math
import euler

def main():
    max_primes = 0
    max_product = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            stop = False
            while not stop:
                value = n ** 2 + a * n + b
                if not euler.is_prime(value):
                    stop = True
                n += 1
            if n > max_primes:
                max_primes = n
                max_product = a * b
    print('maximum product = ', max_product)

if __name__ == "__main__":
    main()


