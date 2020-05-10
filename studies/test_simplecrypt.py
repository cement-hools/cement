import simplecrypt

with open("d:\encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("d:\passwords.txt", "rb") as inp:
    key = inp.readlines()
a = 0
for i in key:
        a += 1
        i = i.strip()
        #i = i.split()
        print(a, i, 'Key')
        try:
            result = simplecrypt.decrypt(i, encrypted)
        except:
            print('Key is not accepted')
        else:
            print('Congratilation : ', result.decode('utf8'))
            break

