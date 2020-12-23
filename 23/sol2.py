data = open("input.txt", "r").read().splitlines()
data = [int(d) for d in data[0]]

from itertools import cycle
from collections import deque
mil = 1_000_000

cups = deque(data+list(range(max(data)+1,mil+1)))
pcups = cups.copy()
pcups.rotate(-1)

highest = max(cups)

nexts = dict(zip(cups,pcups))
current = data[0]

for i in range(10_000_000):

    a = nexts[current]
    b = nexts[a]
    c = nexts[b]
    d = nexts[c]

    destination = current - 1
    while destination in [a,b,c]:
        destination -= 1
    if destination <= 0:
        destination = highest
        while destination in [a,b,c]:
            destination -= 1

    after_dest = nexts[destination]
    nexts[destination] = a
    nexts[c] = after_dest
    nexts[current] = d
    current = nexts[current]

print(nexts[1]* nexts[nexts[1]])
