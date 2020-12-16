
data = open("input.txt", "r").read().splitlines()
data.append("\n")
print(data)
data2 = []
tmp = []
for v in data:
    if v != '':
        tmp.append(v)
    if v == '' or v =='\n':
        data2.append(tmp)
        tmp = []

print(data2)
rules = data2[0]
my_ticket = data2[1]
nearby = data2[2]

rules2 = set()
for v in rules:
    ranges = v.split(":")[1].split('or')
    range1 = list(map(int, ranges[0].split('-')))
    range2 = list(map(int, ranges[1].split('-')))
    for i in range(range1[0], range1[1]+1):
        rules2.add(i)
    for i in range(range2[0], range2[1]+1):
        rules2.add(i)
notinside = []
for v in nearby[1:]:
    if v == '\n':
        continue
    for i in list(map(int,v.split(','))):
        if i not in rules2:
            notinside.append(i)
            break
print(notinside)
print(sum(notinside))
print(nearby)
