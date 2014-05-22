#! python
import sys
import math
import euler

def main():
    x = 1

    while True:
        s = ''.join(sorted(str(x)))
        multiples = []
        for c in range(2, 7):
            multiples.append(''.join(sorted(str(c * x))))
        if all(t == s for t in multiples):
            break

        x += 1
    print(x)

if __name__ == "__main__":
    main()


