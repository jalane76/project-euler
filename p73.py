#! python

import time
import itertools
import fractions
import euler

def main():
    D = 12000
    min = fractions.Fraction(1, 3)
    max = fractions.Fraction(1, 2)
    count = euler.count_fractions_in_range(min, max, D)

    print(count)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')