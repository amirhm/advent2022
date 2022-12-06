import sys
from collections import namedtuple
points = namedtuple('points', ['start', 'stop'])


def readdata(filename):
    with open(filename) as fid:
        txt = fid.read()
    return txt.split("\n")


def part1(data):
    total = 0
    for idx, l in enumerate(data):
        p1, p2 = l.split(',')
        p1 = points(*map(int, p1.split('-')))
        p2 = points(*map(int, p2.split('-')))

        if (
            ((p1.start <= p2.start) and (p1.stop >= p2.stop))
            or
            ((p1.start >= p2.start) and (p1.stop <= p2.stop))
           ):
            total += 1
    return total


def part2(data):
    total = 0
    for idx, l in enumerate(data):
        p1, p2 = l.split(',')
        p1 = points(*map(int, p1.split('-')))
        p2 = points(*map(int, p2.split('-')))

        if (
            ((p1[0] <= p2[0] <= p1[1]) or (p1[0] <= p2[1] <= p1[1]))
            or
            (p2[0] <= p1[0] <= p2[1])
           ):
            total += 1
    return total


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    data = readdata(filename)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    exit(main())
