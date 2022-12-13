import sys
import math
from collections import namedtuple
import heapq

point = namedtuple('point', ['x', 'y'])


def readdata(filename):
    with open(filename) as fid:
        data = [[v for v in line] for line in fid.read().split()]
    return data


def neighbours(cord):
    yield point(cord.x - 1, cord.y)
    yield point(cord.x + 1, cord.y)
    yield point(cord.x, cord.y - 1)
    yield point(cord.x, cord.y + 1)


def move(data, path, target, seen):
    m, n = len(data), len(data[0])
    if path:
        cost, cord = heapq.heappop(path)
        for c in neighbours(cord):
            if (
                (0 <= c.x < m and 0 <= c.y < n) and
                (
                    (data[cord.x][cord.y] == "S") or
                    (data[c.x][c.y] == "E") or
                    (ord(data[c.x][c.y]) <= (ord(data[cord.x][cord.y]) + 1))
                )
            ):
                if c not in seen:
                    seen.add(c)
                    heapq.heappush(path, (cost + 1, c))
                    if c.x == target.x and c.y == target.y:
                        return cost + 1
        return False
    else:
        return 10000


def part1(lines):
    m, n = len(lines), len(lines[0])

    start = [point(i, j) for i in range(m) for j in range(n) if lines[i][j] == "S"][0]
    target = [point(i, j) for i in range(m) for j in range(n) if lines[i][j] == "E"][0]

    def dj(start, target):
        path = [(0, start)]
        heapq.heapify(path)
        seen = set()
        while not (cost := move(lines, path, target, seen)):
            pass
        return cost

    cost = dj(start, target)
    return cost


def part2(lines):
    m, n = len(lines), len(lines[0])

    starts = [point(i, j) for i in range(m) for j in range(n) if lines[i][j] == "a"]
    target = [point(i, j) for i in range(m) for j in range(n) if lines[i][j] == "E"][0]

    def dj(start, target):
        path = [(0, start)]
        heapq.heapify(path)
        seen = set()
        while not (cost := move(lines, path, target, seen)):
            pass
        return cost

    return min([dj(start, target) for start in starts])


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    lines = readdata(filename)
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == "__main__":
    exit(main())
