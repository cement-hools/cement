# put your python code here
n = 10#int(input())
m = []
w = 1
c = 1
n1 = n
n2 = -n
k1 = 0
k2 = -1
с = 0
for i in range(n):
    a = list()
    for j in range(1, n + 1):
        a.append(0)
    m.append(a)

while w <= n ** 2:
    for i in range(k1, n1):
        #if m[k1][i] == 0:
            m[k1][i] = w
            w += 1

    for i in range(k1+1, n1-1):
        #if m[i][n1-1] == 0:
            m[i][n1-1] = w
            w += 1

    for i in range(k2, n2, -1):
        #if m[k2][i] == 0:
            m[k2][i] = w
            w += 1

    for i in range(k2, n2, -1):
        #if m[i][n2] == 0:
            m[i][n2] = w
            w += 1
    k1 += 1
    n1 -= 1
    k2 -= 1
    n2 += 1
    с += 1
for i in m:
    for j in i:
        print(j, end='\t')
    print()
