with open('D:/1.txt') as inf:
    p = inf.readlines()


n = 'abc a bCd bC AbC BC BCD bcd ABC\n abc a bCd bC AbC BC BCD bcd ABC'
n = n.replace('\n', ' ')
n = n.split(' ')
dict = {}
res_key = 'z'
res_cnt = 0
for i in range(len(n)):
    n[i] = n[i].lower()
key = set(n)

for i in key:
    dict[i] = n.count(i)
for i in key:
    if dict[i] > res_cnt or dict[i] == res_cnt and i < res_key:

            res_cnt = dict[i]
            res_key = i

print(res_key, res_cnt)
otv = res_key+' '+str(res_cnt)
print(otv)

with open('D:/2.txt', 'w') as ouf:
    ouf.write(otv)
print(dict)
print(p)
#for k in dict.keys():
    #print(k)
#print(max(dict.values()))
#print(dict.keys())