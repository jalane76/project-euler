#! python
import sys
import math
import euler
import itertools

def main():
    n = 286
    is_found = False
    T = 0

    while not is_found:
        t_n = euler.triangle_number(n)
        if euler.is_pentagonal_number(t_n) and euler.is_hexagonal_number(t_n):
            T = t_n
            is_found = True
        n += 1

    print(T)

if __name__ == "__main__":
    main()


