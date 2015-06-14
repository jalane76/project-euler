#! python

import time
import itertools
import euler

def main():
    n = 5
    count = euler.integer_partition_count_2(n)
    while count % 1000000 != 0:
        if n % 100 == 0:
            print(str(n) + ' : ' + str(count))
        n += 1
        count = euler.integer_partition_count_2(n)
    print(n)
    print(count)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')