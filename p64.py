#! python

import time
import math
import euler

def generate_sequence(n):
    first_term = math.floor(n ** 0.5)
    sequence = [first_term]
    if euler.square_number(first_term) == n:
        return sequence

    terms = []
    term = process_term(n, (first_term, -first_term, 1))
    while term not in terms:
        terms.append(term)
        term = process_term(n, term)
    sequence.append([t[0] for t in terms])
    return sequence

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

def main():
    N = 10000
    odd_count = 0
    for n in range(2, N + 1):
        if not euler.is_square_number(n):
            sequence = generate_sequence(n)
            period = len(sequence[1])
            if period % 2 != 0:
                odd_count += 1
    print(odd_count)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')