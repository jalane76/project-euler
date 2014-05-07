#! python
import sys
import math
import euler

# I think I might be able to prove either a bound of 9! or that n has less than 7 digits

def main():
    total = 0
    for n in range(3, 100000):
        fac_sum = 0
        for i in str(n):
            fac_sum += math.factorial(int(i))
        if n == fac_sum:
            total += n
            print(n)
    print('total = ', total)

if __name__ == "__main__":
    main()


