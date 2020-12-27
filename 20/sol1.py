import numpy as np
data = open("input.txt", "r").read().splitlines()
data2 = {}
nl = []
tid = None
for d in data:

    if d =='':
        continue
    if 'Tile' in d:
        if tid is None:
            tid = d.split(' ')[1][:-1]
        data2[tid] = np.array(nl)
        tid = d.split(' ')[1][:-1]
        nl = []
        continue
    nl.append([x for x in d])

data2[tid] = np.array(nl)

from collections import defaultdict
matches = defaultdict(list)
for k,v  in data2.items():
    matches[",".join(v[0])].append(k)
    matches[",".join(v[-1])].append(k)
    matches[",".join(v[:,0])].append(k)
    matches[",".join(v[:,-1])].append(k)
    matches[",".join(v[0][::-1])].append(k)
    matches[",".join(v[-1][::-1])].append(k)
    matches[",".join(v[:,0][::-1])].append(k)
    matches[",".join(v[:,-1][::-1])].append(k)

    if True:
        pass

matches_count = defaultdict(int)
for k,v in matches.items():
    if len(v) != 2:
        continue
    else:
        print(k,v)
        for val in v:
            matches_count[val] += 1
mlt = 1
for k,v in matches_count.items():
    if v == 4:
        print(k)
        mlt *= int(k)
# -*- tab-width: 2 -*-
