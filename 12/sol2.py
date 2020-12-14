import math
data = open("input.txt", "r").read().splitlines()
data2 = [(l[0], int(l[1:])) for l in data]
x, y = 0, 0
wx, wy = 10, 1
for c, v in data2:
    if (c== 'R' or c =='L') and (v >= 360 or v<0)  :
        v = v % 360
        if v < 0:
            v = 360 + v

    if c == 'L' or c == 'R':
        if abs(v) == 180:
            wx = -wx
            wy = -wy
        if (c =='L' and v == 90) or (c == 'R' and v == 270):
            tx = -wy
            ty = wx
            wy = ty
            wx = tx
        if (c =='R' and v == 90) or (c == 'L' and v == 270):
            tx = wy
            ty = -wx
            wy = ty
            wx = tx

    if c == 'F':
        x = x + wx * v
        y = y + wy * v

    if c == 'N':
        wy = wy + v
    if c == 'S':
        wy = wy - v
    if c == 'E':
        wx = wx + v
    if c== 'W':
        wx = wx - v
    print(c,v, wx, wy, x,y)

print(math.floor(abs(x))+math.floor(abs(y)))
