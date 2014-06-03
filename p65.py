#! python

import time
import math
import fractions
import euler

def continued_fraction(n, i, s):
    if n - 1 == i:
        return fractions.Fraction(1, s[i])
    else:
        return fractions.Fraction(1, s[i] + continued_fraction(n, i + 1, s))

def calc_convergence(n, s):
    fractional = fractions.Fraction(s[0], 1)
    if n > 1:
        fractional += continued_fraction(n, 1, s)
    return fractional

def main():
    n = 100

    # generate sequence for e
    e = [2]
    k = 1
    while len(e) < n:
        e.extend([1, 2 * k, 1])
        k += 1
    convergent = calc_convergence(n, e)
    sum_digits = sum([int(c) for c in str(convergent.numerator)])
    print(sum_digits)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')