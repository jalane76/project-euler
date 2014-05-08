#! python
import sys
import math
import euler

def main():
    max_p = 0
    max_solutions = []
    for p in range(3, 1001):
        solutions = []
        for c in range(p - 2, 1, -1):
            for b in range(p - c - 1, 0, -1):
                a = p - c - b
                if a + b + c == p and a ** 2 + b ** 2 == c ** 2:
                    solution = ()
                    if a < b:
                        solution = (a, b, c)
                    else:
                        solution = (b, a, c)
                    solutions.append(solution)
        solutions = set(solutions)
        if len(solutions) > len(max_solutions):
            max_p = p
            max_solutions = solutions
    print(max_solutions)
    print(max_p)

if __name__ == "__main__":
    main()


