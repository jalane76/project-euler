#! python

import time
import itertools
import fractions
import euler

import fractions

def main():
    D = 1000000
    target = fractions.Fraction(3, 7)

    closest = euler.nearest_left_reduced_proper_fraction(target, D)
    print(closest.numerator)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')