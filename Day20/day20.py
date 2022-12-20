import sys

def readdata(filename):
    with open(filename) as fid:
        data = list(map(int, fid.read().split("\n")))
    return data

class node:
    def __init__(self, val, before=None, next=None):
        self.before = before
        self.next = next
        self.val = val



def part1(lines):
    n = len(lines)
    cur = node(lines[0] ) 
    di = {0:cur} 
    for i in range(1, n):
        cur.next = node(lines[i]  , before=cur) 
        di.update({i: cur.next})
        cur = cur.next
        if cur.val == 0:
            zero = cur

    first = di[0]
    last = di[n - 1]
    first.before, last.next =  last, first

    # print(di)
    for i in range(len(lines)):
        cnt = di[i].val
        if abs(cnt) > 0: 
            b, a = di[i].before , di[i].next
            b.next, a.before = a, b
        if cnt > 0:
            cur = di[i] 
            for k in range(cnt % (n - 1)):
                cur = cur.next
            cur0, cur1 = cur, cur.next
        elif cnt < 0:
            cur = di[i]
            for k in range((-cnt) % (n - 1)):
                cur = cur.before
            cur1, cur0 = cur, cur.before

        if abs(cnt) > 0:
            cur0.next, di[i].before = di[i], cur0
            cur1.before, di[i].next = di[i], cur1

#        cur = head
#        for k in range(n + 2):
#            print(cur.val, end=" ")
#            cur = cur.next
#        print("")
    ret = []
    for c in [1000, 2000, 3000]:
        cur = zero
        for k in range(c):
            cur = cur.next
        ret.append(cur.val)
    return sum(ret)
def part2(lines):
    n = len(lines)
    cur = node(lines[0] * 811589153) 
    di = {0:cur} 
    for i in range(1, n):
        cur.next = node(lines[i] * 811589153, before=cur) 
        di.update({i: cur.next})
        cur = cur.next
        if cur.val == 0:
            zero = cur

    first = di[0]
    last = di[n - 1]
    first.before, last.next =  last, first

    for r in range(10):
        for i in range(len(lines)):
            cnt = di[i].val
            if abs(cnt) > 0: 
                b, a = di[i].before , di[i].next
                b.next, a.before = a, b
            if cnt > 0:
                cur = di[i] 
                for k in range(cnt % (n - 1)):
                    cur = cur.next
                cur0, cur1 = cur, cur.next
            elif cnt < 0:
                cur = di[i]
                for k in range((-cnt) % (n - 1)):
                    cur = cur.before
                cur1, cur0 = cur, cur.before

            if abs(cnt) > 0:
                cur0.next, di[i].before = di[i], cur0
                cur1.before, di[i].next = di[i], cur1

        #  cur = first
        #  for k in range(n):
        #      print(cur.val, end=" ")
        #      cur = cur.next
        #  print("")
    ret = []
    for c in [1000, 2000, 3000]:
        cur = zero
        for k in range(c):
            cur = cur.next
        ret.append(cur.val)
    return sum(ret)

def main():
    _, filename, *_ = *sys.argv, "data.txt"
    lines = readdata(filename)
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')

if __name__ == "__main__":
    exit(main())









