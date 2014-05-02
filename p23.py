#! python
import sys
import math
import euler

def main():
    abundants = [x for x in range(12, 28123) if euler.is_abundant_number(x)]
    result = 0
    for x in range(1, 28123):
        if not euler.is_sum_of_two_abundant_numbers(x, abundants):
            result += x

    print(result)

if __name__ == "__main__":
    main()

