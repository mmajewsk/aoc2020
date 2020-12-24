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
            if self.allhexes.get(new_tid) is None:
                self.n[x] = Hex(new_tid)
            else:
                self.n[x] = Hex.allhexes[new_tid]
        self.n[x].touched += 1
        return self.n[x]

# use the fact that hex can be represented as
# grid with every second row offset by 1
start = Hex((0,0,0))
for d in data2:
    new = start
    for l in d:
        new = new.go(l)
    new.flipped += 1

flipped = list(filter(lambda x:x%2==1, [x.flipped for k,x in Hex.allhexes.items()]))
