import sys
from collections import defaultdict


def readdata(filename):
    with open(filename) as fid:
        txt = fid.read().split('\n')
    return txt


def part1(text, n):
    counter = defaultdict(int)
    for i in range(len(text)):
        old, cur = text[i - n], text[i]
        counter[cur] += 1
        if i >= n:
            if counter[old] == 1:
                counter.pop(old)
            else:
                counter[old] -= 1

            if len(counter) == n:
                break
    return i + 1


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    txt = readdata(filename)
    for line in txt:
        print(f'part1: {part1(line, 4)}')
    for line in txt:
        print(f'part2: {part1(line, 14)}')


if __name__ == "__main__":
    exit(main())
