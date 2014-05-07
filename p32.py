#! python
import sys
import math
import euler
import itertools

def main():
    digits = '123456789'
    products = []
    permutations = itertools.permutations(digits, len(digits))
    for p in permutations:
        for m1 in range(1, len(digits) - 1):
            for m2 in range(m1 + 1, len(digits)):
                multiplicand = int(''.join(p[:m1]))
                multiplier = int(''.join(p[m1:m2]))
                product = int(''.join(p[m2:]))
                if multiplicand * multiplier == product:
                        products.append(product)
    products = set(products)
    total = sum(products)
    print(total)

if __name__ == "__main__":
    main()


