import sys
import math


def readdata(filename):
    with open(filename) as fid:
        lines = fid.read().split("\n\n")
    data = [line.split("\n") for line in lines]
    return data


class monkey:
    def __init__(self, data):
        self.data = data
        self.operation = None
        self.divisor = 1
        self.divide = True
        self.target = None
        self.cnt = 0
        self.ret = [[], []]

    def set_item(self, value):
        self.data = self.data + value

    def get_item(self):
        return self.ret

    def play(self):
        data = self.data
        self.cnt += len(data)
        self.ret = [[], []]
        for d in data:
            d = self.operation(d)
            if self.divide:
                d = d // 3
            if (d % self.divisor) == 0:
                self.ret[0].append(d)
            else:
                self.ret[1].append(d)
        self.data.clear()


def parse_monkeys(data):
    mk_data = []
    for mid in range(len(data)):
        mk_data.append((
            data[mid][1].split(":")[-1].strip().split(','),
            data[mid][2].split("=")[-1].strip().split(),
            data[mid][3].split()[-1].strip(),
            data[mid][4].split()[-1].strip(),
            data[mid][5].split()[-1].strip()
        ))
    mon = []
    for mk in mk_data:
        data = list(map(int, mk[0]))
        mon.append(monkey(data))

    for idx, mk in enumerate(mk_data):
        mon[idx].operation = eval("lambda old:" + "".join(mk[1]))
        mon[idx].divisor = int(mk[2])
        mon[idx].target = int(mk[3]), int(mk[4])
    return mon


def part1(monkeys):
    for r in range(20):
        for m in monkeys:
            m.play()
            a, b = m.get_item()
            monkeys[m.target[0]].set_item(a)
            monkeys[m.target[1]].set_item(b)

    c = ([m.cnt for m in monkeys])
    return (math.prod(sorted(c)[-2:]))


def part2(mon):
    const = math.prod([mk.divisor for mk in mon])
    for mk in mon:
        mk.divide = False
    for r in range(10000):
        for m in mon:
            m.play()
            a, b = m.get_item()
            a = [(val % const) for val in a]
            b = [(val % const) for val in b]
            mon[m.target[0]].set_item(a)
            mon[m.target[1]].set_item(b)

    c = ([m.cnt for m in mon])
    return (math.prod(sorted(c)[-2:]))


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    lines = readdata(filename)
    monkeys = parse_monkeys(lines)
    print(f'part1: {part1(monkeys)}')
    monkeys = parse_monkeys(lines)
    print(f'part2: {part2(monkeys)}')


if __name__ == "__main__":
    exit(main())
