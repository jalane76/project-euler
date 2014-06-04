#! python
import sys
import math
import euler
import time

def get_left_parent(triangle, level, index):
    parent_index = index - 1
    parent_level = level - 1
    if parent_index < 0:
        return 0
    else:
        return triangle[parent_level][parent_index]

def get_right_parent(triangle, level, index):
    parent_index = index
    parent_level = level - 1
    if parent_index >= len(triangle[parent_level]):
        return 0
    else:
        return triangle[parent_level][parent_index]

def main():
    with open('triangle.txt') as f:
        triangle = [[int(x) for x in line.split()] for line in f]

    for level in range(1, len(triangle)):
        for index in range(len(triangle[level])):
            left = get_left_parent(triangle, level, index)
            right = get_right_parent(triangle, level, index)
            if left > right:
                triangle[level][index] += left
            else:
                triangle[level][index] += right

    print(max(triangle[-1]))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')
