#! python
import sys
import math
import euler

def main():
    numbers = []
    
    f = open('p13.dat')
    
    line = f.readline()
    while line:
        numbers.append(line.strip())
        line = f.readline()
        
    f.close()
    
    sum = 0
    for n in numbers:
        sum += int(n[:15])
    
    print(str(sum)[:10])

if __name__ == "__main__":
    main()
