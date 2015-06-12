#! python

import time
import itertools
import euler

def main():
    seed = (3, 4, 5)
    L = 1500000
    count = 0

    p_list = euler.generate_pythagorean_perimeters_less_than(seed, L)
    p_list.sort()

    if p_list[0] != p_list[1]:
        count = count + 1
    for i in range(1, len(p_list) - 1):
        if p_list[i - 1] != p_list[i] and p_list[i] != p_list[i + 1]:
            count = count + 1
    if p_list[-2] != p_list[-1]:
        count = count + 1

    print(count)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')