#! python

import time
import itertools
import euler

def main():
    print(euler.partition_function(100, []) - 1)


if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')