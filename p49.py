#! python
import sys
import math
import euler
import itertools

def main():
    result = ''
    for n in range(1488, 10000):
        n_2 = n + 3330
        n_3 = n + 2 * 3330
        if euler.is_prime(n) and euler.is_prime(n_2) and euler.is_prime(n_3):
            n_str = str(n)
            n_2_str = str(n_2)
            n_3_str = str(n_3)
            perms = [''.join(p) for p in itertools.permutations(n_str)]
            if n_2_str in perms and n_3_str in perms:
                result = n_str + n_2_str + n_3_str
                break
    print(result)

if __name__ == "__main__":
    main()


