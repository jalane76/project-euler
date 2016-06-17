#! python
import sys
import math

def main():
    for a in range(1000):
        for b in range(1000):
            for c in range(1000):
                if a * a + b * b == c * c and a + b + c == 1000 and a < b and b < c:
                    print(a * b * c)
                    return
    
if __name__ == "__main__":
    main()
