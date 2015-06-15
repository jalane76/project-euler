#! python

import time
import itertools
import math
import euler
from decimal import *

def main():
    getcontext().prec = 150
    N = 101
    num_digits = 100
    power = Decimal(0.5)

    total_sum = 0
    for n in range(1, N):
        if not euler.is_square_number(n):
            d = Decimal(n)
            root = d ** power
            digital_sum = euler.digital_sum(root, num_digits)
            print(str(n) + ' : ' + str(digital_sum))
            total_sum += digital_sum
    print(total_sum)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')