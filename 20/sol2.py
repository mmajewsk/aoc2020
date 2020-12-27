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
    matches[",".join(v[0])].append((k,1))
    matches[",".join(v[-1])].append((k,2))
    matches[",".join(v[:,0])].append((k,3))
    matches[",".join(v[:,-1])].append((k,4))
    matches[",".join(v[0][::-1])].append((k,5))
    matches[",".join(v[-1][::-1])].append((k,6))
    matches[",".join(v[:,0][::-1])].append((k,7))
    matches[",".join(v[:,-1][::-1])].append((k,8))
    if True:
        pass

matches_count = defaultdict(int)
for k,v in matches.items():
    if len(v) != 2:
        continue
    else:
        # print(k,v)
        for val in v:
            matches_count[val[0]] += 1

d = len(matches_count)
image = np.zeros((int(np.sqrt(d)), int(np.sqrt(d))), dtype=object)
srtd = sorted(matches_count.items(), key=lambda x: x[1], reverse=True)

corners = list(filter(lambda x: x[1] == 4, matches_count.items()))

# all allowed operations
operations ={
    0: lambda x:x,
    1: lambda x:np.flip(x,1),
    2: lambda x:np.flip(x,0),
    3: lambda x:np.rot90(x, 1),
    4: lambda x:np.rot90(x, 2),
    5: lambda x:np.rot90(x, 3),
}

# finding upper left for starting point
msides=[]
for candidate in corners:
    pairs = []
    for sides, m in matches.items():
        if candidate[0] in [x[0] for x in m] and len(m) > 1:
            assert len(m) == 2
            msides.append(m)
            prs = dict(m)
            candside = prs.pop(candidate[0])
            therside = list(prs.values())[0]
            pairs.append((candside, therside))
        if (4,3) not in pairs and (2,1) not in pairs:
            continue
        else:
            left_upper = candidate[0]


image_rendered= np.zeros((int(np.sqrt(d)), int(np.sqrt(d))), dtype=object)

found = {left_upper}
image[0,0] = data2[left_upper]
from itertools import combinations
def check_fit(mat, i, j):
    if i != 0:
        c = image[i-1,j][-1,:]
        d = mat[0,:]
        if not np.all(c ==d):
            return False
    if j!= 0:
        c = image[i,j-1][:,-1]
        d = mat[:,0]
        if not np.all(c== d):
            return False
    return True

def get_candidate(i,j):
    if j!= 0:
        s = ",".join(image[i,j-1][:,-1])
        m = matches[s]
        only = set([ y[0] for y in m]) - found
        assert len(only) ==1
        choice = next(iter(only))
        return choice
    elif j== 0:
        s = ",".join(image[i-1,j][-1,:])
        m = matches[s]
        only = set([ y[0] for y in m]) - found
        assert len(only) ==1
        choice = next(iter(only))
        return choice

manip_oper = list(combinations(operations.keys(), 2))

for k in range(image.shape[0]):
    for l in range(image.shape[0]):
        if k==l==0:
            continue
        else:
            candidate_label = get_candidate(k,l)
            candidate = data2[candidate_label]
            cand_ok = False
            for a,b in manip_oper:
                postb = operations[b](candidate)
                ctr = operations[a](postb)
                if check_fit(ctr, k, l):
                    cand_ok = True
                    found.add(candidate_label)
                    image[k,l] = ctr
            assert cand_ok
img2 = np.zeros_like(image)

for k in range(image.shape[0]):
    for l in range(image.shape[0]):
        img2[k,l] = image[k,l][1:-1,1:-1]

noborder = np.asarray(np.bmat([i.tolist() for i in img2]))

monster = [
    "##################O#",
    "O####OO####OO####OOO",
    "#O##O##O##O##O##O###"
]

popek = np.array([[x== "O" for x in r] for r in monster])
suma = sum(sum(popek))
flatmonster = np.array(list(zip(*popek.nonzero())))

occs = dict(zip(*np.unique(noborder.flatten(), return_counts=True)))
hashcount= occs['#']

for a,b in manip_oper:
    postb = operations[b](noborder)
    nb = operations[a](postb)
    found_monster= []
    for (i,j),x in np.ndenumerate(noborder):
        nowmonster= flatmonster + (i,j)
        if popek.shape[1]+j >= noborder.shape[1] or popek.shape[0] + i >= noborder.shape[0]:
            continue
        end = nb[nowmonster.T[0], nowmonster.T[1]]
        # print(end=="#")
        if np.all(end=="#"):
            found_monster.append((i,j))
    if found_monster:
        print(hashcount - len(found_monster)*suma)
        break

