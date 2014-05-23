#! python
import poker

def main():
    max_digital_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            n = a ** b
            s = sum([int(c) for c in str(n)])
            if s > max_digital_sum:
                max_digital_sum = s
    print(max_digital_sum)

if __name__ == "__main__":
    main()