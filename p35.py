#! python
import sys
import math
import euler

def rotate(s, n):
    return s[n:] + s[:n]

def main():
     primes = []
     for n in range(2, 1000000):
         if euler.is_prime(n):
             is_prime = True
             for i in range(len(str(n))):
                 p = int(rotate(str(n)[:], i))
                 if not euler.is_prime(p):
                     is_prime = False
                     break
             if (is_prime):
                primes.append(n)
     print(primes)
     print(len(primes))

if __name__ == "__main__":
    main()


