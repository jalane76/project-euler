#! python
import sys
import math

def is_evenly_divisible(f, n):
    while f > 0:
        if n % f != 0:
            return False
        f -= 1
    return True

def main():
    f = 20
    n = f
    while True:
        if is_evenly_divisible(f, n):
            break
        n += f

    print(n)
    
if __name__ == "__main__":
    main()
