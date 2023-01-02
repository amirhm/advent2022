import sys


def readdata(filename):
    with open(filename) as fid:
        data = [line for line in fid.read().split("\n")]
    data = [[v.split() for v in line.split(":")] for line in data]
    return {node[0]: int(cm[0]) if len(cm) == 1 else cm for node, cm in data}


def part1(dic):
    cache = {}

    def check(node):
        val = dic[node]

        if node in cache:
            return cache[node]
        if isinstance(val, int):
            cache[node] = val
        elif val[1] == '+':
            cache[node] = check(val[0]) + check(val[2])
        elif val[1] == '-':
            cache[node] = check(val[0]) - check(val[2])
        elif val[1] == '*':
            cache[node] = check(val[0]) * check(val[2])
        elif val[1] == '/':
            cache[node] = int(check(val[0]) / check(val[2]))
        return cache[node]
    cnt = check('root')
    return cnt


def part2(dic):

    def check(node, humn):
        cache = {'humn': humn}

        def _check(node):
            nonlocal dic
            val = dic[node]
            if node in cache:
                return cache[node]
            if isinstance(val, int):
                cache[node] = val
            elif val[1] == '+':
                cache[node] = _check(val[0]) + _check(val[2])
            elif val[1] == '-':
                cache[node] = _check(val[0]) - _check(val[2])
            elif val[1] == '*':
                cache[node] = _check(val[0]) * _check(val[2])
            elif val[1] == '/':
                cache[node] = _check(val[0]) / _check(val[2])
            return cache[node]
        return _check(node)

    n1, _, n2 = dic['root']

    def check_dependancy(node):
        dep = []

        def dfs(node):
            if isinstance(dic[node], int):
                return
            else:
                n1, _, n2 = dic[node]
                for n in [n1, n2]:
                    dep.append(n)
                    dfs(n)

        dfs(node)
        return dep

    cnt1, cnt2 = check(n1, dic['humn']), check(n2, dic['humn'])

    if 'humn' in check_dependancy(n1):
        nc, val = n1, cnt2
    elif 'humn' in check_dependancy(n2):
        nc, val = n2, cnt1
    dir = 'ascend' if check(n1, 0) < check(n1, 1) else 'descend'

    left, right = 0, 10000000000000
    while left <= right:
        mid = (left + right) // 2
        cnt = check(nc, mid)
        if cnt == val:
            break
        if dir == 'ascend':
            left, right = (mid + 1, right) if cnt < val else (left, mid - 1)
        else:
            left, right = (mid + 1, right) if cnt > val else (left, mid - 1)

    return mid


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    lines = readdata(filename)
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == "__main__":
    exit(main())
