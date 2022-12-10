import sys


def readdata(filename):
    with open(filename) as fid:
        txt = fid.read().split('\n')
    return txt


def part1(lines):
    x = 1
    t = 0
    cyc = []

    for line in lines:
        cmd, *v = line.split()
        if cmd == "noop":
            t += 1
            cyc.append((t, x))
        elif cmd == "addx":
            t += 1
            cyc.append((t, x))
            t += 1
            cyc.append((t, x))
            x += int(v[0])

    _sum = sum([(cyc[i][0] * cyc[i][1]) for i in range(19, 220, 40)])
    return _sum, cyc


def part2(cyc):
    h_size = 40

    def sprit(t, x):
        return "#" if x <= ((t - 1) % h_size) + 1 <= x + 2 else " "

    crc = [sprit(t, x) for t, x in cyc]

    it = iter(crc)
    disp = ["".join([next(it) for i in range(40)]) for j in range(6)]

    return "\n".join(disp)


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    lines = readdata(filename)
    p1, data = part1(lines)
    print(f'part1: {p1}')
    print(f'part1:\n{part2(data)}')


if __name__ == "__main__":
    exit(main())
