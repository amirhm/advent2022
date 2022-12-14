import sys
from collections import namedtuple
import heapq
from itertools import product
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


def move_fwd(data, path, target, seen):
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
                    if c in target:
                        return cost + 1
        return False
    else:
        raise AssertionError


def move_bkd(data, path, target, seen):
    m, n = len(data), len(data[0])
    if path:
        cost, cord = heapq.heappop(path)
        for c in neighbours(cord):
            if (
                (0 <= c.x < m and 0 <= c.y < n) and
                (
                    (data[cord.x][cord.y] == "E") or
                    (ord(data[cord.x][cord.y]) <= (ord(data[c.x][c.y]) + 1))
                )
            ):
                if c not in seen:
                    seen.add(c)
                    heapq.heappush(path, (cost + 1, c))
                    if c in target:
                        return cost + 1
        return False
    else:
        raise AssertionError


def part1(lines):
    m, n = len(lines), len(lines[0])
    itr = product(range(m), range(n))
    start = [point(i, j) for i, j in itr if lines[i][j] == "S"][0]
    itr = product(range(m), range(n))
    target = [point(i, j) for i, j in itr if lines[i][j] == "E"][0]
    target = set({target})

    def dj(start, target):
        path = [(0, start)]
        heapq.heapify(path)
        seen = set()
        while not (cost := move_fwd(lines, path, target, seen)):
            pass
        return cost

    cost = dj(start, target)
    return cost


def part2(lines):
    m, n = len(lines), len(lines[0])

    itr = product(range(m), range(n))
    starts = [point(i, j) for i, j in itr if lines[i][j] == "a"]
    itr = product(range(m), range(n))
    target = [point(i, j) for i, j in itr if lines[i][j] == "E"][0]
    target, starts = set(starts), target

    def dj(start, target):
        path = [(0, start)]
        heapq.heapify(path)
        seen = set()
        while not (cost := move_bkd(lines, path, target, seen)):
            pass
        return cost

    return dj(starts, target)


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    lines = readdata(filename)
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == "__main__":
    exit(main())
