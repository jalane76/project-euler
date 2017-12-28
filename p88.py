#! python

import time
from datetime import timedelta
import math
import euler
from collections import Counter
from operator import mul
from functools import reduce

def main():

    # bounds
    k_max = 6 # this also happens to be as large as any coordinate in a sum/product can be
    v = 2 * k_max # this is the largest that any of the sums/products can be
    b = k_max - 1 - math.ceil(math.log(k_max)) # this is the lower bound on the number of ones in the solution
    print(k_max - b)

    # solve k_max case directly to get upper bound
    min_sum = math.inf


    #N_max = [1] * k_max
    #while sum(N_max) != reduce(mul, N_max, 1):


    min_sums = {}

    # get the prime factorizations of all the possible sums below the bound
    prime_facs = [euler.prime_factorization(i) for i in range(2, v + 1)]
    mults = [Counter(facs).most_common() for facs in prime_facs]
    for m in mults:
        count_sum = sum([p[1] for p in m])
        N = reduce(mul, [p[0] ** p[1] for p in m], 1)
        m = N - sum([p[0] * p[1] for p in m])
        k = m + count_sum
        if k > 1 and N <= 2 ** (k_max - b):
            if k not in min_sums or N < min_sums[k]:
                min_sums[k] = N

    min_sums = set(min_sums.values())
    print(prime_facs)
    print(mults)
    print(min_sums)
    print(sum(min_sums))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', str(timedelta(seconds=(time.time() - start))))