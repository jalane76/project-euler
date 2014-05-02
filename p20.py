#! python
import sys
import math
import euler

def main():
    n = str(math.factorial(100))
    s = 0
    for i in range(len(n)):
        s += int(n[i])

    print(n)
    print(s)

if __name__ == "__main__":
    main()

