#! python
import sys
import math
import euler
import itertools

def char_to_num(c):
    return ord(c) - 64

def alphabetical_value(word):
    return sum([char_to_num(c) for c in word])

def main():
    words = []
    with open('words.txt') as f:
        words = f.read().replace('\n', '')

    words = words.replace('\"', '')
    words = words.split(',')

    total = 0
    for word in words:
        n = alphabetical_value(word)
        t = (2 * n) ** 0.5
        top = math.ceil(t)
        bottom = math.floor(t)
        if euler.triangle_number(top) == n or euler.triangle_number(bottom) == n:
            print(word, ': ', n)
            total += 1
    print(total)

if __name__ == "__main__":
    main()


