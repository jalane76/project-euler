#! python

import time
import itertools
import euler

def main():
    N = 1000000
    max_ratio = 0
    max_n = 0

    for n in range(2, N + 1):
        ratio = n / euler.totient(n)
        if ratio > max_ratio:
            max_ratio = ratio
            max_n = n

    print(max_n)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')