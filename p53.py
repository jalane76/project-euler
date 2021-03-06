#! python
import sys
import math
import euler

def main():
    count = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if euler.binomial_coefficient(n, r) > 1000000:
                count += 1
    print(count)

if __name__ == "__main__":
    main()


