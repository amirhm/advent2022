import sys


def readdata(filename):
    with open(filename) as fid:
        txt = fid.read().split('\n')
    return txt


class folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.folders = {}
        self.files = []
        self.size = None
        self.parent = parent


def parse_tree(lines):
    root = folder('root')
    cur = root
    n = len(lines)
    idx = 0
    while idx < n - 1:
        p1, p2, *p3 = lines[idx].split()
        if p1 == "$":  # commands
            if p2 == "ls":
                while idx < n - 1 and (not lines[idx + 1].startswith("$")):
                    idx += 1
                    p1, p2, *p3 = lines[idx].split()
                    if p1 == "dir":
                        cur.folders.update({p2: folder(p2, cur)})
                    else:
                        cur.files.append((p1, p2))

            elif p2 == "cd":
                if p3[0] == "..":
                    cur = cur.parent
                elif p3[0] == "/":
                    cur = root
                elif p3[0] in cur.folders:
                    cur = cur.folders[p3[0]]
        idx += 1

    # getsize:
    def dfs(node):
        if not node:
            return
        size = sum([dfs(n) for _, n in node.folders.items()])
        size += sum([int(file[0]) for file in node.files])
        node.size = size
        return size
    dfs(root)
    return root


def part1(root_tree):
    lst = []

    def smallnodes(node):
        if not node:
            return
        if node.size < 100_000:
            lst.append(node.size)
        for _, n in node.folders.items():
            smallnodes(n)
    smallnodes(root_tree)
    return sum(lst)


def part2(root_tree):
    value = 30_000_000 - (70000000 - root_tree.size)
    lst = []

    def smallnodes(node):
        if not node:
            return
        lst.append(node.size)
        for _, n in node.folders.items():
            smallnodes(n)
    smallnodes(root_tree)
    lst.sort()
    return list(filter(lambda x: x > value, lst))[0]


def main():
    _, filename, *_ = *sys.argv, "data.txt"
    txt = readdata(filename)
    root = parse_tree(txt)
    print(f'part1: {part1(root)}')
    print(f'part2: {part2(root)}')


if __name__ == "__main__":
    exit(main())
