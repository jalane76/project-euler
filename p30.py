#! python
import sys
import math
import euler

def main():
    p = 5
    sum = 0
    for n in range(2, p * (9 ** p)):
        num_sum = 0
        for d in str(n):
            num_sum += int(d) ** p
        if n == num_sum:
            sum += n
            print(n)
    print(sum)

if __name__ == "__main__":
    main()


