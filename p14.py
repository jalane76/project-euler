#! python
import sys
import math
import euler

def main():
    largest_number = 0
    largest_sequence = []
    largest_length = 0
    for i in range(2, 1000000):
        sequence = euler.collatz_sequence(i)
        if len(sequence) > largest_length:
            largest_number = i
            largest_sequence = sequence
            largest_length = len(sequence)
            
    print(largest_number)
    #print(largest_sequence)
    print(largest_length)

if __name__ == "__main__":
    main()
