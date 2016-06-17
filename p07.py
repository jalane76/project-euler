#! python
import sys
import math

def is_prime(n):
    root = math.floor(math.sqrt(n))
    f = 2
    while f <= root:
        if n % f == 0:
            return False
        f += 1
    return True

def main():
    prime = 0
    i = 2
    counter = 0
    
    while counter < 10001:
        if is_prime(i):
            prime = i
            counter += 1 
        i += 1

    print(prime)
    
if __name__ == "__main__":
    main()
