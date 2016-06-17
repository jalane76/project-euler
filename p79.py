#! python

import time
import itertools
import euler

def main():
    with open('p79_keylog.txt') as f:
        logins = [[x for x in line.split()] for line in f]
    logins = [s[0] for s in logins]

    pairs_1 = [(s[0], s[1]) for s in logins]
    pairs_2 = [(s[1], s[2]) for s in logins]
    pairs = pairs_1 + pairs_2
    pairs = list(set(pairs))
    pairs.sort()

    d = {str(i) : ([], []) for i in range(0, 10)}
    for p in pairs:
        x = p[0]
        y = p[1]
        d[x][1].append(y)
        d[y][0].append(x)

    remove_keys = [k for k in d.keys() if len(d[k][0]) == 0 and len(d[k][1]) == 0]
    for k in remove_keys:
        del d[k]

    keys = list(d.keys())
    result = [keys[0]]
    for k in keys:
        lists = d[k]

        if result[0] in lists[1]:
            result = [k] + result
        elif result[-1] in lists[0]:
            result.append(k)
        else:
            for i in range(0, len(result) - 1):
                left = result[i]
                right = result[i + 1]
                if left in lists[0] and right in lists[1]:
                    result.insert(i + 1, k)

    print(d)
    print(''.join(result))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')