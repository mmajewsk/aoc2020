data = open("input.txt", "r").read().splitlines()
count = 0


def slope(r, d):
    count = 0
    k = r
    for i, l in enumerate(data[::d]):
        if i == 0:
            continue
        count += 1 if l[k] == "#" else 0
        k += r
        if k >= len(l):
            k = k % len(l)
    return count


d = [
    slope(1, 1),
    slope(3, 1),
    slope(5, 1),
    slope(7, 1),
    slope(1, 2),
]
s = 1
for i in d:
    s *= i
print(s)
