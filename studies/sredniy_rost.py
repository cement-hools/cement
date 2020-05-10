with open('D:/1.txt', encoding='utf-8') as inf:
    #p = inf.read().strip().split(';')
    file = inf.read()

file = file.strip()
#file = file.split('\t')
file = file.splitlines()
data = []

data_fin = []
for i in range(1,12):
    data_fin += [[i, 0, 0]]

for i in file:
    data += [i.split('\t')]
s = 0
for clas in range(1,12):
    for i in data:
        if i[0] == str(clas):
            s += 1
            for j in data_fin:
                if j[0] == clas:
                    j[1] += s
                    j[2] += int(i[2])
        s = 0

with open('D:/2.txt', 'w') as ouf:

    for row in data_fin:
        if row[2] == 0:
            print(row[0], '-', file=ouf)
        else:
            print(row[0], row[2]/row[1], file=ouf)
#print(file)
#print(data)
#print(data_fin)