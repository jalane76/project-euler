#! python

import time

def main():
    with open('p81_matrix.txt') as f:
        matrix = [[int(x) for x in line.split(',')] for line in f]

    mat_size = len(matrix)

    for i in range(mat_size - 2, -1, -1):
        matrix[mat_size - 1][i] += matrix[mat_size - 1][i + 1]
        matrix[i][mat_size - 1] += matrix[i + 1][mat_size - 1]

    for i in range(mat_size - 2, -1, -1):
        for j in range(mat_size - 2, -1, -1):
            matrix[i][j] += min([matrix[i + 1][j], matrix[i][j + 1]])

    print(matrix[0][0])

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')