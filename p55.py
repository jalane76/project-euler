#! python
import euler

def main():
    lychrel_count = 0
    for n in range(1, 10000):
        is_lychrel = True
        m = n
        for i in range(0, 50):
            m = m + int(str(m)[::-1])
            s = str(m)
            if euler.is_palindrome(s):
                is_lychrel = False
                break

        if is_lychrel:
            print(n, ' ', m)
            lychrel_count += 1

    print(lychrel_count)

if __name__ == "__main__":
    main()