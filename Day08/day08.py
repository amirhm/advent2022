import sys
from functools import reduce


def readdata(filename):
    with open(filename) as fid:
        txt = [[int(val) for val in line] for line in fid.read().split('\n')]

    return txt


def part1(data):
    m, n = len(data), len(data[0])
    field = {}

    for i in range(m):
        field[(i, 0, 'left')] = (True, data[i][0])
        field[(i, n - 1, 'right')] = (True, data[i][n - 1])

    for j in range(m):
        field[(0, j, 'top')] = (True, data[0][j])
        field[(m - 1, j, 'bottom')] = (True, data[m - 1][j])

    def dfs(i, j, direction):
        if (i, j, direction) in field:
            return field[(i, j, direction)]
        if direction == "top":
            if (i > 0) and (i, j, "top") not in field:
                mx = dfs(i - 1, j, "top")[1]
                field[(i, j, "top")] = (data[i][j] > mx), max(data[i][j], mx)
        if direction == "bottom":
            if (i < m - 1) and (i, j, "bottom") not in field:
                mx = dfs(i + 1, j, "bottom")[1]
                field[(i, j, "bottom")] = (data[i][j] > mx), max(mx, data[i][j])
        if direction == "right":
            if (j < n - 1) and (i, j, "right") not in field:
                mx = dfs(i, j + 1, "right")[1]
                field[(i, j, "right")] = (data[i][j] > mx), max(mx, data[i][j])
        if direction == "left":
            if (0 < j) and (i, j, "left") not in field:
                mx = dfs(i, j - 1, "left")[1]
                field[(i, j, "left")] = (data[i][j] > mx), max(mx, data[i][j])
        return field[(i, j, direction)]

    dfs(0, 0, "bottom")
    dfs(0, 0, "right")
    dfs(m - 1, n - 1, "top")
    dfs(m - 1, n - 1, "left")
    mat = [[0 for _ in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            dfs(i, j, "bottom")
            dfs(i, j, "right")
            dfs(i, j, "top")
            dfs(i, j, "left")
            mat[i][j] = field[(i, j, 'top')][0] or field[(i, j, 'left')][0] or field[(i, j, 'bottom')][0] or field[(i, j, 'right')][0]
    return sum([sum(m) for m in mat])


def part2_2(data):

    def dfs(i, dir, data, field={}):
        m = len(data)
        if i in field:
            return field[i]
        if dir and i == 0:
            return ((data[0], 0), 0)
        if (not dir) and i == m - 1:
            return ((data[m - 1], m - 1), 0)
        idx = (i - 1) if dir else (i + 1)
        mx = data[idx]
        while (0 < idx < m - 1) and (data[i] > mx):
            (mx, idx), _ = dfs(idx, dir, data, field)
        field[i] = ((mx, idx), (i - idx) if dir else (idx - i))
        return field[i]

    m, n = len(data), len(data[0])
    mat = [[[0, 0, 0, 0] for _ in range(n)] for i in range(m)]

    for i in range(m):
        field = {}
        for j in range(n):
            _, mat[i][j][0] = dfs(j, True, data[i], field)
        field = {}
        for j in range(n):
            _, mat[i][j][1] = dfs(j, False, data[i], field)

    dataT = list(zip(*data))

    for j in range(n):
        field = {}
        for i in range(m):
            _, mat[i][j][2] = dfs(i, True, dataT[j], field)
        field = {}
        for i in range(m):
            _, mat[i][j][3] = dfs(i, False, dataT[j], field)

    _mx = 0
    for i in range(m):
        for j in range(n):
            _mx = max(reduce(lambda x, y: x * y, mat[i][j]), _mx)

    return _mx


def part2(data):
    m, n = len(data), len(data[0])
    field = {}

    for i in range(m):
        field[(i, 0, 'left')] = ((data[i][0], 0), 0)
        field[(i, n - 1, 'right')] = ((data[i][n - 1], n - 1), 0)

    for j in range(m):
        field[(0, j, 'top')] = ((data[0][j], 0), 0)
        field[(m - 1, j, 'bottom')] = ((data[m - 1][j], m - 1), 0)

    def dfs(i, j, direction):
        if (i, j, direction) in field:
            return field[(i, j, direction)]
        if direction == "top":
            idx = i - 1
            mx = data[i - 1][j]
            while (idx > 0) and (data[i][j] > mx):
                (mx, idx), _ = dfs(idx, j, "top")
            field[(i, j, "top")] = ((mx, idx), i - idx)

        if direction == "left":
            idx = j - 1
            mx = data[i][j - 1]
            while (idx > 0) and (data[i][j] > mx):
                (mx, idx), _ = dfs(i, idx, direction)
            field[(i, j, direction)] = ((mx, idx), j - idx)

        if direction == "bottom":
            idx = i + 1
            mx = data[idx][j]
            while (idx < m - 1) and (data[i][j] > mx):
                (mx, idx), _ = dfs(idx, j, direction)
            field[(i, j, direction)] = ((mx, idx), idx - i)

        if direction == "right":
            idx = j + 1
            mx = data[i][idx]
            while (idx < n - 1) and (data[i][j] > mx):
                (mx, idx), _ = dfs(i, idx, direction)
            field[(i, j, direction)] = ((mx, idx), idx - j)
        return field[(i, j, direction)]

    mat = [[1 for _ in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            for dir in ['top', 'left', 'bottom', 'right']:
                _, cnt = dfs(i, j, dir)
                mat[i][j] *= cnt

    return max([max(m)for m in mat])


def _part2(data):
    m, n = len(data), len(data[0])
    mx = [[0 for j in range(n)] for i in range(m)]
    mx1 = [[[] for j in range(n)] for i in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            s1, s2, s3, s4 = 0, 0, 0, 0
            for k in range(i - 1, -1, -1):
                s1 += 1
                if data[i][j] <= data[k][j]:
                    break
            for k in range(i + 1, m):
                s2 += 1
                if data[i][j] <= data[k][j]:
                    break
            for k in range(j + 1, n):
                s3 += 1
                if data[i][j] <= data[i][k]:
                    break
            for k in range(j - 1, -1, -1):
                s4 += 1
                if data[i][j] <= data[i][k]:
                    break
            mx[i][j] = s1 * s2 * s3 * s4
            mx1[i][j].append([s1, s4, s2, s3])

    return max([max(m) for m in mx])


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    data = readdata(filename)
    print(f'part1: {part1(data)}')
    print(f'part2: {_part2(data)}')
    print(f'part2: {part2(data)}')
    print(f'part2: {part2_2(data)}')


if __name__ == "__main__":
    exit(main())
