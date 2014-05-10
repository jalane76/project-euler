#! python
import sys
import math
import euler
import itertools

def main():
    found_it = False
    j = 2
    D = 0
    while not found_it:
        p_j = euler.pentagonal_number(j)
        for k in range(j - 1, 0, -1):
            p_k = euler.pentagonal_number(k)
            #print(p_j, ', ', p_k)
            if euler.is_pentagonal_number(p_j - p_k) and euler.is_pentagonal_number(p_j + p_k):
                D = math.fabs(p_j - p_k)
                found_it = True
                break
        j += 1
    print(D)

if __name__ == "__main__":
    main()


