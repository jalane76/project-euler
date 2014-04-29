#! python
import sys
import math

def is_prime(n):
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
    
