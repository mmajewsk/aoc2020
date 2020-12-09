import itertools
data = open("input.txt", "r").read().splitlines()
data2 = [int(k) for k in data]
l = 25
for i in range(l, len(data2)):
    comb = list(itertools.combinations(data2[i-l:i],2))
    sums = [sum(k) for k in comb]
    v = data2[i]
    if v in sums:
        continue
    else:
        print(v)
        print(data2[i-l:i])
        print(list(comb))
        print(sums)
        break
b = False
for i in range(len(data2)):
    if b:
        break
    for j in range(i):
        m = data2[j:i]
        if sum(data2[j:i]) == v:
            print("ddd")
            print(m)
            print(i,j)
            print(min(m) + max(m))
            b= True
            break
