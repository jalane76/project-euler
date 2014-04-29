#! python
import sys
import math

def is_prime(n):    #Fix this to be more robust
    if n <= 3:
        if n <= 1:
            return False
        return True
    if not n % 2 or not n % 3:
        return False
    for i in range(5, int(n**0.5) + 1, 6):   
        if not n % i or not n % (i + 2):
            return False
    return True
    
def factors(n):     #Fix this to be more robust
    if n == 1:
        factors = [1]
    else:
        factors = [1, n]
    root = int(n**0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n / i))
    factors.sort()
    return factors
