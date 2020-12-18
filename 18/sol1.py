
data = open("input.txt", "r").read().splitlines()

def calculate(l):
    tmp = int(l[0])
    size = len(l)
    for i, v in enumerate(l):
        if i==0:
            continue
        if v == '*':
            operation = lambda a,b: a*b
        elif v == '+':
            operation = lambda a,b: a+b
        else:
            tmp = operation(tmp, int(v))
    return tmp

def consume(openl):
    mst_rcnt = openl.pop()
    tmp = calculate(mst_rcnt)
    if len(openl) >= 1:
        openl[-1].append(tmp)
        return openl
    else:
        return tmp

sms = []
suma = 0
for d in data:
    openl = []
    levels = []
    vls = d.split(' ')
    level = 0
    curit = 0
    for i,v in enumerate(vls):
        if len(openl)==0 and '(' not in v and ')' not in v:
            levels.append(v)
        elif len(openl) != 0 and '(' not in v and ')' not in v:
            openl[-1].append(v)
        if '(' in v:
            p = v.count("(")
            for j in range(p):
                openl.append([])
            openl[-1].append(v[p:])
        if ')' in v:
            p = v.count(")")
            openl[-1].append(v[:-p])
            for j in range(p):
                openl = consume(openl)
            if not isinstance(openl, list):
                levels.append(openl)
                openl = []
    res = calculate(levels)
    suma += res
print(suma)
