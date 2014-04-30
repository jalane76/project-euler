#! python
import sys
import math
import euler

def number_to_words(n):
    if n < 0 or n >= 1000:
        return str(n) + ' is out of bounds!'

    result = ''
    if n >= 100:
        result = result + number_to_name(int(n / 100)) + 'hundred'
        if n % 100 != 0:
            result = result + 'and'
        n = int(str(n)[1:3])
    if n >= 20:
        result = result + tens(int(n / 10))
        n = int(str(n)[1:2])
    if n > 0:
        result = result + number_to_name(n)
    
    return result

def number_to_name(n):
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'

def tens(n):
    if n == 2:
        return 'twenty'
    if n == 3:
        return 'thirty'
    if n == 4:
        return 'forty'
    if n == 5:
        return 'fifty'
    if n == 6:
        return 'sixty'
    if n == 7:
        return 'seventy'
    if n == 8:
        return 'eighty'
    if n == 9:
        return 'ninety'

def main():
    result = 0
    for i in range(1, 1000):
        result += len(number_to_words(i))
    result += len('onethousand')
    print(result)

if __name__ == "__main__":
    main()
