import re
import copy
filename = "data.txt"


with open(filename) as fid:
    txt = fid.read().split('\n')

for idx, t in enumerate(txt):
    if t.startswith('move'):
        break

brd, cmds = txt[:idx -1], txt[idx:]

b = [[l[i:i+4].strip() for i in range(0, len(l), 4) ] for l in reversed(brd)]
board = [[i for i in v if i] for v in  zip(*b)]
brd = copy.deepcopy(board)

for cm in cmds:
    a, b, c = map(int, re.findall('move ([0-9]*) from ([0-9]*) to ([0-9]*)', cm)[0])
    for k in range(a):
        board[c - 1].append(board[b - 1].pop())


part1 = "".join([l.pop().replace('[', "").replace(']', "") for l in board])
print(part1)

board = brd
for cm in cmds:
    a, b, c = map(int, re.findall('move ([0-9]*) from ([0-9]*) to ([0-9]*)', cm)[0])
    v = [board[b - 1].pop() for i in range(a)]
    board[c - 1].extend(reversed(v))

part2 = "".join([l.pop().replace('[', "").replace(']', "") for l in board])
print(part2)
