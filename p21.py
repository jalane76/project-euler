#! python
import sys
import math
import euler

def main():
    amicable_numbers = []

    for i in range(1, 10000):
        i_divisors = euler.even_divisors(i)
        i_sum = sum(i_divisors)
        j_divisors = euler.even_divisors(i_sum)
        j_sum = sum(j_divisors)
        if i == j_sum and i != i_sum and amicable_numbers.count(i) == 0 and amicable_numbers.count(j_sum) == 0:
            amicable_numbers.extend([i, i_sum])

    print(amicable_numbers)
    print(sum(amicable_numbers))

if __name__ == "__main__":
    main()

