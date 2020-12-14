import math
data = open("input.txt", "r").read().splitlines()
data2 = [(l[0], int(l[1:])) for l in data]
x, y = 0, 0
orientation = 0 # starting east counterclockwise
for c, v in data2:
    if c == 'R':
        orientation -= v
    if c == 'L':
        orientation += v


    if orientation >= 360 or orientation<0 :
        orientation = orientation % 360
        if orientation < 0:
            orientation = 360 + orientation

    if c == 'F':
        if orientation == 0:
            c = 'E'
        elif orientation == 90:
            c = 'N'
        elif orientation == 180:
            c = 'W'
        elif orientation == 270:
            c = 'S'
        else:
            print('scream', c,v, orientation)
            break
        # y += math.sin(math.radians(orientation)) * v
        # x += math.cos(math.radians(orientation)) * v
    if c == 'N':
        y += v
    if c == 'S':
        y -= v
    if c == 'E':
        x += v
    if c== 'W':
        x -= v
    print(c,v, x,y, orientation)
print(math.floor(abs(x))+math.floor(abs(y)))
