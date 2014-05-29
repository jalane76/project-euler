#! python

import euler
import math
import itertools
import time

def main():
    p = 1
    powerful_numbers = []

    done = False
    while not done:
        # generate all of the p-digit powers
        n = 1
        powers = []
        while len(str(n ** p)) < p:
            n += 1
        while len(str(n ** p)) == p:
            powers.append(n ** p)
            n += 1

        if powers:
            powerful_numbers.extend(powers)
            p += 1
        else:
            done = True
    print(powerful_numbers)
    print(len(powerful_numbers))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')