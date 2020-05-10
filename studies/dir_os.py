import os
import os.path
d = []
w = os.walk('D:\sample')

print('*')
os.chdir('D:\sample')
for root, dirs, files in os.walk('.'):
    print(root, dirs, files)
    print('*')
    for i in files:
        if i.endswith('.py'):
            print('***', root[2:], '***')
            root = root[2:]

            d.append(root)
            print(d, 'Spisok')
            break
d.sort()
print(d)
for i in d:
    print(i)
with open('D:/2.txt', 'w') as ouf:

    for i in d:
        print(i, file=ouf)