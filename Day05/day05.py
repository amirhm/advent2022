import re
import sys
from copy import deepcopy


reg = re.compile('move ([0-9]*) from ([0-9]*) to ([0-9]*)')


def readdata(filename):
    with open(filename) as fid:
        txt = fid.read().split('\n')

    for idx, t in enumerate(txt):
        if t.startswith('move'):
            break
    brd, cmds = txt[:idx - 1], txt[idx:]
    b = [[ln[i:i+4] for i in range(0, len(ln), 4)] for ln in reversed(brd)]
    board = [[i for i in v if i.strip()] for v in zip(*b)]
    return board, cmds


def part1(board, cmds):
    for cm in cmds:
        a, b, c = map(int, reg.findall(cm)[0])
        for k in range(a):
            board[c - 1].append(board[b - 1].pop())

    ret = "".join([ln.pop() for ln in board])
    return ret.replace('[', "").replace(']', "").replace(" ", "")


def part2(board, cmds):
    for cm in cmds:
        a, b, c = map(int, reg.findall(cm)[0])
        v = [board[b - 1].pop() for i in range(a)]
        board[c - 1].extend(reversed(v))

    ret = "".join([ln.pop() for ln in board])
    return ret.replace('[', "").replace(']', "").replace(" ", "")


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    brd, cmds = readdata(filename)
    print(part1(deepcopy(brd), cmds))
    print(part2(brd, cmds))


if __name__ == "__main__":
    exit(main())
