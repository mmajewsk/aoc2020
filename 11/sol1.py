import numpy as np
data = open("input.txt", "r").read().splitlines()
data2 = [list(l) for l in data]
def wrap_nb(x,i,j):
    nb = []
    inds = (i,j-1), (i,j+1), (i-1,j), (i+1,j), (i-1,j-1), (i+1,j+1), (i+1,j-1), (i-1,j+1)
    for id in inds:
       try:
           if id[0] >= 0 and id[1] >= 0:
               nb.append(x[id[0], id[1]])
       except:
           continue
    return nb
data3 =np.array(data2)
print()
print(data3)
print(wrap_nb(data3,0,0))
print()

def process(d_in):
    data4 = np.zeros(d_in.shape,dtype=np.object)
    data5 = np.zeros(d_in.shape,dtype=np.object)

    for i in range(len(d_in)):
        for j in range(len(d_in[0])):
            data4[i,j] = '#' if (d_in[i,j] == 'L' and wrap_nb(d_in, i,j).count('#') == 0) else d_in[i,j]
    for i in range(len(d_in)):
        for j in range(len(d_in[0])):
            wrp = wrap_nb(data4, i,j)
            wrp_cnt = wrp.count('#') >= 4
            cond = (wrp_cnt and data4[i,j]=='#')
            if cond:
                data5[i,j] = 'L'
            elif data4[i,j] == '#':
                data5[i,j] = '#'
            else:
                data5[i,j] = data4[i,j]
    return data5

d_new = data3.copy()
print("oooo")
print(d_new)
d_prev = np.zeros(data3.shape,dtype=np.object)
while not np.all(d_new ==d_prev):
    d_prev = d_new.copy()
    d_new = process(d_new)

unique, counts = np.unique(d_new, return_counts=True)
print(dict(zip(unique, counts)))

print(wrap_nb(d_new, 0, 2))
