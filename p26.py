#! python
import sys
import math
import euler

def main():
    max_length = 0
    max_d = 0
    for d in range(2, 1000):
        frac = euler.UnitFraction(d)
        if len(frac.repeated_sequence) > max_length:
            max_length = len(frac.repeated_sequence)
            max_d = d

    print('max_d = ', max_d)
    print('max_length = ', max_length)

if __name__ == "__main__":
    main()

