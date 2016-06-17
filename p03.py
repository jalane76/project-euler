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
    num = 600851475143
    
    # We only need to test up to the square root of the number
    rootNum = math.floor(math.sqrt(600851475143))
    
    # Start with a factor of 2
    f = 2
    
    factors = []
    # Find all of the factors of num
    while f <= rootNum:
        if num % f == 0:
            factors.append(f)
        f += 1
        
    # Reverse the list to put it in descending order
    factors.reverse()
    
    # Print out the largest prime factor
    for factor in factors:
        if is_prime(factor):
            print(factor)
            break    
    
if __name__ == "__main__":
    main()
