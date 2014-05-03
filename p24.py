#! python
import sys
import math
import euler

def permute(head, tail, counter, limit):
    if not tail:
        counter += 1
        if counter >= limit:
            print(counter, ': ', ''.join([str(i) for i in head]))
            exit()
    else:
        for d in tail:
            h = head.copy()
            h.append(d)
            t = tail.copy()
            t.remove(d)
            counter = permute(h, t, counter, limit)
    return counter

def main():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    permute([], digits, 0, 1000000)

if __name__ == "__main__":
    main()
