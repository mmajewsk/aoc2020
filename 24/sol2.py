data = open("input.txt", "r").read().splitlines()

s = data[0]
tr1 = dict(zip(['se','sw','nw','ne'], 'abcd'))
def wtr(sstr, tr):
    for p in tr:
        sstr = sstr.replace(p, tr[p])
    return sstr

def fix(sstr):
    sstr = wtr(sstr, tr1)
    tr2 = s.maketrans('ew', 'ef')
    return sstr.translate(tr2)

data2 = [fix(x) for x in data]

class Hex:
    allhexes = {}
    neis = {
        'a': (0, 1, -1),
        'b': (1, 0, -1),
        'c': (0, -1, 1),
        'd': (-1, 0, 1),
        'e': (-1, 1, 0),
        'f': (1, -1, 0),
    }
    def __init__(self, tid):
        self.n = {}
        self.tid = tid
        self.touched = 0
        self.flipped = 0
        Hex.allhexes[tid] = self

    def go(self, x):
        if self.n.get(x) is None:
            dtid = Hex.neis[x]
            new_tid = self.tid[0]+dtid[0], self.tid[1]+dtid[1], self.tid[2]+dtid[2]
            if Hex.allhexes.get(new_tid) is None:
                self.n[x] = Hex(new_tid)
            else:
                self.n[x] = Hex.allhexes[new_tid]
        self.n[x].touched += 1
        return self.n[x]

start = Hex((0,0,0))
for d in data2:
    new = start
    for l in d:
        new = new.go(l)
    new.flipped += 1

import copy
def count_adj(h):
    counter = 0
    for k in h.neis:
        if h.go(k).flipped%2 ==1:
            counter += 1
    return counter

def artrules(m):
    mapkeys = list(m.keys())
    adjacentcy = {k:count_adj(m[k]) for k in mapkeys}
    toflip = []
    for k,v in adjacentcy.items():
        #black
        if m[k].flipped%2==1  and (v==0 or v>2):
            toflip.append(k)
        #white
        if m[k].flipped%2==0 and v==2:
            toflip.append(k)
    return toflip

def count_black(m):
    flipped = list(filter(lambda x:x%2==1, [x.flipped for k,x in m.items()]))
    return len(flipped)

x,y,z= list(zip(*Hex.allhexes.keys()))
xmin, xmax = min(x), max(x)
ymin, ymax = min(y), max(y)
zmin, zmax = min(z), max(z)

print("prefill", len(Hex.allhexes))

for h in list(Hex.allhexes.values()):
    for k in h.neis:
        h.go(k)

print("postfill", len(Hex.allhexes))

for i in range(100):
    toflip = artrules(Hex.allhexes)
    for ind in toflip:
        Hex.allhexes[ind].flipped += 1
    print(i, count_black(Hex.allhexes))
