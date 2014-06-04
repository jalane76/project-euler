#! python

import time
import math
import fractions
import euler

def main():
    n = 100

    # generate sequence for e
    e = [2]
    k = 1
    while len(e) < n:
        e.extend([1, 2 * k, 1])
        k += 1
    convergents = euler.calc_convergents_with_sequence(e)
    convergent = convergents[99]
    sum_digits = sum([int(c) for c in str(convergent.numerator)])
    print(sum_digits)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')