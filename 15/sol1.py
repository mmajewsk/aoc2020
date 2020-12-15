data = open("input.txt","rt").read()
data2 = list(map(int, data.split(',')))
end = 2020
lastindexof = lambda v,l: len(l) - 1 - l[::-1].index(v)
spoken = [] + data2
for i in range(len(data2), end):
    prev = spoken[i-1]
    if spoken.count(prev) > 1:
        lio = lastindexof(prev, spoken[:-1])
        diff = (i)-(lio+1)
        spoken.append(diff)
    elif spoken.count(prev) <= 1:
        spoken.append(0)
print(spoken[-1])
