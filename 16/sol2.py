
data = open("input.txt", "r").read().splitlines()
data.append("\n")
# print(data)
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
    for i in range(range1[0], range1[1]+1):
        rules2.add(i)
        rules_d[k].append(i)
    for i in range(range2[0], range2[1]+1):
        rules_d[k].append(i)
        rules2.add(i)

notinside = []
inside = []
for v in nearby[1:]:
    if v == '\n':
        continue
    notin = False
    rvals = list(map(int,v.split(',')))
    if set(rvals).issubset(rules2):
        inside.append(rvals)

in_t = list(zip(*inside))
# print(inside)
# print(rules_d)

from collections import defaultdict
ordering = defaultdict(list)
for i,v in enumerate(in_t):
    # print(v)
    for k in rules_d:
        # print(set(v), set(rules_d[k]), set(v).issubset(set(rules_d[k])))
        if set(v).issubset(set(rules_d[k])):
            ordering[k].append(i)

for k in ordering:
    print(k, ordering[k])

good = {}
allkeys = list(ordering.keys())
found_numb = []
for i in range(20):
    for i,a in enumerate(allkeys):
        daf = set(ordering[a]) - set(found_numb)
        print(daf)
        if len(daf) == 1:
            good[a] = list(daf)[0]
            found_numb.append(good[a])
            del allkeys[i]
            break
    print("all")
    print(allkeys)

inv_map = {v: k for k, v in good.items()}
dlg = list(map(int,my_ticket[1].split(',')))
mltp = 1
for i, a in enumerate(dlg):
    if 'departure' in inv_map[i]:
        print(inv_map[i], a)
        mltp *= a
print(mltp)



# print(ordering)
#
# sol = dict(zip(ordering, list(map(int,my_ticket[1].split(',')))))
# print(sol)
# tmpl = 1
# for k in sol:
#     if 'departure' in k:
#         tmpl *= sol[k]
#         print(k, sol[k])
# print(tmpl)
# print(tmpl)
