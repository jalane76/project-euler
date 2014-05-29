#! python
import sys
import euler

def main():
    lychrel_count = 0
    lychrels = []
    sums = []
    for n in range(1, 10000):
        is_lychrel = True
        m = n
        for i in range(0, 10000):
            m = m + int(str(m)[::-1])
            s = str(m)
            if euler.is_palindrome(s):
                is_lychrel = False
                break

        if is_lychrel:
            lychrels.append(n)
            sums.append(m)
            lychrel_count += 1

    print(lychrel_count)
    print(len(set(sums)))

if __name__ == "__main__":
    main()