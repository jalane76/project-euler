#! python
import sys
import math
import euler

def main():
    grid_size = 20
    print(euler.binomial_coefficient(grid_size + grid_size, grid_size))

if __name__ == "__main__":
    main()
