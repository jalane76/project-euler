#! python

import time
import math
import euler

# Definitely needs optimization.  I let it run while I went to lunch.  Took 40 minutes, but did get the right answer.

def calc_path(a):
    return math.sqrt(a[0] * a[0] + a[1] * a[1])

def calc_min_path(faces):
    return min(map(calc_path, faces))

def calc_faces(x, y, z):
    return [(x, y + z), (y, x + z), (z, x + y)]

def main():

    max_paths = 1000000
    over = False

    # initial "seed" guess
    M = 900
    integer_min_count = 0
    for m1 in range(M, 0, -1):
        for m2 in range(m1, 0, -1):
            for m3 in range(m2, 0, -1):
                faces = calc_faces(m1, m2, m3)
                min_path = calc_min_path(faces)
                if min_path.is_integer():
                    integer_min_count += 1


    while not over:
        M += 1
        m1 = M
        for m2 in range(m1, 0, -1):
            for m3 in range(m2, 0, -1):
                faces = calc_faces(m1, m2, m3)
                min_path = calc_min_path(faces)
                if min_path.is_integer():
                    integer_min_count += 1
        over = integer_min_count > max_paths
        print(M, ", ", integer_min_count)


if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')
