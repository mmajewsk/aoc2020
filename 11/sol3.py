import numpy as np
data = open("input.txt", "r").read().splitlines()
data2 = [list(l) for l in data]
data3 = np.array(data2)
def ind_incr(a, incr):
    i,j = incr
    inds = []
    k, m = i, j
    for l in range(a):
        inds.append((k,m))
        k += i
        m += j
    return inds

prids_global = {}

def create_indicies(x):
    a,b = x.shape
    incrs_ar = [
        ind_incr(a, (-1,-1)),
        ind_incr(a, (-1, 0)),
        ind_incr(a, (-1, 1)),

        ind_incr(a, (1,-1)),
        ind_incr(a, (1,0)),
        ind_incr(a, (1,1)),

        ind_incr(a, (0,-1)),
        ind_incr(a, (0,1)),
    ]
    return incrs_ar


def produce_ind(arr, i,j):
    global inshape_indeces
    ind = []
    for line in np.array(inshape_indeces):
        nn = []
        newline = line + [i,j]
        for v in newline:
            if v[0] < 0 or v[1] <0 or v[0] >= arr.shape[0] or v[1] >= arr.shape[1]:
                continue
            else:
                nn.append(v)
        ind.append(nn)
    return ind

def get_visible(arr, i,j):
    key = str(i)+','+str(j)
    if prids_global.get(key) is None:
        prids = produce_ind(arr, i,j)
        prids_global[key] = prids
    else:
        prids = prids_global[key]
    c = 0
    for k in range(8):
        for m,n in prids[k]:
            if arr[m,n] == '#':
                c += 1
                break
            elif arr[m,n] == 'L':
                break
    return c

def process(d_in):
    data4 = d_in.copy()
    data5 = np.zeros(d_in.shape,dtype=np.object)
    linds = np.argwhere(d_in == 'L')
    lindsapp = np.apply_along_axis(lambda x: get_visible(d_in, x[0], x[1])==0, 1, linds.copy())
    changids = linds[lindsapp].T
    data4[changids[0], changids[1]] = '#'
    linds2 = np.argwhere(data4 == '#')
    data5 = data4.copy()
    linds2 = np.argwhere(data4 == '#')
    lindsapp2 = np.apply_along_axis(lambda x: get_visible(data4, x[0], x[1])>=5, 1, linds2.copy())
    changids2 = linds2[lindsapp2].T
    data5[changids2[0], changids2[1]] = 'L'
   return data5

d_new = data3.copy()
print("oooo")
print(d_new)
d_prev = np.zeros(data3.shape,dtype=np.object)
inshape_indeces = create_indicies(data3)
it = 0
print(d_new.shape)
while not np.all(d_new ==d_prev):
    it += 1
    print("it", it)
    d_prev = d_new.copy()
    d_new = process(d_new)

unique, counts = np.unique(d_new, return_counts=True)
print(dict(zip(unique, counts)))
