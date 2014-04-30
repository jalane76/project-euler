#! python
import sys
import math
import euler

def main():
    gridSize = 20
    print(euler.binomial_coefficient(gridSize + gridSize, gridSize))

if __name__ == "__main__":
    main()
