from collections import Counter
data = open("input.txt", "r").read().splitlines()
data.append('')
groups = []

g = []
for l in data:
    if l == '':
        groups.append(g)
        g = []
    else:
        g.append(l)

summer = 0
for g in groups:
    s = ""
    for l in g:
        s += l
    size = len(g)
    c = Counter(s)
    for k in c:
        if c[k] == size:
            summer += 1
print(summer)
