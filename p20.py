#! python
import sys
import math
import euler

def main():
    n = str(math.factorial(100))
    s = sum([int(i) for i in n])

    print(n)
    print(s)

if __name__ == "__main__":
    main()

