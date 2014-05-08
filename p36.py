#! python
import sys
import math
import euler

def main():
    total = 0
    for n in range(1000000):
        if euler.is_palindrome(str(n)) and euler.is_palindrome("{0:b}".format(n)):
            total += n
    print(total)

if __name__ == "__main__":
    main()


