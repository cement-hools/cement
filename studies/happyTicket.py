b = int('023012')

print(b//100000)

a = list('200002')

for i in range(0, 6):
    a[i] = int(a[i])

    print(a[i])


a1 = a[0] + a[1] + a[2]
a2 = a[3] + a[4] + a[5]
if int(a1) == int(a2):
    print('Счастливый')
else:
    print('Обычный')

