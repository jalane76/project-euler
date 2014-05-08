#! python
import sys
import math
import euler

def main():
    i = 1
    s = ''
    num_digits = 1
    total = 1

    n = 10
    while num_digits < n:
        i += 1
        s = str(i)
        num_digits += len(s)
    total *= int(s[n - num_digits - 1])

    n *= 10 #100
    while num_digits < n:
        i += 1
        s = str(i)
        num_digits += len(s)
    total *= int(s[n - num_digits - 1])

    n *= 10 #1000
    while num_digits < n:
        i += 1
        s = str(i)
        num_digits += len(s)
    total *= int(s[n - num_digits - 1])

    n *= 10 #10000
    while num_digits < n:
        i += 1
        s = str(i)
        num_digits += len(s)
    total *= int(s[n - num_digits - 1])

    n *= 10 #100000
    while num_digits < n:
        i += 1
        s = str(i)
        num_digits += len(s)
    total *= int(s[n - num_digits - 1])

    n *= 10 #1000000
    while num_digits < n:
        i += 1
        s = str(i)
        num_digits += len(s)
    total *= int(s[n - num_digits - 1])

    print(total)

if __name__ == "__main__":
    main()


