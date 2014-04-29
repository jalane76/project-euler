#! python
import sys
import math
import euler

def main():
    num_factors = 500
    i = 1
    n = 1
    
    factors = euler.factors(n)
    while len(factors) < num_factors:
        i += 1
        n += i
        factors = euler.factors(n)
    
    print(n)

if __name__ == "__main__":
    main()
