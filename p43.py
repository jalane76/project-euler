#! python
import sys
import math
import euler
import itertools

def main():
    digits = '0123456789'
    primes = [2, 3, 5, 7, 11, 13, 17]
    total = 0
    for p in itertools.permutations(digits):
        s = ''.join(p)
        is_div = True
        for i in range(1, len(s) - 2):
            n = int(s[i:i + 3])
            if n % primes[i - 1] != 0:
                is_div = False
                break
        if is_div:
            total += int(s)
    print(total)


if __name__ == "__main__":
    main()


