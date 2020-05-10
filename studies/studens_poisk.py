with open('D:/1.txt', encoding='utf-8') as inf:
    #p = inf.read().strip().split(';')
    file = inf.read()


file = file.strip()
file = file.splitlines()
data = []


print(file)

for item in file:
    s = item.split(';')
    data.append(s)

s = 0
mat = 0
phi = 0
rus = 0
cnt = 0
with open('D:/2.txt', 'w') as ouf:
    for user in data:
        for i in range(1, len(user)):
            s += int(user[i])
        print(round(s/(len(data[0])-1), 9), file=ouf)
        #ouf.write(str(round((s/(len(data[0])-1)), 9)) )
        #ouf.write('\n')
        mat += int(user[1])
        phi += int(user[2])
        rus += int(user[3])
        s = 0
        cnt += 1
    #print(mat/cnt, phi/cnt, rus/cnt, sep=', ', file=ouf)

    mat = str(round((mat/cnt), 9))
    phi = str(round((phi/cnt), 9))
    rus = str(round((rus/cnt), 9))
    print(mat, phi, rus, file=ouf)
    #ouf.write('%.9f %.9f %.9f'mat/cnt)
    #ouf.write(', '.join((mat, phi, rus)))
    #ouf.write('\n')

print(cnt)
