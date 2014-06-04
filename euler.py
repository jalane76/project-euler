#! python
import sys
import math
import fractions

# Primes and factoring

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

def prime_factors(n):
    return [i for i in factors(n) if is_prime(i)]

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

def is_sum_of_prime_and_twice_square(n):
    max_square = math.floor((0.5 * n) ** 0.5)
    for i in range(max_square, 0, -1):
        p = n - 2 * i * i
        if is_prime(p):
            return True
    return False


# String-like operations on numbers

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

def rotate_right(n, r):
    return int(str(n)[-r:] + str(n)[:-r])

def rotate_left(n, r):
    return int(str(n)[r:] + str(n)[:r])

def is_permutation(n, m):
    return sorted(list(str(n))) == sorted(list(str(m)))

# Sequences and counting

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

def fibonacci(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return math.floor((golden_ratio ** n) / (5 ** 0.5) + 0.5)

def fibonacci(f_n1, f_n2):
    return f_n1 + f_n2

def root_continued_fraction_sequence(n):
    def process_term(n, term):
        whole_term = term[0]
        numerator = term[2]
        denominator = term[1]

        new_whole_term = 0
        new_numerator =  -denominator
        new_denominator = int((n - denominator ** 2) / numerator)
        while new_numerator - new_denominator >= -math.floor(n ** 0.5):
            new_numerator -= new_denominator
            new_whole_term += 1
        return (new_whole_term, new_numerator, new_denominator)

    first_term = math.floor(n ** 0.5)
    sequence = [first_term]
    if square_number(first_term) == n:
        return sequence

    terms = []
    term = process_term(n, (first_term, -first_term, 1))
    while term not in terms:
        terms.append(term)
        term = process_term(n, term)
    sequence.append([t[0] for t in terms])
    return sequence

def next_continued_fraction_convergent(b, A_n1, A_n2, B_n1, B_n2):
    return fractions.Fraction(b * A_n1 + A_n2, b * B_n1 + B_n2)

def calc_convergents_with_sequence(s):
    convergents = [fractions.Fraction(s[0], 1)]
    A_n1 = s[0]
    A_n2 = 1
    B_n1 = 1
    B_n2 = 0
    for b in s[1:]:
        convergent = next_continued_fraction_convergent(b, A_n1, A_n2, B_n1, B_n2)
        convergents.append(convergent)
        A_n2 = A_n1
        B_n2 = B_n1
        A_n1 = convergent.numerator
        B_n1 = convergent.denominator
    return convergents

def calc_convergents_with_repeating_sequence(s, n):
    convergents = [fractions.Fraction(s[0], 1)]
    repeated_sequence = s[1]
    A_n1 = s[0]
    A_n2 = 1
    B_n1 = 1
    B_n2 = 0
    for i in range(0, n):
        b = repeated_sequence[i % len(repeated_sequence)]
        convergent = next_continued_fraction_convergent(b, A_n1, A_n2, B_n1, B_n2)
        convergents.append(convergent)
        A_n2 = A_n1
        B_n2 = B_n1
        A_n1 = convergent.numerator
        B_n1 = convergent.denominator
    return convergents

def find_fundamental_pell_solution(d):
    s = root_continued_fraction_sequence(d)
    convergent = fractions.Fraction(s[0], 1)
    repeated_sequence = s[1]
    A_n1 = s[0]
    A_n2 = 1
    B_n1 = 1
    B_n2 = 0
    i = 0
    while convergent.numerator ** 2 - d * convergent.denominator ** 2 != 1:
        b = repeated_sequence[i % len(repeated_sequence)]
        convergent = next_continued_fraction_convergent(b, A_n1, A_n2, B_n1, B_n2)
        A_n2 = A_n1
        B_n2 = B_n1
        A_n1 = convergent.numerator
        B_n1 = convergent.denominator
        i += 1
    return (convergent.numerator, convergent.denominator)

# Polygonal or figurative numbers

def triangle_number(n):
    return int(0.5 * n * (n + 1))

def is_triangle_number(n):
    if n < 1:
        return False
    m = (2 * n) ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return triangle_number(top) == n or triangle_number(bottom) == n

def square_number(n):
    return int(n ** 2)

def is_square_number(n):
    if n < 1:
        return False
    m = n ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return n == square_number(top) or n == square_number(bottom)

def pentagonal_number(n):
    return int(0.5 * n * (3 * n - 1))

def is_pentagonal_number(n):
    if n < 1:
        return False
    m = (2 * n / 3) ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return pentagonal_number(top) == n or pentagonal_number(bottom) == n

def hexagonal_number(n):
    return int(n * (2 * n - 1))

def is_hexagonal_number(n):
    if n < 1:
        return False
    m = (n * 0.5) ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return hexagonal_number(top) == n or hexagonal_number(bottom) == n

def heptagonal_number(n):
    return int(n * (5 * n - 3) * 0.5)

def is_heptagonal_number(n):
    if n < 1:
        return False
    m = (2 * n / 5) ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return heptagonal_number(top) == n or heptagonal_number(bottom) == n

def octagonal_number(n):
    return int(n * (3 * n - 2))

def is_octagonal_number(n):
    if n < 1:
        return False
    m = (n / 3) ** 0.5
    top = math.ceil(m)
    bottom = math.floor(m)
    return octagonal_number(top) == n or octagonal_number(bottom) == n

def cubic_number(n):
    return n ** 3

def is_cubic_number(n):
    if n < 1:
        return False
    m = n ** (1 / 3)
    top = math.ceil(m)
    bottom = math.floor(m)
    return n == cubic_number(top) or n == cubic_number(bottom)


# List helpers

def product(list):
    p = 1
    for n in list:
        p *= n
    return p


# Unit fraction class

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