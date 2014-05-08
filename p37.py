#! python
import sys
import math
import euler

def is_truncatable_prime(n):
    if not euler.is_prime(n):
        return False
    n = str(n)
    for i in range(1, len(n)):
        left = int(n[i:])
        right = int(n[:-i])
        if not euler.is_prime(left):
            return False
        if not euler.is_prime(right):
            return False
    return True

def main():
    total = 0
    primes = []
    n = 11
    while len(primes) < 11:
        if is_truncatable_prime(n):
            total += n
            primes.append(n)
        n += 1
    print(primes)
    print('total = ', total)

if __name__ == "__main__":
    main()


