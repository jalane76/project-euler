#! python

import time
import itertools
import euler

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    perms = itertools.permutations(nums)
    n_gons = [euler.NGonRing(p) for p in perms]
    magical_n_gons = list({n for n in n_gons if n.is_magic()})
    strings = [n.magic_string() for n in n_gons]
    strings = [s for s in strings if len(s) == 16]
    print(max(strings))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')