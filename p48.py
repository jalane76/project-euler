#! python
import sys
import math
import euler
import itertools

def main():
    total = 0
    for i in range(1, 1001):
        term = 1
        for j in range(0, i):
            term *= i
            term_str = str(term)
            if len(term_str) > 10:
                term = int(term_str[-10:])
        total += term
        total_str = str(total)
        if len(total_str) > 10:
            total = int(total_str[-10:])
    print(total)

if __name__ == "__main__":
    main()


