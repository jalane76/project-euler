#! python

import time
import math
import euler


def main():

    M = 5010
    P = math.sqrt(M)
    P = math.ceil(P)
    factors = [x for x in range(2, P) if euler.is_prime(x)]
    factors.sort(reverse=True)
    print(factors)
    num_solutions = 0
    for x in factors:
        for y in factors:
            for z in factors:
                n = math.pow(x, 2) + math.pow(y, 3) + math.pow(z, 4)
                if n < M:
                    num_solutions += 1
    print(num_solutions)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')
