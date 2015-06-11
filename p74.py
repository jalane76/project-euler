#! python

import time
import itertools
import euler

def main():
    lengths = [0] * 60
    N = 1000000
    sum = 0
    for n in range(3, N):
        length = euler.factorial_sum_chain_size(n)

        if length == 60:
            sum = sum + 1
        elif length > 60:
            print('ERROR: chains should not have more than 60 terms <' + str(n) + ', ' + str(length) + '>')
            exit()
        lengths[length - 1] = lengths[length - 1] + 1
    print(lengths)
    print(sum)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')