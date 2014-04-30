#! python
import sys
import math
import euler

def main():
    s = str(2**1000)
    sum = 0
    for d in s:
        sum += int(d)

    print(sum)

if __name__ == "__main__":
    main()
