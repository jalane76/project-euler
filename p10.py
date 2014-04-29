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
    result = 0
    for i in range(2,2000000):
        if is_prime(i):
            result += i
    print(result)
    
if __name__ == "__main__":
    main()
