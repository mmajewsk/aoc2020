data = open("input1.txt", "r").read().splitlines()
data = [int(d) for d in data[0]]

from itertools import cycle
from collections import deque
cups = deque(data[:])

cur_ind = 0
thind = 0
highest = max(cups)
smallest = min(cups)
current = cups[cur_ind]
print()
print("----------------------------------")
print()
for i in range(100):
    # picked = cycle(cups)
    print("-- move {} --)".format(i+1))
    print("cups: {}".format(cups))
    cups_cpy = cups.copy()
    picked = []
    cur_ind = thind
    if cur_ind+4 >= len(cups_cpy):
        cups.rotate(-3)
        cur_ind -= 3
    a = cups[cur_ind+1]
    b = cups[cur_ind+2]
    c = cups[cur_ind+3]
    print("picked", a,b,c)
    cups.remove(a)
    cups.remove(b)
    cups.remove(c)
    destination = current - 1
    while destination in [a,b,c]:
        destination -= 1
    if destination <= 0:
        destination = max(cups)
    put_i = cups.index(destination)
    print(abs(put_i-cur_ind))
    cups.insert(put_i+1, c)
    cups.insert(put_i+1, b)
    cups.insert(put_i+1,a)
    thind = cups.index(current)+1
    if thind >= len(cups):
        cups.rotate(-2)
        thind = cups.index(current)+1
    current = cups[thind]
    print("destination: {}".format(destination))
    print("cur: {}".format(current))
    print("placed: {}".format(cups))
    print()
start = 0
lcups = list(cups)
print(cups)
onind = lcups.index(1)
collected = lcups[onind+1:] + lcups[:onind]
print("colledted", "".join([str(c) for c in collected]))
