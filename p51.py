#! python
import sys
import math
import euler

def main():
    family_size = 8
    smallest_prime = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    is_found = False
    p = 11
    while not is_found:
        if not euler.is_prime(p):
            p += 1
            continue

        s = str(p)
        family = []
        for c in s:
            family.clear()
            for d in digits:
                t = str.replace(s, c, d)
                if len(str(int(t))) == len(str(int(s))):
                    family.append(t)
            family = [int(x) for x in family]
            family = [x for x in family if euler.is_prime(x)]

            if len(family) == family_size:
                smallest_prime = min(family)
                is_found = True
        p += 1

    print(smallest_prime)

if __name__ == "__main__":
    main()


