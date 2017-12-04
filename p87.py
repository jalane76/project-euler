#! python

import time
import math
import euler


def main():

    M = 50000000
    P = math.sqrt(M)
    P = math.floor(P)
    factors = [x for x in range(2, P) if euler.is_prime(x)]
    print(factors)
    solutions = []
    for x in factors:
        x2 = math.pow(x, 2)
        if x2 < M:
            for y in factors:
                y3 = math.pow(y, 3)
                if x2 + y3 < M:
                    for z in factors:
                        z4 = math.pow(z, 4)
                        n = x2 + y3 + z4
                        if n < M:
                            solutions.append(n)
    solutions = set(solutions)
    print(len(solutions))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')
