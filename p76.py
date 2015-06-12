#! python

import time
import itertools
import euler

def main():
    print(euler.get_2_term_summations(7))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')