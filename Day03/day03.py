with open('data.txt') as fid:
    txt = fid.read()

data = txt.split('\n')
di = {chr(65 + i): i + 27 for i in range(26)}
di.update({chr(96 + i + 1): i + 1 for i in range(26)})

total = 0
for line in data:
    s1, s2 = line[:len(line) // 2], line[len(line) // 2:]
    d = set(s1).intersection(set(s2))
    total += sum(map(lambda x: di[x], d))
print(total)

total = 0
for s1, s2, s3 in zip(data[::3], data[1::3], data[2::3]):
    d = set(s1).intersection(set(s2)).intersection(set(s3))
    total += sum(map(lambda x: di[x], d))
print(total)
