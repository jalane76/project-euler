#! python

import time
import math
import fractions
import euler

def find_minimal_solution(d):
    pass

def main():
    n = 13
    D = [x for x in range(2, n + 1) if not euler.is_square_number(x)]

    max_x = 0
    max_d = 0

    # for i in range(0, len(D)):
    #     solution = find_minimal_solution(D[i])
    #     print(D[i], ': ', solution)
    #     if solution[0] > max_x:
    #         max_x = solution[0]
    #         max_d = D[i]
    # print(max_d)




if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')