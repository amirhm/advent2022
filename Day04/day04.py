from collections import namedtuple
points = namedtuple('points', ['start','stop'])


with open("data.txt") as fid:
    txt = fid.read()

data = txt.split("\n")


total = 0
for idx, l in enumerate(data):
    p1, p2 = l.split(',')
    p1 = points(*map(int, p1.split('-')))
    p2 = points(*map(int, p2.split('-')))

    if ((p1.start <= p2.start) and (p1.stop >= p2.stop)) or ((p1.start >= p2.start) and (p1.stop <= p2.stop)):
        total += 1
print(total)

total = 0
for idx, l in enumerate(data):
    p1, p2 = l.split(',')
    p1 = points(*map(int, p1.split('-')))
    p2 = points(*map(int, p2.split('-')))

    if ((p1[0] <= p2[0] <= p1[1]) or (p1[0] <= p2[1] <= p1[1])) or (p2[0] <= p1[0] <= p2[1])  : 
        total += 1
print(total)