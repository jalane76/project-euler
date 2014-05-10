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

def is_palindrome(s):
    return s == s[::-1]

def is_pandigital(n):
    n = str(n)
    s = '123456789'
    if len(n) > 9:
        return False
    for d in s[:len(n)]:
        if d not in n:
            return False
    return True


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

def triangle_number(n):
    return int(0.5 * n * (n + 1))

def is_triangle_number(n):
    m = (2 * n) ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return triangle_number(top) == n or triangle_number(bottom) == n

def pentagonal_number(n):
    return int(0.5 * n * (3 * n - 1))

def is_pentagonal_number(n):
    m = (2 * n / 3) ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return pentagonal_number(top) == n or pentagonal_number(bottom) == n

def hexagonal_number(n):
    return n * (2 * n - 1)

def is_hexagonal_number(n):
    m = (n * 0.5) ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return hexagonal_number(top) == n or hexagonal_number(bottom) == n

def fibonacci(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return math.floor((golden_ratio ** n) / (5 ** 0.5) + 0.5)

def fibonacci(f_n1, f_n2):
    return f_n1 + f_n2

class UnitFraction:
    denominator = 1
    remainders = []
    digits = []
    repeated_sequence = []
    __is_generated = False

    def __init__(self, denominator):
        self.denominator = denominator
        self.remainders.clear()
        self.digits.clear()
        self.repeated_sequence.clear()
        self.__is_generated = False

        # DEBUG - temporarily do this here
        self.__generate()

    def get_decimal_representation(self):
        return 1 / self.denominator

    def __generate(self):
        if not self.__is_generated:
            remainder = 1
            while remainder != 0 and self.remainders.count(remainder) <= 1:
                digit = 0
                remainder *= 10
                if remainder >= self.denominator:
                    digit = int(remainder / self.denominator)
                    remainder = remainder % self.denominator
                self.remainders.append(remainder)
                self.digits.append(digit)
            if remainder != 0:
                last_remainder = self.remainders[-1]
                self.remainders = self.remainders[:len(self.remainders) - 1]
                period = len(self.remainders) - self.remainders.index(last_remainder)
                if period > 1:
                    self.digits = self.digits[:len(self.digits) - 1]
                self.repeated_sequence = self.digits[-period:]
            self.__is_generated = True