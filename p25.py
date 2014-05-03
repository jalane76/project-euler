#! python
import sys
import math
import euler

def main():
    n = 3
    f_n1 = 1
    f_n2 = 1
    f_n = 2
    while len(str(f_n)) < 1000:
        n += 1
        f_n1 = f_n2
        f_n2 = f_n
        f_n = euler.fibonacci(f_n1, f_n2)

    print(n)

if __name__ == "__main__":
    main()
