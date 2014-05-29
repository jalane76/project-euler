#! python

import euler
import math
import itertools
import time



def main():
    n = 3
    num_cube_permutations = 5

    is_found = False
    while not is_found:
        N = euler.cubic_number(n)
        num_digits = len(str(N))

        # generate all the cubic numbers with num_digits digits
        cubes = []
        while len(str(N)) <= num_digits:
            cubes.append(N)
            n += 1
            N = euler.cubic_number(n)

        # make a list of lists of permutations
        perms = []
        while cubes:
            c = cubes[0]
            p = [c]
            p.extend([d for d in cubes[1:] if euler.is_permutation(c, d)])
            for x in p:
                cubes.remove(x)
            perms.append(p)
        perms = [p for p in perms if len(p) == num_cube_permutations]
        if perms:
            is_found = True
    print(perms)
    print(min(perms[0]))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')