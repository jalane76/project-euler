#! python

import time
import itertools
import euler

def main():
    n = 10
    while euler.prime_partition_count(n, [] , []) < 5000:
        n += 1
    print(n)


if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')