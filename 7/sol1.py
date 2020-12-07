
data = open("input.txt", "r").read().splitlines()
dict_graph = {}
for l in data:
    src, dst = l.split(' bags contain ')
    o = dst.split(',')
    o = [k.replace('.','').replace(' bags', '').replace(' bag', '') for k in o]

    print(src, o)
    o = [k[1:] if k[0]==' ' else k for k in o]
    print(src, o)
    if len(o) == 1 and o[0] == 'no other':
        d_small = {}
    else:
        d_small = {}
        for k in o:
            d_small[k[2:]] =  int(k[0])
    print(src, d_small)
    dict_graph[src] = d_small

looking = 'shiny gold'
containing = []
l = 0
prev = 0
first = True
while True:
    for src,dst in dict_graph.items():
        if first and looking in dst.keys():
            # print("found:", looking, 'src', src, 'in', dst)
            containing.append(src)
        else:
            for c in containing:
                if src not in containing and c in dst.keys():

                    # print("found:", c, 'src', src, 'in', dst)
                    containing.append(src)
    first = False
    prev = l
    l = len(set(containing))
    if prev - l == 0:
        break
print(len(set(containing)))
