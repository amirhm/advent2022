import sys
import math


def readdata(filename):
    with open(filename) as fid:
        lines = fid.read().split("\n\n")
    data = [line.split("\n") for line in lines]
    return data


class nodes:
    def __init__(self, parent=None):
        self.parent = parent
        self.childs = []


def check(l1, l2):
    ret = []

    def dfs(v0, v1):
        nonlocal ret
        if ret:
            return ret[0]
        if isinstance(v0, list) and isinstance(v1, list):
            while v0 and v1:
                dfs(v0[0], v1[0])
                v0, v1 = v0[1:], v1[1:]
            if not v0 and v1:
                # print("left ran out")
                ret.append(1)
            elif v0 and not v1:
                # print("right ran out")
                ret.append(2)
        elif isinstance(v0, int) and isinstance(v1, int):
            if v0 < v1:
                # print("smaller")
                ret.append(1)
            elif v0 > v1:
                # print("bigger")
                ret.append(2)
        elif isinstance(v0, list):
            dfs(v0, [v1])
        elif isinstance(v1, list):
            dfs([v0], v1)
    ret = []
    dfs(l1, l2)
    return True if ret[0] == 1 else False


def part1(lines):
    su = 0
    for idx, (l1, l2) in enumerate(lines):
        p1, p2 = eval(l1), eval(l2)
        ans = check(p1, p2)
        if ans == 1:
            su += (idx + 1)

    return su


class packet:
    def __init__(self, data, idx=0):
        self.data = data
        self.idx = idx

    def __lt__(self, other):
        return check(self.data, other.data)


def part2(lines):
    packets = []
    for l1, l2 in lines:
        p1, p2 = eval(l1), eval(l2)
        packets.append(packet(p1))
        packets.append(packet(p2))
    packets.append(packet([[2]], 1))
    packets.append(packet([[6]], 1))
    p = sorted(packets)

    results = math.prod([idx + 1 for idx, val in enumerate(p) if val.idx == 1])
    return results


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    lines = readdata(filename)
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == "__main__":
    exit(main())
