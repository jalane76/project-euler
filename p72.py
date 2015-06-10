#! python

import time
import itertools
import fractions
import euler

import fractions

def main():
    D = 1000000
    count = 0

    for d in range(2, D + 1):
        count = count + euler.totient(d)

    print(count)


if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')