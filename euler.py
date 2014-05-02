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
    for i in range(5, int(n ** 0.5) + 1, 6):   
        if not n % i or not n % (i + 2):
            return False
    return True
    
def factors(n):     #Fix this to be more robust
    if n == 1:
        factors = [1]
    else:
        factors = [1, n]
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            factors.append(i)
            if i != int(n / i):
                factors.append(int(n / i))
    factors.sort()
    return factors

def even_divisors(n):   #Fix this to be more robust
    divisors = factors(n)
    del divisors[-1]
    return divisors

def is_perfect_number(n):
    return sum(even_divisors(n)) == n

def is_deficient_number(n):
    return sum(even_divisors(n)) < n

def is_abundant_number(n):
    return sum(even_divisors(n)) > n

def is_sum_of_two_abundant_numbers(n, abundants):
    if n < 24:
        return False
    if n > 28123:
        return True
    a = abundants[0]
    for a in abundants:
        if a > int(n / 2):
            return False
        if is_abundant_number(n - a):
            return True
    return False

def collatz_sequence(n):
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

def binomial_coefficient(n, k):
    numerator = 1
    for i in range(n - k + 1, n + 1):
        numerator *= i
    return int(numerator / math.factorial(k))
