#! python

import euler
import operator

def is_cyclic(n, m):
    return n != m and str(n)[2:] == str(m)[:2]

def main():
    #check_funcs = [euler.is_triangle_number, euler.is_square_number, euler.is_pentagonal_number, euler.is_hexagonal_number, euler.is_heptagonal_number, euler.is_octagonal_number]
    check_funcs = [euler.is_triangle_number, euler.is_square_number, euler.is_pentagonal_number]
    polygonals = [[n for n in range(1000, 10000) if check_func(n)] for check_func in check_funcs]
    S = [[p] for p in polygonals[0]]
    for i in range(1, len(polygonals)):
        new_S = []
        polys = polygonals[i]
        for s in S:
            for p in polys:
                if is_cyclic(s[-1], p):
                    new_S = new_S + [s + [p]]
        S = new_S
    S = [s for s in S if is_cyclic(s[-1], s[0])]
    print(S)

if __name__ == "__main__":
    main()