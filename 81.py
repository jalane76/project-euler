#! python

import time
import itertools
import math
import euler
from decimal import *

def main():
    with open('p81_matrix_test.txt') as f:
        matrix = [[int(x) for x in line.split(',')] for line in f]

    path_sum = 0



    print(path_sum)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')