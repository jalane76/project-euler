#! python
import sys

def sum_multiples_below(multiple, limit):
    sum = 0
    n = 0
    while n < limit:
        sum += n
        n += multiple
    return sum

def main():
    sum = sum_multiples_below(3, 1000) + sum_multiples_below(5, 1000) - sum_multiples_below(15, 1000)
    print (sum)

if __name__ == "__main__":
    main()
