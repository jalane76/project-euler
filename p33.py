#! python
import sys
import math
import euler
import itertools
import fractions

def main():
    fracs = []
    for numerator in range(10, 99):
        for denominator in range(numerator + 1, 100):
            if not (numerator % 10 == 0 and denominator % 10 == 0):
                original = fractions.Fraction(numerator, denominator)
                n1 = int(numerator / 10)
                n2 = numerator % 10
                d1 = int(denominator / 10)
                d2 = denominator % 10
                new_frac = None
                if n1 == d1 and d2 != 0:
                    new_frac = fractions.Fraction(n2, d2)
                elif n2 == d1 and d2 != 0:
                    new_frac = fractions.Fraction(n1, d2)
                elif n1 == d2 and d1 != 0:
                    new_frac = fractions.Fraction(n2, d1)
                elif n2 == d2 and d1 != 0:
                    new_frac = fractions.Fraction(n1, d1)
                if new_frac and original == new_frac:
                    fracs.append(original)
    product = fractions.Fraction(1, 1)
    print(fracs)
    total = fracs[0] * fracs[1] * fracs[2] * fracs[3]
    print(total.denominator)

if __name__ == "__main__":
    main()


