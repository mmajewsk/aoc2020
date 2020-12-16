data = open("input.txt", "r").read().splitlines()
data.append("\n")
data2 = []
tmp = []
for v in data:
    if v != '':
        tmp.append(v)
    if v == '' or v =='\n':
        data2.append(tmp)
        tmp = []

rules = data2[0]
my_ticket = data2[1]
nearby = data2[2]

rules2 = set()
rules_d = {}
for v in rules:
    ranges = v.split(":")[1].split('or')
    range1 = list(map(int, ranges[0].split('-')))
    range2 = list(map(int, ranges[1].split('-')))
    k = v.split(':')[0]
    rules_d[k] = []
    rules_d[k] += range(range1[0], range1[1]+1)
    rules_d[k] += range(range2[0], range2[1]+1)
    rules2 |= set(rules_d[k])

notinside = []
inside = []
# filtering invalid
for v in nearby[1:]:
    if v == '\n':
        continue
    notin = False
    rvals = list(map(int,v.split(',')))
    if set(rvals).issubset(rules2):
        inside.append(rvals)

# columns, not rows
in_t = list(zip(*inside))

# which columns fulfill rules
from collections import defaultdict
ordering = defaultdict(list)
for i,v in enumerate(in_t):
    for k in rules_d:
        if set(v).issubset(set(rules_d[k])):
            ordering[k].append(i)
        ordering[k] = sorted(ordering[k])

# GOD OF SORT
inv_map = {}
srtd = sorted(ordering.items(), key = lambda v: len(v[1]))
for i,v in enumerate(srtd):
    if i-1 >= 0:
        g = set(v[1]) - set(srtd[i-1][1])
    else:
        g = set(v[1])
    inv_map[list(g)[0]] = v[0]

# For(d) Multiplah
dlg = list(map(int,my_ticket[1].split(',')))
mltp = 1
for i, a in enumerate(dlg):
    if 'departure' in inv_map[i]:
        # print(inv_map[i], a)
        mltp *= a
print(mltp)
