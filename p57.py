#! python
import fractions

def main():
    c = fractions.Fraction(1, 1)
    count = 0
    for i in range(0, 1000):
        n = c.numerator + 2 * c.denominator
        d = c.numerator + c.denominator
        c = fractions.Fraction(n, d)
        if len(str(c.numerator)) > len(str(c.denominator)):
            count += 1
    print(count)

if __name__ == "__main__":
    main()