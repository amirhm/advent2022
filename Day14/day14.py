import sys


def readdata(filename="data.txt"):
    with open(filename) as fid:
        lines = fid.read().split('\n')
    return [[tuple(map(int, point.split(','))) for point in line.split("->")] for line in lines]

def fill_rocks(data):
    rocks = set()
    for line in data:
        n = len(line)
        for j in range(n - 1):
            st = line[j] 
            sp = line[j + 1]
            if st[0] == sp[0]:
                start, stop = min(st[1], sp[1]), max(st[1], sp[1]) + 1
                for k in range(start, stop):
                    rocks.add((st[0], k))

            if st[1] == sp[1]:
                start, stop = min(st[0], sp[0]), max(st[0], sp[0]) + 1
                for k in range(start, stop):
                    rocks.add((k, st[1]))

    return rocks


def n_point(point):
    yield point[0] , point[1] + 1 
    yield point[0] - 1, point[1] + 1 
    yield point[0] + 1, point[1] + 1


class game:
    def __init__(self, rocks, level):
        self.rocks = rocks
        self.level = level
    def move(self, point):
        for p in n_point(point):
            if p not in self.rocks:
                return  p
            else:
                continue
        return None

    def play1(self):
        end_game = False
        cnt = 0
        while not end_game:
            point = (500, 0)
            n_point = self.move(point)
            while (n_point is not None)  and (n_point[1] < self.level):
                n_point, point = self.move(point), n_point
            if n_point is None:
                self.rocks.add(point)
                cnt += 1
            elif n_point[1] >= self.level:
                end_game = True
        
        return cnt

    def play2(self):
        cnt = 0
        while True:
            px, py = (500, 0)
            while (py < self.level):
                if (px, py + 1 ) not in self.rocks:
                    py += 1
                elif (px - 1, py + 1) not in self.rocks:
                    px -= 1
                    py += 1
                elif (px + 1, py + 1) not in self.rocks:
                    px += 1
                    py += 1
                else:
                    self.rocks.add((px, py))
                    break
            self.rocks.add((px, py))
            cnt += 1
        
            if (500, 0) in self.rocks:
                break
        return cnt


def part1(lines):
    rocks = fill_rocks(lines)
    abys = max(map(lambda x: x[1], rocks))
    g = game(rocks, abys + 1)
    return g.play1()

def part2(lines):
    rocks = fill_rocks(lines)
    abys = max(map(lambda x: x[1], rocks))
    g = game(rocks, abys)
    return g.play2()

import time
def main():
    _, filename, *_ = *sys.argv, "data.txt"
    lines = readdata(filename)
    print(f'part1: {part1(lines)}')
    
    t0 = time.time()
    print(f'part2: {part2(lines)}')
    print(f"{time.time() - t0}")

if __name__ == "__main__":
    exit(main())









