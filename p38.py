#! python
import sys
import math
import euler

def main():
    pandigitals = []
    limit = 100000
    for i in range(1, limit):
        s = str(i)
        n = 2
        while len(s) < 9:
            s = s + str(i * n)
            n += 1
        p = int(s)
        if euler.is_pandigital(p):
            pandigitals.append(p)
    print(pandigitals)
    print(max(pandigitals))

if __name__ == "__main__":
    main()


