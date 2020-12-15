from collections import defaultdict
data = open("input.txt","r").read()
# data = open("input.txt","rt").read()
data2 = list(map(int, data.split(',')))
print(data2)
end =  30000000
lastindexof = lambda v,l: len(l) - 1 - l[::-1].index(v)
spoken = [] + data2
liof_d = defaultdict(list)
count_d = defaultdict(int)
for i in range(len(data2)):
    liof_d[data2[i]].append(i)
    count_d[data2[i]] = 1
# print(liof_d)
for i in range(len(data2), end):
    prev = spoken[i-1]
    # print('start', i,prev)
    if count_d[prev] > 1:
        lio = liof_d[prev][-2]
        diff = (i)-(lio+1)
        spoken.append(diff)
        # print(lio, diff, liof_d)
        liof_d[diff].append(i)
        count_d[diff] += 1
    elif count_d[prev] <= 1:
        spoken.append(0)
        liof_d[0].append(i)
        count_d[0] += 1
print(spoken[-1])
