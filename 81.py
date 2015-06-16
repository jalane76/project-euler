#! python

import time
import itertools
import math
import euler
from decimal import *

ROW = 0
COL = 1

def peek_down(point, matrix):
    i = point[ROW]
    j = point[COL]
    if j + 1 >= len(matrix):
        return None
    return matrix[i][j + 1]

def peek_right(point, matrix):
    i = point[ROW]
    j = point[COL]
    if i + 1 >= len(matrix):
        return None
    return matrix[i + 1][j]

def move_down(point):
    return (point[ROW], point[COL] + 1)

def move_right(point):
    return (point[ROW] + 1, point[COL])

def main():
    with open('p81_matrix_test.txt') as f:
        matrix = [[int(x) for x in line.split(',')] for line in f]

    sequence = []

    current_point = (0, 0)
    end_point = (len(matrix) - 1, len(matrix) - 1)

    path_sum = matrix[current_point[ROW]][current_point[COL]]
    sequence.append(path_sum)

    while current_point != end_point:
        down = peek_down(current_point, matrix)
        right = peek_right(current_point, matrix)

        if down is None or (right is not None and down > right):
            sequence.append(right)
            path_sum += right
            current_point = move_right(current_point)
        else:
            sequence.append(down)
            path_sum += down
            current_point = move_down(current_point)

    print(path_sum)
    print(sequence)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')