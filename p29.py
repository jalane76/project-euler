#! python
import sys
import math
import euler

def main():
    terms = []
    for a in range(2, 101):
        for b in range(2, 101):
            terms.append(a ** b)
    terms.sort()
    terms = set(terms)
    print(len(terms))

if __name__ == "__main__":
    main()


