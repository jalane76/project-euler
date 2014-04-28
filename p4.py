#! python
import sys
import math

def is_palindrome(s):
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    if len(s1) != len(s2):
        s2 = s2[1:]
    s2 = s2[::-1]
    return s1 == s2

def main():
    palindromes = []

    # Find all the palindromes
    for i in range(100, 1000):
        for j in range(100, 1000):
            n = i * j
            if is_palindrome(str(n)):
                palindromes.append(n)

    # Find the largest palindrome
    largest = 0
    for p in palindromes:
        if p >= largest:
            largest = p

    print(largest)
    
if __name__ == "__main__":
    main()
