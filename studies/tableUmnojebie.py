a = 7
b = 10
c = 5
d = 6

'''for t in range(c, d+1):
    print('\t', t,end ='')
print('')'''

for i in range(1, 10):
    print(i, '\t', end='')
    for n in range(2, 10):
        print(i, '*', n, '=', i*n, '\t', end='', sep ='')
    print('')