
import sys


def readdata(filename):
    with open(filename) as fid:
        data = [line.split() for line in fid.read().split("\n")]
    return data


class pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y

    def move(self, cmd):
        if cmd == "R":
            self.y += 1
        if cmd == "U":
            self.x += 1
        if cmd == "D":
            self.x -= 1
        if cmd == "L":
            self.y -= 1

    def update(self, hpos):
        xd, sx = abs(hpos.x - self.x), 1 if hpos.x > self.x else -1
        yd, sy = abs(hpos.y - self.y), 1 if hpos.y > self.y else -1
        if (xd > 1 and yd >= 1) or (xd >= 1 and yd > 1):
            self.x += sx
            self.y += sy
        elif xd > 1:
            self.x += sx
        elif yd > 1:
            self.y += sy


def part1(data):
    head = pos(0, 0)
    tl = pos(0, 0)
    tail_seen = set()
    for cmd, cnt in data:
        cnt = int(cnt)
        for j in range(cnt):
            head.move(cmd)
            tl.update(head)
            tail_seen.add(tl.get_pos())
    return len(tail_seen)


def part2(data):
    head = pos(0, 0)
    tail_num = 9
    tl = [pos(0, 0) for i in range(tail_num)]
    lst = [head, *tl]

    tail_seen = set()
    for cmd, cnt in data:
        cnt = int(cnt)
        for j in range(cnt):
            head.move(cmd)
            for i in range(len(lst) - 1):
                lst[i + 1].update(lst[i])
            tail_seen.add(lst[-1].get_pos())
    return len(tail_seen)


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    data = readdata(filename)
    print(f'part1: {part1(data)}')
    print(f'part2: {part2(data)}')


if __name__ == "__main__":
    exit(main())
