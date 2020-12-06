import string
from collections import defaultdict
data = open("input.txt", "r").read().splitlines()

checks = defaultdict(list)
for l in data:
    rdata = l[:7]
    cdata = l[7:]
    trr =rdata.maketrans("FB", "01")
    trc =cdata.maketrans("LR", "01")
    rval = int(rdata.translate(trr),2)
    cval = int(cdata.translate(trc),2)
    checks[rval].append(cval)
for r in checks:
    if len(checks[r]) != 8:
        print(r, checks[r], rval*8+cval)
