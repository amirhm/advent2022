import sys
from functools import reduce


def readdata(filename):
    with open(filename) as fid:
        txt = [[int(val) for val in line] for line in fid.read().split('\n')]
    return txt


def part1(data):
    m, n = len(data), len(data[0])
    field = {}

    def dfs(i, j, direction):
        if (i, j, direction) in field:
            return field[(i, j, direction)]
        if (
            ((i == 0) and direction == "t")
            or ((i == m - 1) and direction == "b")
            or ((j == 0) and direction == "l")
            or ((j == n - 1) and direction == "r")
           ):
            field[(i, j, direction)] = (True, data[i][j])

        if (0 < i) and direction == "t":
            mx = dfs(i - 1, j, "t")[1]
            field[(i, j, "t")] = (data[i][j] > mx), max(mx, data[i][j])
        if (i < m - 1) and direction == "b":
            mx = dfs(i + 1, j, "b")[1]
            field[(i, j, "b")] = (data[i][j] > mx), max(mx, data[i][j])
        if (j < n - 1) and direction == "r":
            mx = dfs(i, j + 1, "r")[1]
            field[(i, j, "r")] = (data[i][j] > mx), max(mx, data[i][j])
        if (0 < j) and direction == "l":
            mx = dfs(i, j - 1, "l")[1]
            field[(i, j, "l")] = (data[i][j] > mx), max(mx, data[i][j])
        return field[(i, j, direction)]

    s = 0
    for i in range(m):
        for j in range(n):
            s += any([dfs(i, j, d)[0] for d in 'bltr'])
    return s


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

    def dfs(i, j, direction):
        if (i, j, direction) in field:
            return field[(i, j, direction)]

        if direction == "top":
            idx = max(i - 1, 0)
            mx = data[i - 1][j]
            while (idx > 0) and (data[i][j] > mx):
                (mx, idx), _ = dfs(idx, j, "top")
            field[(i, j, "top")] = ((mx, idx), i - idx)

        if direction == "left":
            idx = max(j - 1, 0)
            mx = data[i][j - 1]
            while (idx > 0) and (data[i][j] > mx):
                (mx, idx), _ = dfs(i, idx, direction)
            field[(i, j, direction)] = ((mx, idx), j - idx)

        if direction == "bottom":
            idx = min(i + 1, m - 1)
            mx = data[idx][j]
            while (idx < m - 1) and (data[i][j] > mx):
                (mx, idx), _ = dfs(idx, j, direction)
            field[(i, j, direction)] = ((mx, idx), idx - i)

        if direction == "right":
            idx = min(j + 1, n - 1)
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
