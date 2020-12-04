
data = open("input.txt", "r").read().splitlines()
elements = []
tmp_el = []
data.append('')
for n, i in enumerate(data):
    if i == '' or n == len(data):
        elements.append(tmp_el)
        tmp_el = []
        continue
    tmp_el += i.split()
allowd=[
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid',
'byr'
]

elements_d = []
counter = 0
eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl' ,'oth']
for d in elements:
    dic = {}
    for j in d:
        k,v = j.split(":")
        dic[k] = v
    # if len(set(allowd).intersection(set(dic.keys()))) == len(allowd):
    s = 0
    for c in allowd:
        if c in dic.keys():
            s += 1
    if s == 7:
        chck = [len(dic['byr']) == 4 and 1920<=int(dic['byr'])<=2002,
        len(dic['iyr']) == 4 and 2010<=int(dic['iyr'])<=2020,
        len(dic['eyr']) == 4 and 2020<=int(dic['eyr'])<=2030,
         (dic['hgt'][-2:] == 'cm' and 150<=int(dic['hgt'][:-2])<=193) or (dic['hgt'][-2:] == 'in' and 59<=int(dic['hgt'][:-2])<=76),
         (dic['hcl'][0] == "#" and len(dic['hcl'][1:])==6 and dic['hcl'][1:].isalnum() and dic['hcl'][1:].lower() == dic['hcl'][1:]),
         (dic['ecl'] in eyes),
         (len(dic['pid'])==9)]
        if all(chck):
            counter +=1



    
    elements_d.append(dic)


# print(data)
# print(elements)
print(elements_d[-1])
print(counter)
