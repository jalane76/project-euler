#! python

import time
import itertools
import math
import euler
from decimal import *

ROW = 0
COL = 1

def peek_up(point, matrix):
    i = point[ROW]
    j = point[COL]
    if j - 1 < 0:
        return None
    return matrix[i][j - 1]

def peek_down(point, matrix):
    i = point[ROW]
    j = point[COL]
    if j + 1 >= len(matrix):
        return None
    return matrix[i][j + 1]

def peek_left(point, matrix):
    i = point[ROW]
    j = point[COL]
    if i - 1 < 0:
        return None
    return matrix[i - 1][j]

def peek_right(point, matrix):
    i = point[ROW]
    j = point[COL]
    if i + 1 >= len(matrix):
        return None
    return matrix[i + 1][j]

def move_up(point):
    return (point[ROW], point[COL] - 1)

def move_down(point):
    return (point[ROW], point[COL] + 1)

def move_left(point):
    return (point[ROW] - 1, point[COL])

def move_right(point):
    return (point[ROW] + 1, point[COL])

def main():
    with open('p81_matrix.txt') as f:
        matrix = [[int(x) for x in line.split(',')] for line in f]

    head = (0, 0)
    tail = (len(matrix) - 1, len(matrix) - 1)

    forward_sequence = []
    forward_point = head

    backward_sequence = []
    backward_point = tail

    forward_sum = matrix[forward_point[ROW]][forward_point[COL]]
    forward_sequence.append(forward_sum)
    
    backward_sum = matrix[backward_point[ROW]][backward_point[COL]]
    backward_sequence.append(backward_sum)

    while forward_point != backward_point and forward_point != tail and backward_point != head:
        down = peek_down(forward_point, matrix)
        right = peek_right(forward_point, matrix)

        if down is None or (right is not None and down > right):
            forward_sequence.append(right)
            forward_sum += right
            forward_point = move_right(forward_point)
        else:
            forward_sequence.append(down)
            forward_sum += down
            forward_point = move_down(forward_point)

        up = peek_up(backward_point, matrix)
        left = peek_left(backward_point, matrix)

        if up is None or (left is not None and up > left):
            backward_sequence.insert(0, left)
            backward_sum += left
            backward_point = move_left(backward_point)
        else:
            backward_sequence.insert(0, up)
            backward_sum += up
            backward_point = move_up(backward_point)

    sequence = forward_sequence + backward_sequence[1:]
    path_sum = sum(sequence)
    length = len(sequence)

    print(path_sum)
    print(sequence)
    print(length)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')