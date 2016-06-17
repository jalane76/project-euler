#! python
import sys
import math

def sum_of_squares(n):
	result = 0
	for i in range(n + 1):
		result += i * i
	return result

def square_of_sum(n):
	result = 0
	for i in range(n + 1):
		result += i
	result = result * result
	return result

def main():
    result = square_of_sum(100) - sum_of_squares(100)
    print(result)
    
if __name__ == "__main__":
    main()
