#! python

def apply_key(tokens, key):
    new_tokens = []
    for i in range(0, len(tokens)):
        new_tokens.append(tokens[i] ^ key[i % len(key)])
    return new_tokens

def main():
    text = ''
    tokens = []
    total = 0
    with open('cipher1.txt') as f:
        for line in f:
            tokens.extend([int(x) for x in line.split(',')])

    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                key = [a, b, c]
                orig_tokens = apply_key(tokens, key)
                text = ''.join([chr(c) for c in orig_tokens])
                if text.count(' the ') > 5:
                    total = sum(orig_tokens)
    print(total)

if __name__ == "__main__":
    main()