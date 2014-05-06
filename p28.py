#! python
import sys
import math
import euler

def main():
    begin = 3
    end = 1001
    step = 2
    sum = 1
    for n in range(begin, end + 1, step):
        ne = n ** 2
        nw = ne - n + 1
        sw = nw - n + 1
        se = sw - n + 1
        sum += ne + nw + sw + se
    print(sum)

if __name__ == "__main__":
    main()


