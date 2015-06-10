#! python

import time
import itertools
import euler

def main():
    N = 10000000
    min_ratio = N
    min_n = 2

    for n in range(2, N):
        t = euler.totient(n)
        if euler.is_permutation(n, t):
            ratio = n / t
            if ratio < min_ratio:
                min_ratio = ratio
                min_n = n

    print(min_n)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')