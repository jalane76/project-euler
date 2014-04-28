#! python
import sys

def main():
    f1 = 1
    f2 = 2
    result = f2
    while f2 <= 4000000:
        f = f1 + f2
        if f % 2 == 0:
            result += f
        f1 = f2
        f2 = f
    print(result)

if __name__ == "__main__":
    main()
