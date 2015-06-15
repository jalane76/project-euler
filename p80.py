#! python

import time
import itertools
import math
import euler
from decimal import *

def main():
    getcontext().prec = 150
    N = 101
    power = Decimal(0.5)

    digital_sum = 0
#    for n in range(1, N):
#        d = Decimal(n)
#        root = d ** power
#        s = str(root).split('.')[1]
#        digital_sum += sum([int(c) for c in s])

#    print(digital_sum)
    n = 2
    d = Decimal(n)
    print(d)
    root = d ** power
    print(root)
    s = str(root).split('.')[1]
    print(str(len(s)) + ' : ' + s)
    digital_sum += sum([int(c) for c in s][:101])

    print(digital_sum)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')