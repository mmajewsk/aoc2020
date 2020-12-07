
data = open("input.txt", "r").read().splitlines()
dict_graph = {}
for l in data:
    src, dst = l.split(' bags contain ')
    o = dst.split(',')
    o = [k.replace('.','').replace(' bags', '').replace(' bag', '') for k in o]

    # print(src, o)
    o = [k[1:] if k[0]==' ' else k for k in o]
    # print(src, o)
    if len(o) == 1 and o[0] == 'no other':
        d_small = {}
    else:
        d_small = {}
        for k in o:
            d_small[k[2:]] =  int(k[0])
    # print(src, d_small)
    dict_graph[src] = d_small

looking = 'shiny gold'

def rec(chk, all_d):
    print(chk)
    d_chk = all_d[chk]
    if d_chk == {}:
        return 0
    s = 0
    for d in d_chk:
        v = rec(d, all_d)
        # print(d_chk[d], v)
        s += int(d_chk[d]) + int(d_chk[d])*v
        print(chk, int(d_chk[d]), d,v)
    return s

print(rec(looking, dict_graph))

