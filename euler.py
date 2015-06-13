#! python
import sys
import math
import fractions
import pyprimes

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

def is_relatively_prime(m, n):
    return fractions.gcd(m, n) == 1
    
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

def coprimes_less_than(n):
    if n < 2:
        return []
    if n == 2:
        return [1]
    else:
        coprimes = [1]
        roof = math.ceil(n / 2)
        for i in range(2, roof):
            if is_relatively_prime(i, n):
                coprimes.append(i)
                coprimes.append(n - i)
        coprimes.append(n - 1)
        coprimes.sort()
        return coprimes

def totient(n):
    factors = list(set(pyprimes.factors(n)))
    result = 1
    for p in factors:
        result = result * (1 - (1 / p))
    return round(result * n)

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

factorial_digit_values = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def factorial_sum_of_digits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum = sum + factorial_digit_values[int(i)]
    return sum

factorial_sum_chain_loop_values = {0 : 0,
                                   1 : 0,
                                   2 : 0,
                                   145 : 0,
                                   169 : 2,
                                   363601 : 2,
                                   1454 : 2,
                                   871 : 1,
                                   45361 : 1,
                                   872 : 1,
                                   45362 : 1}

def factorial_sum_chain_size(n):
    num_terms = 1
    previous_n = -1
    while n not in factorial_sum_chain_loop_values and previous_n != n:
        previous_n = n
        n = factorial_sum_of_digits(n)
        num_terms = num_terms + 1
    if n in factorial_sum_chain_loop_values:
        num_terms = num_terms + factorial_sum_chain_loop_values[n]
    return num_terms

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

def partition_function(n, memory):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    if memory is None or len(memory) == 0:
        memory = [0] * (n + 1)
    result = 0
    for k in range(1, n + 1):
        m = (-1) ** (k + 1)

        n_1 = n - int((3 * k * k - k) / 2)
        p_1 = 0
        if n_1 < 0 or memory[n_1] == 0:
            p_1 = partition_function(n_1, memory)
        else:
            p_1 = memory[n_1]

        n_2 = n - int((3 * k * k + k) / 2)
        p_2 = 0
        if n_2 < 0 or memory[n_2] == 0:
            p_2 = partition_function(n_2, memory)
        else:
            p_2 = memory[n_2]
        result = result + m * (p_1 + p_2)
    if memory[n] == 0:
        memory[n] = result
    return result

#  These next three functions take up too much space
def summations(n):
    summations = get_2_term_summations(n)
    for summation in summations:
        summations.extend(expand_summation(summation))
    unique = []
    for s in summations:
        if s not in unique:
            unique.append(s)
    return unique

def expand_summation(summation):
    index = len(summation) - 1
    while summation[index] == 1 and index >= 0:
        index = index - 1
    if index == 0 and summation[index] == 1:
        return [summation]

    two_terms = get_2_term_summations(summation[index])
    new_summations = []
    for terms in two_terms:
        new_summation = summation[:index] + terms + summation[index + 1:]
        new_summations.append(new_summation)
    return new_summations

def get_2_term_summations(n):
    if n < 2:
        return []
    summations = []
    for i in range(math.ceil(n / 2), n):
        summations.append([i, n - i])
    return summations

def min_num_binary_nodes(n):
    if n <= 1:
        return 0
    return min_num_binary_nodes(n - 1) + min_num_binary_nodes(math.floor(n/2)) + 1

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

# Fractions

def nearest_left_reduced_proper_fraction(target, max_denominator):
    target_value = float(target)
    closest = fractions.Fraction(0, 1)
    min_distance = 1

    for d in range(2, max_denominator + 1):
        n = math.floor(d * target_value)
        frac = fractions.Fraction(n, d)
        while frac.numerator != n and n >= 1:
            n = n - 1
            frac = fractions.Fraction(n, d)
        distance = target_value - float(frac)
        if distance < min_distance and frac != target:
            min_distance = distance
            closest = frac
    return closest

def count_fractions_in_range(min_limit, max_limit, D):
    min_value = float(min_limit)
    max_value = float(max_limit)
    count = 0
    for d in range(2, D + 1):
        n_min = math.ceil(d * min_value)
        n_max = math.floor(d * max_value)
        for n in range(n_min, n_max + 1):
            if n != min_limit.numerator and n != max_limit.numerator and d != min_limit.denominator and d != max_limit.denominator and is_relatively_prime(n, d):
                count = count + 1
    return count

# Triangles

def generate_up_triple(seed_triple):
    a = seed_triple[0]
    b = seed_triple[1]
    c = seed_triple[2]
    return (a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c)

def generate_along_triple(seed_triple):
    a = seed_triple[0]
    b = seed_triple[1]
    c = seed_triple[2]
    return (a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c)

def generate_down_triple(seed_triple):
    a = seed_triple[0]
    b = seed_triple[1]
    c = seed_triple[2]
    return (-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c)

def generate_triple_multiple(triple, m):
    return (triple[0] * m, triple[1] * m, triple[2] * m)

def generate_pythagorean_perimeters_less_than(seed_triple, max_perimeter):
    perimeters = []
    L = sum(seed_triple)
    if L > max_perimeter:
        return perimeters

    perimeters.append(L)
    m = 2
    m_triple = generate_triple_multiple(seed_triple, m)
    L_m = sum(m_triple)
    while L_m <= max_perimeter:
        perimeters.append(L_m)
        m = m + 1
        m_triple = generate_triple_multiple(seed_triple, m)
        L_m = sum(m_triple)

    up = generate_up_triple(seed_triple)
    along = generate_along_triple(seed_triple)
    down = generate_down_triple(seed_triple)

    perimeters.extend(generate_pythagorean_perimeters_less_than(up, max_perimeter))
    perimeters.extend(generate_pythagorean_perimeters_less_than(along, max_perimeter))
    perimeters.extend(generate_pythagorean_perimeters_less_than(down, max_perimeter))

    return perimeters

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

class NGonRing:
    __nodes = []
    node_count = 0
    n = 0

    def __init__(self, nodes):
        self.__nodes = nodes
        self.node_count = len(nodes)
        self.n = int(self.node_count / 2)
        if self.n % 2 != 1 or self.n < 3:
            raise ValueError('Incorrect number of nodes to create an n-gon')

    def __eq__(self, other):
        return self.get_all_groups() == other.get_all_groups()

    def __hash__(self):
        return sum(self.__nodes)

    def get_group(self, i):
        j = i + self.n
        if i == self.n - 1:
            k = self.n
        else:
            k = i + self.n + 1
        return (self.__nodes[i], self.__nodes[j], self.__nodes[k])

    def get_all_groups(self):
        min_index = 0
        for i in range(0, self.n):
            if self.__nodes[i] < self.__nodes[min_index]:
                min_index = i

        groups = []
        for i in range(0, self.n):
            groups.append(self.get_group((i + min_index) % self.n))
        return groups

    def is_magic(self):
        groups = self.get_all_groups()
        S = sum(groups[0])
        for g in groups[1:]:
            if sum(g) != S:
                return False
        return True

    def total(self):
        if self.is_magic():
            return sum(self.get_group(0))
        else:
            return 0

    def magic_string(self):
        return ''.join([''.join(map(str, g)) for g in self.get_all_groups()])
