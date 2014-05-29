#! python

import euler
import itertools

def is_cyclic(n, m):
    return n != m and str(n)[2:] == str(m)[:2]

def main():
    check_funcs = [euler.is_triangle_number, euler.is_square_number, euler.is_pentagonal_number, euler.is_hexagonal_number, euler.is_heptagonal_number, euler.is_octagonal_number]
    polygonals = [[n for n in range(1000, 10000) if check_func(n)] for check_func in check_funcs]
    polygonals = list(itertools.chain(*polygonals))
    print('There are ', len(polygonals), ' polygonal numbers.')

    cycles = [[p] for p in polygonals]
    for i in range(1, len(check_funcs)):
        new_cycles = []
        for c in cycles:
            for p in polygonals:
                if is_cyclic(c[-1], p):
                    new_cycles = new_cycles + [c + [p]]
        cycles = new_cycles
        print('step ', i, ': ', len(cycles))
    cycles = [sorted(c) for c in cycles if is_cyclic(c[-1], c[0])]
    cycles = {tuple(c) for c in cycles}
    cycles = [list(c) for c in cycles]

    print('There are ', len(cycles), ' unique cycles.')

    poly_cycles = []
    for c in cycles[:]:
        perms = itertools.permutations(c)
        for p in perms:
            if all([f(x) for f, x in zip(check_funcs, p)]):
                poly_cycles.append(c)
                break
    print(poly_cycles)
    print(sum(poly_cycles[0]))

if __name__ == "__main__":
    main()