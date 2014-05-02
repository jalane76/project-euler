#! python
import sys
import math
import euler

def char_to_num(c):
    return ord(c) - 64

def alphabetical_value(name):
    return sum([char_to_num(c) for c in name])

def main():
    names = ''
    with open('names.txt') as f:
        names = f.read().replace('\n', '')

    names = names.replace('\"', '')
    names = names.split(',')
    names.sort()

    total = 0
    for i in range(len(names)):
        total += (i + 1) * alphabetical_value(names[i])

    print(total)

if __name__ == "__main__":
    main()

